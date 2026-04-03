invoices: dict = {}
_next_id: int = 1


def seed_data():
    global _next_id
    seed_records = [
        {"patientId": 1, "appointmentId": 1, "invoiceDate": "2026-04-01",
         "consultationFee": 2500.0, "medicineFee": 500.0,  "labFee": 1000.0,
         "paymentMethod": "CARD",      "totalAmount": 4000.0, "paymentStatus": "PAID"},
        {"patientId": 2, "appointmentId": 2, "invoiceDate": "2026-04-02",
         "consultationFee": 3000.0, "medicineFee": 750.0,  "labFee": 0.0,
         "paymentMethod": "CASH",      "totalAmount": 3750.0, "paymentStatus": "PENDING"},
        {"patientId": 3, "appointmentId": 3, "invoiceDate": "2026-04-03",
         "consultationFee": 1500.0, "medicineFee": 300.0,  "labFee": 200.0,
         "paymentMethod": "INSURANCE", "totalAmount": 2000.0, "paymentStatus": "PENDING"},
    ]
    for record in seed_records:
        invoices[_next_id] = {"id": _next_id, **record}
        _next_id += 1


def get_all() -> list:
    return list(invoices.values())


def get_by_id(inv_id: int) -> dict | None:
    return invoices.get(inv_id)


def get_by_patient(patient_id: int) -> list:
    return [i for i in invoices.values() if i["patientId"] == patient_id]


def get_by_status(status: str) -> list:
    return [i for i in invoices.values() if i["paymentStatus"].upper() == status.upper()]


def insert(data: dict) -> dict:
    global _next_id
    total = data["consultationFee"] + data["medicineFee"] + data["labFee"]
    new_record = {"id": _next_id, **data, "totalAmount": total, "paymentStatus": "PENDING"}
    invoices[_next_id] = new_record
    _next_id += 1
    return new_record


def update(inv_id: int, data: dict, payment_status: str) -> dict | None:
    if inv_id not in invoices:
        return None
    total = data["consultationFee"] + data["medicineFee"] + data["labFee"]
    invoices[inv_id] = {"id": inv_id, **data, "totalAmount": total, "paymentStatus": payment_status}
    return invoices[inv_id]


def delete(inv_id: int) -> bool:
    if inv_id not in invoices:
        return False
    del invoices[inv_id]
    return True
