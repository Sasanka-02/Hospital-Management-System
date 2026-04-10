from pydantic import BaseModel

# Keep this for your POST requests (which don't have an ID yet)
class AppointmentCreate(BaseModel):
    patientId: int
    doctorId: int
    appointmentDate: str
    appointmentTime: str
    reason: str

# Define the full Appointment model without inheritance to control order
class Appointment(BaseModel):
    id: int  
    patientId: int
    doctorId: int
    appointmentDate: str
    appointmentTime: str
    reason: str
    status: str  # SCHEDULED | COMPLETED | CANCELLED

    class Config:
        from_attributes = True