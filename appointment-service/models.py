from pydantic import BaseModel


class AppointmentBase(BaseModel):
    patientId: int
    doctorId: int
    appointmentDate: str
    appointmentTime: str
    reason: str


class AppointmentCreate(AppointmentBase):
    pass


class Appointment(AppointmentBase):
    id: int
    status: str  # SCHEDULED | COMPLETED | CANCELLED

    class Config:
        from_attributes = True
