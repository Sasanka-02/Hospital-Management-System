from models import PatientCreate
import data_service


def get_all_patients() -> list:
    return data_service.get_all()


def get_patient_by_id(patient_id: int) -> dict | None:
    return data_service.get_by_id(patient_id)


def create_patient(patient: PatientCreate) -> dict:
    return data_service.insert(patient.model_dump())


def update_patient(patient_id: int, patient: PatientCreate) -> dict | None:
    return data_service.update(patient_id, patient.model_dump())


def delete_patient(patient_id: int) -> bool:
    return data_service.delete(patient_id)
