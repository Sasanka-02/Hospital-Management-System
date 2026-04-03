medicines: dict = {}
_next_id: int = 1


def seed_data():
    global _next_id
    seed_records = [
        {"name": "Paracetamol 500mg", "genericName": "Acetaminophen", "category": "Analgesic",
         "manufacturer": "CML Pharma",  "unitPrice": 0.50, "stockQuantity": 500, "expiryDate": "2027-12-31"},
        {"name": "Amoxicillin 250mg", "genericName": "Amoxicillin",   "category": "Antibiotic",
         "manufacturer": "Hemas Pharma","unitPrice": 2.50, "stockQuantity": 200, "expiryDate": "2027-06-30"},
        {"name": "Metformin 500mg",   "genericName": "Metformin HCl", "category": "Antidiabetic",
         "manufacturer": "Bristol",     "unitPrice": 1.20, "stockQuantity": 350, "expiryDate": "2026-09-30"},
    ]
    for record in seed_records:
        medicines[_next_id] = {"id": _next_id, **record}
        _next_id += 1


def get_all() -> list:
    return list(medicines.values())


def get_by_id(med_id: int) -> dict | None:
    return medicines.get(med_id)


def get_by_category(category: str) -> list:
    return [m for m in medicines.values() if m["category"].lower() == category.lower()]


def insert(data: dict) -> dict:
    global _next_id
    new_record = {"id": _next_id, **data}
    medicines[_next_id] = new_record
    _next_id += 1
    return new_record


def update(med_id: int, data: dict) -> dict | None:
    if med_id not in medicines:
        return None
    medicines[med_id] = {"id": med_id, **data}
    return medicines[med_id]


def delete(med_id: int) -> bool:
    if med_id not in medicines:
        return False
    del medicines[med_id]
    return True
git commit -m "your update"