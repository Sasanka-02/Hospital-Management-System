from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from typing import List

from models import Medicine, MedicineCreate
import service
import data_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    data_service.seed_data()
    print("\033[1m\033[33m" + "=" * 60 + "\033[0m")
    print("\033[1m  PHARMACY SERVICE\033[0m  ·  FastAPI + Uvicorn + Pydantic")
    print("\033[1m\033[33m" + "=" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  Status   : \033[32mRUNNING\033[0m")
    print("  \033[32m✔\033[0m  Port     : \033[33m8084\033[0m")
    print("  \033[32m✔\033[0m  Swagger  : \033[33mhttp://localhost:8084/docs\033[0m")
    print("  \033[32m✔\033[0m  API Base : \033[33mhttp://localhost:8084/api/pharmacy\033[0m")
    print("\033[33m" + "-" * 60 + "\033[0m")
    print("  Endpoints  : GET · GET/{id} · GET/category/{cat} · POST · PUT/{id} · DELETE/{id}")
    print("  Seed data  : 3 medicines (Analgesic, Antibiotic, Antidiabetic)")
    print("\033[1m\033[33m" + "=" * 60 + "\033[0m\n")
    yield
    print("\n\033[31m  Pharmacy Service shutting down...\033[0m")


app = FastAPI(
    title="Pharmacy Service API",
    description="Hospital Pharmacy & Inventory Microservice",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/pharmacy")


@app.get("/api/pharmacy", response_model=List[Medicine], tags=["Pharmacy"])
def get_all():
    return service.get_all_medicines()


@app.get("/api/pharmacy/{med_id}", response_model=Medicine, tags=["Pharmacy"])
def get_by_id(med_id: int):
    med = service.get_medicine_by_id(med_id)
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return med


@app.get("/api/pharmacy/category/{category}", response_model=List[Medicine], tags=["Pharmacy"])
def get_by_category(category: str):
    return service.get_by_category(category)


@app.post("/api/pharmacy", response_model=Medicine, status_code=201, tags=["Pharmacy"])
def create(medicine: MedicineCreate):
    return service.create_medicine(medicine)


@app.put("/api/pharmacy/{med_id}", response_model=Medicine, tags=["Pharmacy"])
def update(med_id: int, medicine: MedicineCreate):
    updated = service.update_medicine(med_id, medicine)
    if not updated:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return updated


@app.delete("/api/pharmacy/{med_id}", status_code=204, tags=["Pharmacy"])
def delete(med_id: int):
    if not service.delete_medicine(med_id):
        raise HTTPException(status_code=404, detail="Medicine not found")
