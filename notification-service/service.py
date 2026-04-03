from models import NotificationRequest
import data_service


def get_all_notifications() -> list:
    return data_service.get_all()


def get_notification_by_id(notif_id: int) -> dict | None:
    return data_service.get_by_id(notif_id)


def get_by_patient(patient_id: int) -> list:
    return data_service.get_by_patient(patient_id)


def get_by_status(status: str) -> list:
    return data_service.get_by_status(status)


def send_appointment_notification(req: NotificationRequest) -> dict:
    ntype = req.notificationType.upper()
    if ntype == "EMAIL":
        subject = "Appointment Confirmation — City Hospital"
        message = (
            f"Dear {req.patientName},\n\n"
            f"Your appointment is confirmed.\n"
            f"  Date  : {req.appointmentDate}\n"
            f"  Time  : {req.appointmentTime}\n"
            f"  Doctor: Dr. {req.doctorName}\n"
            f"  Reason: {req.reason}\n\n"
            f"Please arrive 10 minutes early.\n\nRegards,\nCity Hospital"
        )
    else:
        subject = "SMS Alert"
        message = (
            f"CityHospital: Appt confirmed for {req.patientName} "
            f"on {req.appointmentDate} at {req.appointmentTime} "
            f"with Dr. {req.doctorName}."
        )
    return data_service.store(
        patient_id=req.patientId,
        patient_name=req.patientName,
        contact_info=req.contactInfo,
        notification_type=ntype,
        subject=subject,
        message=message,
        appointment_date=req.appointmentDate,
        appointment_time=req.appointmentTime,
    )


def send_cancellation_notification(req: NotificationRequest) -> dict:
    subject = "Appointment Cancellation Notice"
    message = (
        f"Dear {req.patientName}, your appointment on {req.appointmentDate} "
        f"at {req.appointmentTime} has been cancelled. "
        f"Please contact us to reschedule."
    )
    return data_service.store(
        patient_id=req.patientId,
        patient_name=req.patientName,
        contact_info=req.contactInfo,
        notification_type=req.notificationType.upper(),
        subject=subject,
        message=message,
        appointment_date=req.appointmentDate,
        appointment_time=req.appointmentTime,
    )


def delete_notification(notif_id: int) -> bool:
    return data_service.delete(notif_id)
