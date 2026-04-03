from models import AppointmentCreate
import data_service


def get_all_appointments() -> list:
    return data_service.get_all()


def get_appointment_by_id(appt_id: int) -> dict | None:
    return data_service.get_by_id(appt_id)


def get_by_patient(patient_id: int) -> list:
    return data_service.get_by_patient(patient_id)


def get_by_doctor(doctor_id: int) -> list:
    return data_service.get_by_doctor(doctor_id)


def create_appointment(appt: AppointmentCreate) -> dict:
    return data_service.insert(appt.model_dump())


def update_appointment(appt_id: int, appt: AppointmentCreate, status: str) -> dict | None:
    return data_service.update(appt_id, appt.model_dump(), status)


def delete_appointment(appt_id: int) -> bool:
    return data_service.delete(appt_id)
