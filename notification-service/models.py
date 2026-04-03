from pydantic import BaseModel


class NotificationRequest(BaseModel):
    patientId: int
    patientName: str
    contactInfo: str        # email address or phone number
    notificationType: str   # EMAIL or SMS
    appointmentDate: str
    appointmentTime: str
    doctorName: str
    reason: str


class Notification(BaseModel):
    id: int
    patientId: int
    patientName: str
    contactInfo: str
    notificationType: str
    subject: str
    message: str
    status: str             # SENT | PENDING | FAILED
    sentAt: str
    appointmentDate: str
    appointmentTime: str

    class Config:
        from_attributes = True
