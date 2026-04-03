ROUTES: dict[str, str] = {
    "/api/patients":      "http://localhost:8081",
    "/api/doctors":       "http://localhost:8082",
    "/api/appointments":  "http://localhost:8083",
    "/api/pharmacy":      "http://localhost:8084",
    "/api/billing":       "http://localhost:8085",
    "/api/notifications": "http://localhost:8086",
}

SERVICE_ENDPOINTS = [
    # Patient
    {"tag":"Patient Service  :8081","method":"GET",   "path":"/api/patients",             "summary":"Get all patients"},
    {"tag":"Patient Service  :8081","method":"GET",   "path":"/api/patients/{patient_id}", "summary":"Get patient by ID"},
    {"tag":"Patient Service  :8081","method":"POST",  "path":"/api/patients",             "summary":"Create a new patient",
     "body":{"firstName":"Kamal","lastName":"Bandara","email":"kamal@email.com","phone":"0774567890","dateOfBirth":"1992-03-10","address":"Negombo","bloodType":"AB+"}},
    {"tag":"Patient Service  :8081","method":"PUT",   "path":"/api/patients/{patient_id}", "summary":"Update a patient"},
    {"tag":"Patient Service  :8081","method":"DELETE","path":"/api/patients/{patient_id}", "summary":"Delete a patient"},
    # Doctor
    {"tag":"Doctor Service  :8082","method":"GET",   "path":"/api/doctors",             "summary":"Get all doctors"},
    {"tag":"Doctor Service  :8082","method":"GET",   "path":"/api/doctors/{doctor_id}", "summary":"Get doctor by ID"},
    {"tag":"Doctor Service  :8082","method":"POST",  "path":"/api/doctors",             "summary":"Create a new doctor",
     "body":{"firstName":"Sachini","lastName":"Peris","specialization":"Dermatology","email":"sachini.p@hospital.lk","phone":"0112345681","licenseNumber":"LIC-004","availableDays":"Mon,Thu"}},
    {"tag":"Doctor Service  :8082","method":"PUT",   "path":"/api/doctors/{doctor_id}", "summary":"Update a doctor"},
    {"tag":"Doctor Service  :8082","method":"DELETE","path":"/api/doctors/{doctor_id}", "summary":"Delete a doctor"},
    # Appointment
    {"tag":"Appointment Service  :8083","method":"GET",   "path":"/api/appointments",                        "summary":"Get all appointments"},
    {"tag":"Appointment Service  :8083","method":"GET",   "path":"/api/appointments/{appt_id}",              "summary":"Get appointment by ID"},
    {"tag":"Appointment Service  :8083","method":"GET",   "path":"/api/appointments/patient/{patient_id}",   "summary":"Get appointments by patient"},
    {"tag":"Appointment Service  :8083","method":"GET",   "path":"/api/appointments/doctor/{doctor_id}",     "summary":"Get appointments by doctor"},
    {"tag":"Appointment Service  :8083","method":"POST",  "path":"/api/appointments",                        "summary":"Schedule a new appointment",
     "body":{"patientId":1,"doctorId":2,"appointmentDate":"2026-04-15","appointmentTime":"10:00","reason":"Routine check-up"}},
    {"tag":"Appointment Service  :8083","method":"PUT",   "path":"/api/appointments/{appt_id}",              "summary":"Update an appointment"},
    {"tag":"Appointment Service  :8083","method":"DELETE","path":"/api/appointments/{appt_id}",              "summary":"Cancel an appointment"},
    # Pharmacy
    {"tag":"Pharmacy Service  :8084","method":"GET",   "path":"/api/pharmacy",                    "summary":"Get all medicines"},
    {"tag":"Pharmacy Service  :8084","method":"GET",   "path":"/api/pharmacy/{med_id}",           "summary":"Get medicine by ID"},
    {"tag":"Pharmacy Service  :8084","method":"GET",   "path":"/api/pharmacy/category/{category}","summary":"Get medicines by category"},
    {"tag":"Pharmacy Service  :8084","method":"POST",  "path":"/api/pharmacy",                    "summary":"Add a new medicine",
     "body":{"name":"Atorvastatin 10mg","genericName":"Atorvastatin","category":"Statin","manufacturer":"Pfizer","unitPrice":3.75,"stockQuantity":150,"expiryDate":"2028-01-31"}},
    {"tag":"Pharmacy Service  :8084","method":"PUT",   "path":"/api/pharmacy/{med_id}",           "summary":"Update medicine details"},
    {"tag":"Pharmacy Service  :8084","method":"DELETE","path":"/api/pharmacy/{med_id}",           "summary":"Remove a medicine"},
    # Billing
    {"tag":"Billing Service  :8085","method":"GET",   "path":"/api/billing",                    "summary":"Get all invoices"},
    {"tag":"Billing Service  :8085","method":"GET",   "path":"/api/billing/{inv_id}",           "summary":"Get invoice by ID"},
    {"tag":"Billing Service  :8085","method":"GET",   "path":"/api/billing/patient/{patient_id}","summary":"Get invoices by patient"},
    {"tag":"Billing Service  :8085","method":"GET",   "path":"/api/billing/status/{status}",    "summary":"Get invoices by status (PENDING/PAID/OVERDUE)"},
    {"tag":"Billing Service  :8085","method":"POST",  "path":"/api/billing",                    "summary":"Create a new invoice",
     "body":{"patientId":1,"appointmentId":1,"invoiceDate":"2026-04-15","consultationFee":2500.00,"medicineFee":750.00,"labFee":500.00,"paymentMethod":"CARD"}},
    {"tag":"Billing Service  :8085","method":"PUT",   "path":"/api/billing/{inv_id}",           "summary":"Update invoice / mark as paid"},
    {"tag":"Billing Service  :8085","method":"DELETE","path":"/api/billing/{inv_id}",           "summary":"Delete an invoice"},
    # Notification
    {"tag":"Notification Service  :8086","method":"GET",   "path":"/api/notifications",                        "summary":"Get all notifications"},
    {"tag":"Notification Service  :8086","method":"GET",   "path":"/api/notifications/{notif_id}",             "summary":"Get notification by ID"},
    {"tag":"Notification Service  :8086","method":"GET",   "path":"/api/notifications/patient/{patient_id}",   "summary":"Get notifications by patient"},
    {"tag":"Notification Service  :8086","method":"GET",   "path":"/api/notifications/status/{status}",        "summary":"Get notifications by status (SENT/PENDING/FAILED)"},
    {"tag":"Notification Service  :8086","method":"POST",  "path":"/api/notifications/send/appointment",       "summary":"Send appointment confirmation (EMAIL or SMS)",
     "body":{"patientId":1,"patientName":"Ashan Perera","contactInfo":"ashan@email.com","notificationType":"EMAIL","appointmentDate":"2026-04-15","appointmentTime":"10:00","doctorName":"Priya Rathnayake","reason":"Routine check-up"}},
    {"tag":"Notification Service  :8086","method":"POST",  "path":"/api/notifications/send/cancellation",      "summary":"Send appointment cancellation notice",
     "body":{"patientId":1,"patientName":"Ashan Perera","contactInfo":"0772345678","notificationType":"SMS","appointmentDate":"2026-04-15","appointmentTime":"10:00","doctorName":"Priya Rathnayake","reason":"Cancelled by patient"}},
    {"tag":"Notification Service  :8086","method":"DELETE","path":"/api/notifications/{notif_id}",             "summary":"Delete a notification record"},
]


def resolve(path: str) -> str | None:
    for prefix, target in ROUTES.items():
        if path.startswith(prefix):
            return target
    return None
