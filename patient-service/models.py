from pydantic import BaseModel


class PatientBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str
    dateOfBirth: str
    address: str
    bloodType: str


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True
