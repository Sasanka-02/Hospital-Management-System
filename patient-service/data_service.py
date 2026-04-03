from models import Patient

# In-memory data store
patients: dict = {}
_next_id: int = 1


def seed_data():
    global _next_id
    seed_records = [
        {"firstName": "Ashan",  "lastName": "Perera",   "email": "ashan@email.com",
         "phone": "0771234567", "dateOfBirth": "1990-05-15", "address": "Colombo 03", "bloodType": "O+"},
        {"firstName": "Nimali", "lastName": "Silva",    "email": "nimali@email.com",
         "phone": "0772345678", "dateOfBirth": "1985-08-22", "address": "Kandy",      "bloodType": "A+"},
        {"firstName": "Ruwan",  "lastName": "Fernando", "email": "ruwan@email.com",
         "phone": "0773456789", "dateOfBirth": "1995-12-10", "address": "Galle",      "bloodType": "B-"},
    ]
    for record in seed_records:
        patients[_next_id] = {"id": _next_id, **record}
        _next_id += 1


def get_all() -> list:
    return list(patients.values())


def get_by_id(patient_id: int) -> dict | None:
    return patients.get(patient_id)


def insert(data: dict) -> dict:
    global _next_id
    new_record = {"id": _next_id, **data}
    patients[_next_id] = new_record
    _next_id += 1
    return new_record


def update(patient_id: int, data: dict) -> dict | None:
    if patient_id not in patients:
        return None
    patients[patient_id] = {"id": patient_id, **data}
    return patients[patient_id]


def delete(patient_id: int) -> bool:
    if patient_id not in patients:
        return False
    del patients[patient_id]
    return True
