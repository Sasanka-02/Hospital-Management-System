from models import MedicineCreate
import data_service


def get_all_medicines() -> list:
    return data_service.get_all()


def get_medicine_by_id(med_id: int) -> dict | None:
    return data_service.get_by_id(med_id)


def get_by_category(category: str) -> list:
    return data_service.get_by_category(category)


def create_medicine(medicine: MedicineCreate) -> dict:
    return data_service.insert(medicine.model_dump())


def update_medicine(med_id: int, medicine: MedicineCreate) -> dict | None:
    return data_service.update(med_id, medicine.model_dump())


def delete_medicine(med_id: int) -> bool:
    return data_service.delete(med_id)
