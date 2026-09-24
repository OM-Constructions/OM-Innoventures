import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, Any

from app.config import settings
from app.services.email_templates import (
    build_company_notification_html,
    build_client_confirmation_html,
    build_otp_verification_html,
)
from app.services.service_catalog import get_service

logger = logging.getLogger("email_service")


def send_html_email(to_email: str, subject: str, html_body: str) -> bool:
    """
    Sends an HTML email via SMTP (supporting both SSL port 465 and STARTTLS 587).
    Falls back to console preview safely if SMTP is unconfigured.
    """
    if not settings.SMTP_HOST or not settings.SMTP_USER or not settings.SMTP_PASSWORD:
        logger.info(
            f"[LOCAL DEV EMAIL] To: {to_email} | Subject: {subject}\n"
            f"(SMTP not configured. Email preview logged to console.)"
        )
        print(f"\n==================== EMAIL NOTIFICATION ====================")
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print(f"From: {settings.SMTP_FROM_NAME} <{settings.SMTP_USER or settings.COMPANY_NOTIFICATION_EMAIL}>")
        print(f"Body snippet:\n{html_body[:400]}...")
        print(f"===========================================================\n")
        return True

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"{settings.SMTP_FROM_NAME} <{settings.SMTP_USER}>"
        msg["To"] = to_email
        msg.attach(MIMEText(html_body, "html"))

        # Gmail SSL port 465 vs STARTTLS port 587
        if settings.SMTP_PORT == 465:
            with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT, timeout=12) as server:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.sendmail(settings.SMTP_USER, to_email, msg.as_string())
        else:
            with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=12) as server:
                server.ehlo()
                server.starttls()
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.sendmail(settings.SMTP_USER, to_email, msg.as_string())
            
        logger.info(f"Email successfully sent to {to_email}")
        return True
    except Exception as e:
        logger.error(f"Failed to dispatch email to {to_email}: {e}")
        print(f"[EMAIL SEND ERROR] {e}")
        return False


def send_otp_email(to_email: str, name: str, otp: str) -> bool:
    """
    Sends a branded 6-digit OTP verification email to the user.
    """
    subject = f"{otp} is your OM Innoventures verification code"
    html_body = build_otp_verification_html(name=name, otp=otp)
    return send_html_email(to_email=to_email, subject=subject, html_body=html_body)


def notify_new_enquiry(enquiry: Dict[str, Any]) -> Dict[str, bool]:
    """
    Sends company notification to COMPANY_NOTIFICATION_EMAIL
    and sends client confirmation to enquiry['email'].
    """
    service_slug = enquiry.get("service", "general-consultation")
    service_info = get_service(service_slug)
    service_name = service_info.get("name", "General Consultation")
    client_name = enquiry.get("name", "Client")
    client_email = enquiry.get("email")

    # 1. Company Notification (Always dispatch to ominnoventuresaitech@gmail.com)
    target_email = settings.COMPANY_NOTIFICATION_EMAIL
    if not target_email or "omengineeringconsultants" in target_email or "ominnoventures.ai@" in target_email:
        target_email = "ominnoventuresaitech@gmail.com"

    company_subject = f"New enquiry: {service_name} - {client_name}"
    company_html = build_company_notification_html(enquiry, service_info)
    company_sent = send_html_email(
        to_email=target_email,
        subject=company_subject,
        html_body=company_html,
    )

    # 2. Client Auto-confirmation
    client_sent = False
    if client_email:
        client_subject = f"Enquiry Received: {service_name} | OM Innoventures"
        client_html = build_client_confirmation_html(enquiry, service_info)
        client_sent = send_html_email(
            to_email=client_email,
            subject=client_subject,
            html_body=client_html,
        )

    return {"company_notified": company_sent, "client_confirmed": client_sent}
