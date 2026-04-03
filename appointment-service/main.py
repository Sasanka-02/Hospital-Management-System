from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from typing import List

from models import Appointment, AppointmentCreate
import service
import data_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    data_service.seed_data()
    print("\033[1m\033[32m" + "=" * 60 + "\033[0m")
    print("\033[1m  APPOINTMENT SERVICE\033[0m  ·  FastAPI + Uvicorn + Pydantic")
    print("\033[1m\033[32m" + "=" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  Status   : \033[32mRUNNING\033[0m")
    print("  \033[32m✔\033[0m  Port     : \033[33m8083\033[0m")
    print("  \033[32m✔\033[0m  Swagger  : \033[32mhttp://localhost:8083/docs\033[0m")
    print("  \033[32m✔\033[0m  API Base : \033[32mhttp://localhost:8083/api/appointments\033[0m")
    print("\033[32m" + "-" * 60 + "\033[0m")
    print("  Endpoints  : GET · GET/{id} · GET/patient/{id} · GET/doctor/{id}")
    print("               POST · PUT/{id} · DELETE/{id}")
    print("  Seed data  : 3 appointments (2 SCHEDULED, 1 COMPLETED)")
    print("\033[1m\033[32m" + "=" * 60 + "\033[0m\n")
    yield
    print("\n\033[31m  Appointment Service shutting down...\033[0m")


app = FastAPI(
    title="Appointment Service API",
    description="Hospital Appointment Management Microservice",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/appointments")


@app.get("/api/appointments", response_model=List[Appointment], tags=["Appointments"])
def get_all():
    return service.get_all_appointments()


@app.get("/api/appointments/{appt_id}", response_model=Appointment, tags=["Appointments"])
def get_by_id(appt_id: int):
    appt = service.get_appointment_by_id(appt_id)
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appt


@app.get("/api/appointments/patient/{patient_id}", response_model=List[Appointment], tags=["Appointments"])
def get_by_patient(patient_id: int):
    return service.get_by_patient(patient_id)


@app.get("/api/appointments/doctor/{doctor_id}", response_model=List[Appointment], tags=["Appointments"])
def get_by_doctor(doctor_id: int):
    return service.get_by_doctor(doctor_id)


@app.post("/api/appointments", response_model=Appointment, status_code=201, tags=["Appointments"])
def create(appt: AppointmentCreate):
    return service.create_appointment(appt)


@app.put("/api/appointments/{appt_id}", response_model=Appointment, tags=["Appointments"])
def update(appt_id: int, appt: AppointmentCreate, status: str = "SCHEDULED"):
    updated = service.update_appointment(appt_id, appt, status)
    if not updated:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return updated


@app.delete("/api/appointments/{appt_id}", status_code=204, tags=["Appointments"])
def delete(appt_id: int):
    if not service.delete_appointment(appt_id):
        raise HTTPException(status_code=404, detail="Appointment not found")
