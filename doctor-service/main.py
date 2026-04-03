from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from typing import List

from models import Doctor, DoctorCreate
import service
import data_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    data_service.seed_data()
    print("\033[1m\033[35m" + "=" * 60 + "\033[0m")
    print("\033[1m  DOCTOR SERVICE\033[0m  ·  FastAPI + Uvicorn + Pydantic")
    print("\033[1m\033[35m" + "=" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  Status   : \033[32mRUNNING\033[0m")
    print("  \033[32m✔\033[0m  Port     : \033[33m8082\033[0m")
    print("  \033[32m✔\033[0m  Swagger  : \033[35mhttp://localhost:8082/docs\033[0m")
    print("  \033[32m✔\033[0m  API Base : \033[35mhttp://localhost:8082/api/doctors\033[0m")
    print("\033[35m" + "-" * 60 + "\033[0m")
    print("  Endpoints  : GET · GET/{id} · POST · PUT/{id} · DELETE/{id}")
    print("  Seed data  : 3 doctors (Cardiology, Neurology, Pediatrics)")
    print("\033[1m\033[35m" + "=" * 60 + "\033[0m\n")
    yield
    print("\n\033[31m  Doctor Service shutting down...\033[0m")


app = FastAPI(
    title="Doctor Service API",
    description="Hospital Doctor Management Microservice",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/doctors")


@app.get("/api/doctors", response_model=List[Doctor], tags=["Doctors"])
def get_all():
    return service.get_all_doctors()


@app.get("/api/doctors/{doctor_id}", response_model=Doctor, tags=["Doctors"])
def get_by_id(doctor_id: int):
    doctor = service.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@app.post("/api/doctors", response_model=Doctor, status_code=201, tags=["Doctors"])
def create(doctor: DoctorCreate):
    return service.create_doctor(doctor)


@app.put("/api/doctors/{doctor_id}", response_model=Doctor, tags=["Doctors"])
def update(doctor_id: int, doctor: DoctorCreate):
    updated = service.update_doctor(doctor_id, doctor)
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated


@app.delete("/api/doctors/{doctor_id}", status_code=204, tags=["Doctors"])
def delete(doctor_id: int):
    if not service.delete_doctor(doctor_id):
        raise HTTPException(status_code=404, detail="Doctor not found")
