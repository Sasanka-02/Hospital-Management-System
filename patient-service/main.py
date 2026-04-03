from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from typing import List

from models import Patient, PatientCreate
import service
import data_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    data_service.seed_data()
    print("\033[1m\033[36m" + "=" * 60 + "\033[0m")
    print("\033[1m  PATIENT SERVICE\033[0m  ·  FastAPI + Uvicorn + Pydantic")
    print("\033[1m\033[36m" + "=" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  Status   : \033[32mRUNNING\033[0m")
    print("  \033[32m✔\033[0m  Port     : \033[33m8081\033[0m")
    print("  \033[32m✔\033[0m  Swagger  : \033[36mhttp://localhost:8081/docs\033[0m")
    print("  \033[32m✔\033[0m  API Base : \033[36mhttp://localhost:8081/api/patients\033[0m")
    print("\033[36m" + "-" * 60 + "\033[0m")
    print("  Endpoints  : GET · GET/{id} · POST · PUT/{id} · DELETE/{id}")
    print("  Seed data  : 3 patients loaded (O+, A+, B-)")
    print("\033[1m\033[36m" + "=" * 60 + "\033[0m\n")
    yield
    print("\n\033[31m  Patient Service shutting down...\033[0m")


app = FastAPI(
    title="Patient Service API",
    description="Hospital Patient Management Microservice",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/patients")


@app.get("/api/patients", response_model=List[Patient], tags=["Patients"])
def get_all():
    return service.get_all_patients()


@app.get("/api/patients/{patient_id}", response_model=Patient, tags=["Patients"])
def get_by_id(patient_id: int):
    patient = service.get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@app.post("/api/patients", response_model=Patient, status_code=201, tags=["Patients"])
def create(patient: PatientCreate):
    return service.create_patient(patient)


@app.put("/api/patients/{patient_id}", response_model=Patient, tags=["Patients"])
def update(patient_id: int, patient: PatientCreate):
    updated = service.update_patient(patient_id, patient)
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated


@app.delete("/api/patients/{patient_id}", status_code=204, tags=["Patients"])
def delete(patient_id: int):
    if not service.delete_patient(patient_id):
        raise HTTPException(status_code=404, detail="Patient not found")
