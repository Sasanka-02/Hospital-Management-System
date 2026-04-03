from models import InvoiceCreate
import data_service


def get_all_invoices() -> list:
    return data_service.get_all()


def get_invoice_by_id(inv_id: int) -> dict | None:
    return data_service.get_by_id(inv_id)


def get_by_patient(patient_id: int) -> list:
    return data_service.get_by_patient(patient_id)


def get_by_status(status: str) -> list:
    return data_service.get_by_status(status)


def create_invoice(invoice: InvoiceCreate) -> dict:
    return data_service.insert(invoice.model_dump())


def update_invoice(inv_id: int, invoice: InvoiceCreate, payment_status: str) -> dict | None:
    return data_service.update(inv_id, invoice.model_dump(), payment_status)


def delete_invoice(inv_id: int) -> bool:
    return data_service.delete(inv_id)
