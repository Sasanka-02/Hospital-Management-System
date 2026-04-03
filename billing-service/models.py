from pydantic import BaseModel


class InvoiceBase(BaseModel):
    patientId: int
    appointmentId: int
    invoiceDate: str
    consultationFee: float
    medicineFee: float
    labFee: float
    paymentMethod: str  # CASH | CARD | INSURANCE


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase):
    id: int
    totalAmount: float
    paymentStatus: str  # PENDING | PAID | OVERDUE

    class Config:
        from_attributes = True
