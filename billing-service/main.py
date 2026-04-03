from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from typing import List

from models import Invoice, InvoiceCreate
import service
import data_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    data_service.seed_data()
    print("\033[1m\033[31m" + "=" * 60 + "\033[0m")
    print("\033[1m  BILLING SERVICE\033[0m  ·  FastAPI + Uvicorn + Pydantic")
    print("\033[1m\033[31m" + "=" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  Status   : \033[32mRUNNING\033[0m")
    print("  \033[32m✔\033[0m  Port     : \033[33m8085\033[0m")
    print("  \033[32m✔\033[0m  Swagger  : \033[31mhttp://localhost:8085/docs\033[0m")
    print("  \033[32m✔\033[0m  API Base : \033[31mhttp://localhost:8085/api/billing\033[0m")
    print("\033[31m" + "-" * 60 + "\033[0m")
    print("  Endpoints  : GET · GET/{id} · GET/patient/{id} · GET/status/{s}")
    print("               POST · PUT/{id} · DELETE/{id}")
    print("  Seed data  : 3 invoices (1 PAID, 2 PENDING)")
    print("\033[1m\033[31m" + "=" * 60 + "\033[0m\n")
    yield
    print("\n\033[31m  Billing Service shutting down...\033[0m")


app = FastAPI(
    title="Billing Service API",
    description="Hospital Billing & Invoice Microservice",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/billing")


@app.get("/api/billing", response_model=List[Invoice], tags=["Billing"])
def get_all():
    return service.get_all_invoices()


@app.get("/api/billing/{inv_id}", response_model=Invoice, tags=["Billing"])
def get_by_id(inv_id: int):
    inv = service.get_invoice_by_id(inv_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return inv


@app.get("/api/billing/patient/{patient_id}", response_model=List[Invoice], tags=["Billing"])
def get_by_patient(patient_id: int):
    return service.get_by_patient(patient_id)


@app.get("/api/billing/status/{status}", response_model=List[Invoice], tags=["Billing"])
def get_by_status(status: str):
    return service.get_by_status(status)


@app.post("/api/billing", response_model=Invoice, status_code=201, tags=["Billing"])
def create(invoice: InvoiceCreate):
    return service.create_invoice(invoice)


@app.put("/api/billing/{inv_id}", response_model=Invoice, tags=["Billing"])
def update(inv_id: int, invoice: InvoiceCreate, paymentStatus: str = "PENDING"):
    updated = service.update_invoice(inv_id, invoice, paymentStatus)
    if not updated:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return updated


@app.delete("/api/billing/{inv_id}", status_code=204, tags=["Billing"])
def delete(inv_id: int):
    if not service.delete_invoice(inv_id):
        raise HTTPException(status_code=404, detail="Invoice not found")
