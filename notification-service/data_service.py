from datetime import datetime

notifications: dict = {}
_next_id: int = 1


def seed_data():
    """Load one sample notification on startup."""
    store(
        patient_id=1,
        patient_name="Ashan Perera",
        contact_info="ashan@email.com",
        notification_type="EMAIL",
        subject="Appointment Confirmation — City Hospital",
        message=(
            "Dear Ashan Perera,\n\n"
            "Your appointment is confirmed.\n"
            "  Date  : 2026-04-01\n"
            "  Time  : 09:00\n"
            "  Doctor: Dr. Kasun Jayawardena\n"
            "  Reason: Chest pain follow-up\n\n"
            "Please arrive 10 minutes early.\n\nRegards,\nCity Hospital"
        ),
        appointment_date="2026-04-01",
        appointment_time="09:00",
    )


def store(patient_id, patient_name, contact_info, notification_type,
          subject, message, appointment_date, appointment_time) -> dict:
    global _next_id
    record = {
        "id":               _next_id,
        "patientId":        patient_id,
        "patientName":      patient_name,
        "contactInfo":      contact_info,
        "notificationType": notification_type.upper(),
        "subject":          subject,
        "message":          message,
        "status":           "SENT",
        "sentAt":           datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "appointmentDate":  appointment_date,
        "appointmentTime":  appointment_time,
    }
    notifications[_next_id] = record
    _next_id += 1
    return record


def get_all() -> list:
    return list(notifications.values())


def get_by_id(notif_id: int) -> dict | None:
    return notifications.get(notif_id)


def get_by_patient(patient_id: int) -> list:
    return [n for n in notifications.values() if n["patientId"] == patient_id]


def get_by_status(status: str) -> list:
    return [n for n in notifications.values() if n["status"].upper() == status.upper()]


def delete(notif_id: int) -> bool:
    if notif_id not in notifications:
        return False
    del notifications[notif_id]
    return True
