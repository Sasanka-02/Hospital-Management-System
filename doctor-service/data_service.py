doctors: dict = {}
_next_id: int = 1


def seed_data():
    global _next_id
    seed_records = [
        {"firstName": "Kasun",  "lastName": "Jayawardena",    "specialization": "Cardiology",
         "email": "kasun.j@hospital.lk",  "phone": "0112345678", "licenseNumber": "LIC-001", "availableDays": "Mon,Tue,Wed"},
        {"firstName": "Priya",  "lastName": "Rathnayake",     "specialization": "Neurology",
         "email": "priya.r@hospital.lk",  "phone": "0112345679", "licenseNumber": "LIC-002", "availableDays": "Thu,Fri"},
        {"firstName": "Dinesh", "lastName": "Wickramasinghe", "specialization": "Pediatrics",
         "email": "dinesh.w@hospital.lk", "phone": "0112345680", "licenseNumber": "LIC-003", "availableDays": "Mon,Wed,Fri"},
    ]
    for record in seed_records:
        doctors[_next_id] = {"id": _next_id, **record}
        _next_id += 1


def get_all() -> list:
    return list(doctors.values())


def get_by_id(doctor_id: int) -> dict | None:
    return doctors.get(doctor_id)


def insert(data: dict) -> dict:
    global _next_id
    new_record = {"id": _next_id, **data}
    doctors[_next_id] = new_record
    _next_id += 1
    return new_record


def update(doctor_id: int, data: dict) -> dict | None:
    if doctor_id not in doctors:
        return None
    doctors[doctor_id] = {"id": doctor_id, **data}
    return doctors[doctor_id]


def delete(doctor_id: int) -> bool:
    if doctor_id not in doctors:
        return False
    del doctors[doctor_id]
    return True
