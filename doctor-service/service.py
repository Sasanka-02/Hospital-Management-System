from models import DoctorCreate
import data_service


def get_all_doctors() -> list:
    return data_service.get_all()


def get_doctor_by_id(doctor_id: int) -> dict | None:
    return data_service.get_by_id(doctor_id)


def create_doctor(doctor: DoctorCreate) -> dict:
    return data_service.insert(doctor.model_dump())


def update_doctor(doctor_id: int, doctor: DoctorCreate) -> dict | None:
    return data_service.update(doctor_id, doctor.model_dump())


def delete_doctor(doctor_id: int) -> bool:
    return data_service.delete(doctor_id)
