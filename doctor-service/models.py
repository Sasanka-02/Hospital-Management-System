from pydantic import BaseModel


class DoctorBase(BaseModel):
    firstName: str
    lastName: str
    specialization: str
    email: str
    phone: str
    licenseNumber: str
    availableDays: str


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: int

    class Config:
        from_attributes = True
