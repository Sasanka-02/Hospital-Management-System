"""
Gateway-side Pydantic models — mirror the exact same fields as each
microservice. json_schema_extra examples show real data values in
Swagger so the gateway UI looks identical to each individual service UI.
"""
from pydantic import BaseModel


# ── Patient ───────────────────────────────────────────────────────────────────
class PatientBody(BaseModel):
    firstName:   str
    lastName:    str
    email:       str
    phone:       str
    dateOfBirth: str
    address:     str
    bloodType:   str

    model_config = {
        "json_schema_extra": {
            "example": {
                "firstName":   "Kamal",
                "lastName":    "Bandara",
                "email":       "kamal@email.com",
                "phone":       "0774567890",
                "dateOfBirth": "1992-03-10",
                "address":     "Negombo",
                "bloodType":   "AB+"
            }
        }
    }


# ── Doctor ────────────────────────────────────────────────────────────────────
class DoctorBody(BaseModel):
    firstName:      str
    lastName:       str
    specialization: str
    email:          str
    phone:          str
    licenseNumber:  str
    availableDays:  str

    model_config = {
        "json_schema_extra": {
            "example": {
                "firstName":      "Sachini",
                "lastName":       "Peris",
                "specialization": "Dermatology",
                "email":          "sachini.p@hospital.lk",
                "phone":          "0112345681",
                "licenseNumber":  "LIC-004",
                "availableDays":  "Mon,Thu"
            }
        }
    }


# ── Appointment ───────────────────────────────────────────────────────────────
class AppointmentBody(BaseModel):
    patientId:       int
    doctorId:        int
    appointmentDate: str
    appointmentTime: str
    reason:          str

    model_config = {
        "json_schema_extra": {
            "example": {
                "patientId":       1,
                "doctorId":        2,
                "appointmentDate": "2026-04-15",
                "appointmentTime": "10:00",
                "reason":          "Routine check-up"
            }
        }
    }


# ── Medicine (Pharmacy) ───────────────────────────────────────────────────────
class MedicineBody(BaseModel):
    name:          str
    genericName:   str
    category:      str
    manufacturer:  str
    unitPrice:     float
    stockQuantity: int
    expiryDate:    str

    model_config = {
        "json_schema_extra": {
            "example": {
                "name":          "Atorvastatin 10mg",
                "genericName":   "Atorvastatin",
                "category":      "Statin",
                "manufacturer":  "Pfizer",
                "unitPrice":     3.75,
                "stockQuantity": 150,
                "expiryDate":    "2028-01-31"
            }
        }
    }


# ── Invoice (Billing) ─────────────────────────────────────────────────────────
class InvoiceBody(BaseModel):
    patientId:       int
    appointmentId:   int
    invoiceDate:     str
    consultationFee: float
    medicineFee:     float
    labFee:          float
    paymentMethod:   str

    model_config = {
        "json_schema_extra": {
            "example": {
                "patientId":       1,
                "appointmentId":   1,
                "invoiceDate":     "2026-04-15",
                "consultationFee": 2500.00,
                "medicineFee":     750.00,
                "labFee":          500.00,
                "paymentMethod":   "CARD"
            }
        }
    }


# ── Notification ──────────────────────────────────────────────────────────────
class NotificationBody(BaseModel):
    patientId:        int
    patientName:      str
    contactInfo:      str
    notificationType: str
    appointmentDate:  str
    appointmentTime:  str
    doctorName:       str
    reason:           str

    model_config = {
        "json_schema_extra": {
            "example": {
                "patientId":        1,
                "patientName":      "Ashan Perera",
                "contactInfo":      "ashan@email.com",
                "notificationType": "EMAIL",
                "appointmentDate":  "2026-04-15",
                "appointmentTime":  "10:00",
                "doctorName":       "Priya Rathnayake",
                "reason":           "Routine check-up"
            }
        }
    }
