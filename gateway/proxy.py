import httpx
import json
from fastapi import Request, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional

from routes import resolve

_HOP_BY_HOP = {"host", "content-length", "transfer-encoding", "connection"}


async def forward(request: Request, body_model: Optional[BaseModel] = None) -> Response:
    """
    Forward the incoming request to the correct upstream microservice.

    When FastAPI parses a Pydantic model from a POST/PUT request body,
    it consumes the raw byte stream — request.body() then returns empty bytes.
    To fix this, callers pass the already-parsed Pydantic model as body_model,
    and we re-serialize it to JSON before forwarding.
    """
    path = request.url.path
    upstream = resolve(path)

    if upstream is None:
        raise HTTPException(
            status_code=404,
            detail=f"No route configured for path: {path}"
        )

    target_url = upstream + path
    if request.url.query:
        target_url += "?" + request.url.query

    # Use re-serialized body if a Pydantic model was parsed by the handler
    if body_model is not None:
        body = body_model.model_dump_json().encode("utf-8")
    else:
        try:
            body = await request.body()
        except Exception:
            body = b""

    headers = {
        k: v for k, v in request.headers.items()
        if k.lower() not in _HOP_BY_HOP
    }

    # Ensure correct Content-Type for any request with a body
    if body:
        headers["content-type"] = "application/json"

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            upstream_response = await client.request(
                method=request.method,
                url=target_url,
                content=body,
                headers=headers,
            )
        except httpx.ConnectError:
            raise HTTPException(
                status_code=503,
                detail=(
                    f"Service unavailable — could not reach {upstream}. "
                    f"Make sure the microservice is running."
                )
            )

    excluded_response_headers = {
        "content-encoding", "transfer-encoding", "content-length"
    }
    response_headers = {
        k: v for k, v in upstream_response.headers.items()
        if k.lower() not in excluded_response_headers
    }

    return Response(
        content=upstream_response.content,
        status_code=upstream_response.status_code,
        headers=response_headers,
        media_type=upstream_response.headers.get("content-type", "application/json"),
    )
