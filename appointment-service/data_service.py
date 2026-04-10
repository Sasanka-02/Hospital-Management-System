appointments: dict = {}
_next_id: int = 1


def seed_data():
    global _next_id
    seed_records = [
        {"patientId": 1, "doctorId": 1, "appointmentDate": "2026-04-01",
         "appointmentTime": "09:00", "reason": "Chest pain follow-up", "status": "SCHEDULED"},
        {"patientId": 2, "doctorId": 2, "appointmentDate": "2026-04-02",
         "appointmentTime": "10:30", "reason": "Headache evaluation",  "status": "SCHEDULED"},
        {"patientId": 3, "doctorId": 3, "appointmentDate": "2026-04-03",
         "appointmentTime": "14:00", "reason": "Child vaccination",    "status": "COMPLETED"},
    ]
    for record in seed_records:
        appointments[_next_id] = {"id": _next_id, **record}
        _next_id += 1


def get_all() -> list:
    return list(appointments.values())


def get_by_id(appt_id: int) -> dict | None:
    return appointments.get(appt_id)


def get_by_patient(patient_id: int) -> list:
    return [a for a in appointments.values() if a["patientId"] == patient_id]


def get_by_doctor(doctor_id: int) -> list:
    return [a for a in appointments.values() if a["doctorId"] == doctor_id]


def insert(data: dict) -> dict | None:
    global _next_id
    # Check for existing duplicate records
    for appt in appointments.values():
        if (appt["patientId"] == data["patientId"] and 
            appt["doctorId"] == data["doctorId"] and 
            appt["appointmentDate"] == data["appointmentDate"] and 
            appt["appointmentTime"] == data["appointmentTime"]):
            return None # Indicate a conflict found
            
    new_record = {"id": _next_id, **data, "status": "SCHEDULED"}
    appointments[_next_id] = new_record
    _next_id += 1
    return new_record


def update(appt_id: int, data: dict, status: str) -> dict | None:
    if appt_id not in appointments:
        return None
    appointments[appt_id] = {"id": appt_id, **data, "status": status}
    return appointments[appt_id]


def delete(appt_id: int) -> bool:
    if appt_id not in appointments:
        return False
    del appointments[appt_id]
    return True
