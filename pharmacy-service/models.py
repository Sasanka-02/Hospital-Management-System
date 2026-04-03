from pydantic import BaseModel


class MedicineBase(BaseModel):
    name: str
    genericName: str
    category: str
    manufacturer: str
    unitPrice: float
    stockQuantity: int
    expiryDate: str


class MedicineCreate(MedicineBase):
    pass


class Medicine(MedicineBase):
    id: int

    class Config:
        from_attributes = True
