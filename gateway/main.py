from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from contextlib import asynccontextmanager

from routes import ROUTES
from proxy import forward
from models import (
    PatientBody, DoctorBody, AppointmentBody,
    MedicineBody, InvoiceBody, NotificationBody
)

TAGS = [
    {"name": "Patient Service  :8081",      "description": "Manage hospital patients — routed to **http://localhost:8081**"},
    {"name": "Doctor Service  :8082",       "description": "Manage doctors & specializations — routed to **http://localhost:8082**"},
    {"name": "Appointment Service  :8083",  "description": "Schedule & track appointments — routed to **http://localhost:8083**"},
    {"name": "Pharmacy Service  :8084",     "description": "Medicine inventory management — routed to **http://localhost:8084**"},
    {"name": "Billing Service  :8085",      "description": "Patient invoices & payments — routed to **http://localhost:8085**"},
    {"name": "Notification Service  :8086", "description": "Email & SMS appointment alerts — routed to **http://localhost:8086**"},
    {"name": "Gateway",                     "description": "Gateway health & route info"},
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("\033[1m\033[97m" + "=" * 60 + "\033[0m")
    print("\033[1m  API GATEWAY\033[0m  ·  FastAPI + HTTPx Async Proxy")
    print("\033[1m\033[97m" + "=" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  Status   : \033[32mRUNNING\033[0m")
    print("  \033[32m✔\033[0m  Port     : \033[33m8080\033[0m")
    print("  \033[32m✔\033[0m  Docs     : \033[97mhttp://localhost:8080/docs\033[0m")
    print("\033[97m" + "-" * 60 + "\033[0m")
    print("  Route Table:")
    for prefix, target in ROUTES.items():
        print(f"    \033[33m:8080{prefix}/**\033[0m  →  \033[32m{target}\033[0m")
    print("\033[97m" + "-" * 60 + "\033[0m")
    print("  \033[32m✔\033[0m  CORS     : enabled (all origins)")
    print("  \033[32m✔\033[0m  Proxy    : HTTPx async client · 30s timeout")
    print("\033[1m\033[97m" + "=" * 60 + "\033[0m\n")
    yield
    print("\n\033[31m  API Gateway shutting down...\033[0m")


app = FastAPI(
    title="Hospital API Gateway",
    description=(
        "**Single entry point on port 8080.** All requests are forwarded to the "
        "correct microservice using HTTPx. The client only ever needs port **8080**.\n\n"
        "| Prefix | Service | Port |\n"
        "|--------|---------|------|\n"
        "| `/api/patients` | Patient Service | 8081 |\n"
        "| `/api/doctors` | Doctor Service | 8082 |\n"
        "| `/api/appointments` | Appointment Service | 8083 |\n"
        "| `/api/pharmacy` | Pharmacy Service | 8084 |\n"
        "| `/api/billing` | Billing Service | 8085 |\n"
        "| `/api/notifications` | Notification Service | 8086 |"
    ),
    version="1.0.0",
    openapi_tags=TAGS,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Gateway info ──────────────────────────────────────────────────────────────
@app.get("/", tags=["Gateway"], summary="Gateway health & route table")
def gateway_info():
    return {"service": "api-gateway", "status": "running", "port": 8080,
            "routes": ROUTES, "docs": "http://localhost:8080/docs"}


# ═════════════════════════════════════════════════════════════════════════════
# PATIENT SERVICE  ·  port 8081
# ═════════════════════════════════════════════════════════════════════════════
@app.get("/api/patients", tags=["Patient Service  :8081"], summary="Get all patients")
async def get_patients(request: Request):
    return await forward(request)

@app.get("/api/patients/{patient_id}", tags=["Patient Service  :8081"], summary="Get patient by ID")
async def get_patient(patient_id: int, request: Request):
    return await forward(request)

@app.post("/api/patients", tags=["Patient Service  :8081"], summary="Create a new patient", status_code=201)
async def create_patient(body: PatientBody, request: Request):
    return await forward(request, body)          # ← pass body so proxy re-serializes it

@app.put("/api/patients/{patient_id}", tags=["Patient Service  :8081"], summary="Update a patient")
async def update_patient(patient_id: int, body: PatientBody, request: Request):
    return await forward(request, body)

@app.delete("/api/patients/{patient_id}", tags=["Patient Service  :8081"], summary="Delete a patient", status_code=204)
async def delete_patient(patient_id: int, request: Request):
    return await forward(request)


# ═════════════════════════════════════════════════════════════════════════════
# DOCTOR SERVICE  ·  port 8082
# ═════════════════════════════════════════════════════════════════════════════
@app.get("/api/doctors", tags=["Doctor Service  :8082"], summary="Get all doctors")
async def get_doctors(request: Request):
    return await forward(request)

@app.get("/api/doctors/{doctor_id}", tags=["Doctor Service  :8082"], summary="Get doctor by ID")
async def get_doctor(doctor_id: int, request: Request):
    return await forward(request)

@app.post("/api/doctors", tags=["Doctor Service  :8082"], summary="Create a new doctor", status_code=201)
async def create_doctor(body: DoctorBody, request: Request):
    return await forward(request, body)

@app.put("/api/doctors/{doctor_id}", tags=["Doctor Service  :8082"], summary="Update a doctor")
async def update_doctor(doctor_id: int, body: DoctorBody, request: Request):
    return await forward(request, body)

@app.delete("/api/doctors/{doctor_id}", tags=["Doctor Service  :8082"], summary="Delete a doctor", status_code=204)
async def delete_doctor(doctor_id: int, request: Request):
    return await forward(request)


# ═════════════════════════════════════════════════════════════════════════════
# APPOINTMENT SERVICE  ·  port 8083
# ═════════════════════════════════════════════════════════════════════════════
@app.get("/api/appointments", tags=["Appointment Service  :8083"], summary="Get all appointments")
async def get_appointments(request: Request):
    return await forward(request)

@app.get("/api/appointments/patient/{patient_id}", tags=["Appointment Service  :8083"], summary="Get appointments by patient ID")
async def get_appointments_by_patient(patient_id: int, request: Request):
    return await forward(request)

@app.get("/api/appointments/doctor/{doctor_id}", tags=["Appointment Service  :8083"], summary="Get appointments by doctor ID")
async def get_appointments_by_doctor(doctor_id: int, request: Request):
    return await forward(request)

@app.get("/api/appointments/{appt_id}", tags=["Appointment Service  :8083"], summary="Get appointment by ID")
async def get_appointment(appt_id: int, request: Request):
    return await forward(request)

@app.post("/api/appointments", tags=["Appointment Service  :8083"], summary="Schedule a new appointment", status_code=201)
async def create_appointment(body: AppointmentBody, request: Request):
    return await forward(request, body)

@app.put("/api/appointments/{appt_id}", tags=["Appointment Service  :8083"], summary="Update an appointment")
async def update_appointment(appt_id: int, body: AppointmentBody, request: Request):
    return await forward(request, body)

@app.delete("/api/appointments/{appt_id}", tags=["Appointment Service  :8083"], summary="Cancel an appointment", status_code=204)
async def delete_appointment(appt_id: int, request: Request):
    return await forward(request)


# ═════════════════════════════════════════════════════════════════════════════
# PHARMACY SERVICE  ·  port 8084
# ═════════════════════════════════════════════════════════════════════════════
@app.get("/api/pharmacy", tags=["Pharmacy Service  :8084"], summary="Get all medicines")
async def get_medicines(request: Request):
    return await forward(request)

@app.get("/api/pharmacy/category/{category}", tags=["Pharmacy Service  :8084"], summary="Get medicines by category")
async def get_medicines_by_category(category: str, request: Request):
    return await forward(request)

@app.get("/api/pharmacy/{med_id}", tags=["Pharmacy Service  :8084"], summary="Get medicine by ID")
async def get_medicine(med_id: int, request: Request):
    return await forward(request)

@app.post("/api/pharmacy", tags=["Pharmacy Service  :8084"], summary="Add a new medicine", status_code=201)
async def create_medicine(body: MedicineBody, request: Request):
    return await forward(request, body)

@app.put("/api/pharmacy/{med_id}", tags=["Pharmacy Service  :8084"], summary="Update medicine details")
async def update_medicine(med_id: int, body: MedicineBody, request: Request):
    return await forward(request, body)

@app.delete("/api/pharmacy/{med_id}", tags=["Pharmacy Service  :8084"], summary="Remove a medicine", status_code=204)
async def delete_medicine(med_id: int, request: Request):
    return await forward(request)


# ═════════════════════════════════════════════════════════════════════════════
# BILLING SERVICE  ·  port 8085
# ═════════════════════════════════════════════════════════════════════════════
@app.get("/api/billing", tags=["Billing Service  :8085"], summary="Get all invoices")
async def get_invoices(request: Request):
    return await forward(request)

@app.get("/api/billing/patient/{patient_id}", tags=["Billing Service  :8085"], summary="Get invoices by patient ID")
async def get_invoices_by_patient(patient_id: int, request: Request):
    return await forward(request)

@app.get("/api/billing/status/{status}", tags=["Billing Service  :8085"], summary="Get invoices by status (PENDING / PAID / OVERDUE)")
async def get_invoices_by_status(status: str, request: Request):
    return await forward(request)

@app.get("/api/billing/{inv_id}", tags=["Billing Service  :8085"], summary="Get invoice by ID")
async def get_invoice(inv_id: int, request: Request):
    return await forward(request)

@app.post("/api/billing", tags=["Billing Service  :8085"], summary="Create a new invoice", status_code=201)
async def create_invoice(body: InvoiceBody, request: Request):
    return await forward(request, body)

@app.put("/api/billing/{inv_id}", tags=["Billing Service  :8085"], summary="Update invoice / mark as paid")
async def update_invoice(inv_id: int, body: InvoiceBody, request: Request):
    return await forward(request, body)

@app.delete("/api/billing/{inv_id}", tags=["Billing Service  :8085"], summary="Delete an invoice", status_code=204)
async def delete_invoice(inv_id: int, request: Request):
    return await forward(request)


# ═════════════════════════════════════════════════════════════════════════════
# NOTIFICATION SERVICE  ·  port 8086
# ═════════════════════════════════════════════════════════════════════════════
@app.get("/api/notifications", tags=["Notification Service  :8086"], summary="Get all notifications")
async def get_notifications(request: Request):
    return await forward(request)

@app.get("/api/notifications/patient/{patient_id}", tags=["Notification Service  :8086"], summary="Get notifications by patient ID")
async def get_notifications_by_patient(patient_id: int, request: Request):
    return await forward(request)

@app.get("/api/notifications/status/{status}", tags=["Notification Service  :8086"], summary="Get notifications by status (SENT / PENDING / FAILED)")
async def get_notifications_by_status(status: str, request: Request):
    return await forward(request)

@app.get("/api/notifications/{notif_id}", tags=["Notification Service  :8086"], summary="Get notification by ID")
async def get_notification(notif_id: int, request: Request):
    return await forward(request)

@app.post("/api/notifications/send/appointment",
          tags=["Notification Service  :8086"],
          summary="Send appointment confirmation (EMAIL or SMS)",
          status_code=201)
async def send_appointment_notification(body: NotificationBody, request: Request):
    return await forward(request, body)

@app.post("/api/notifications/send/cancellation",
          tags=["Notification Service  :8086"],
          summary="Send appointment cancellation notice",
          status_code=201)
async def send_cancellation_notification(body: NotificationBody, request: Request):
    return await forward(request, body)

@app.delete("/api/notifications/{notif_id}",
            tags=["Notification Service  :8086"],
            summary="Delete a notification record",
            status_code=204)
async def delete_notification(notif_id: int, request: Request):
    return await forward(request)
