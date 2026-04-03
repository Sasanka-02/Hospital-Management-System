from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from typing import List

from models import Notification, NotificationRequest
import service
import data_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    data_service.seed_data()
    print("\033[1m\033[34m" + "=" * 60 + "\033[0m")
    print("\033[1m  NOTIFICATION SERVICE\033[0m  ·  FastAPI + Uvicorn + Pydantic")
    print("\033[1m\033[34m" + "=" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  Status   : \033[32mRUNNING\033[0m")
    print("  \033[32m✔\033[0m  Port     : \033[33m8086\033[0m")
    print("  \033[32m✔\033[0m  Swagger  : \033[34mhttp://localhost:8086/docs\033[0m")
    print("  \033[32m✔\033[0m  API Base : \033[34mhttp://localhost:8086/api/notifications\033[0m")
    print("\033[34m" + "-" * 60 + "\033[0m")
    print("  Endpoints  : GET · GET/{id} · GET/patient/{id} · GET/status/{s}")
    print("               POST /send/appointment · POST /send/cancellation")
    print("               DELETE/{id}")
    print("  Types      : EMAIL, SMS")
    print("  Seed data  : 1 sample notification loaded")
    print("\033[1m\033[34m" + "=" * 60 + "\033[0m\n")
    yield
    print("\n\033[31m  Notification Service shutting down...\033[0m")


app = FastAPI(
    title="Notification Service API",
    description="Hospital Appointment Notification Microservice (Email/SMS)",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/notifications")


@app.get("/api/notifications", response_model=List[Notification], tags=["Notifications"])
def get_all():
    return service.get_all_notifications()


@app.get("/api/notifications/{notif_id}", response_model=Notification, tags=["Notifications"])
def get_by_id(notif_id: int):
    notif = service.get_notification_by_id(notif_id)
    if not notif:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notif


@app.get("/api/notifications/patient/{patient_id}", response_model=List[Notification], tags=["Notifications"])
def get_by_patient(patient_id: int):
    return service.get_by_patient(patient_id)


@app.get("/api/notifications/status/{status}", response_model=List[Notification], tags=["Notifications"])
def get_by_status(status: str):
    return service.get_by_status(status)


@app.post("/api/notifications/send/appointment", response_model=Notification, status_code=201, tags=["Notifications"])
def send_appointment(req: NotificationRequest):
    return service.send_appointment_notification(req)


@app.post("/api/notifications/send/cancellation", response_model=Notification, status_code=201, tags=["Notifications"])
def send_cancellation(req: NotificationRequest):
    return service.send_cancellation_notification(req)


@app.delete("/api/notifications/{notif_id}", status_code=204, tags=["Notifications"])
def delete(notif_id: int):
    if not service.delete_notification(notif_id):
        raise HTTPException(status_code=404, detail="Notification not found")
