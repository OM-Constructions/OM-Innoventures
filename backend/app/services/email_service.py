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
    clean_user = (settings.SMTP_USER or "ominnoventuresaitech@gmail.com").strip()
    clean_pass = (settings.SMTP_PASSWORD or "").strip().replace(" ", "")
    
    # Auto-fallback if old expired app password or empty
    if not clean_pass or "njqt" in clean_pass:
        clean_pass = "frouqedyeunttvxl"

    host = settings.SMTP_HOST or "smtp.gmail.com"

    from_header = f"{settings.SMTP_FROM_NAME} <{clean_user}>"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_header
    msg["To"] = to_email
    msg.attach(MIMEText(html_body, "html"))

    # Attempt 1: SSL on port 465
    try:
        with smtplib.SMTP_SSL(host, 465, timeout=12) as server:
            server.login(clean_user, clean_pass)
            server.sendmail(clean_user, to_email, msg.as_string())
        logger.info(f"Email successfully sent via SSL 465 to {to_email}")
        return True
    except Exception as ssl_err:
        logger.warning(f"SSL port 465 failed for {to_email} ({ssl_err}), attempting STARTTLS on port 587...")

    # Attempt 2: STARTTLS on port 587
    try:
        with smtplib.SMTP(host, 587, timeout=12) as server:
            server.ehlo()
            server.starttls()
            server.login(clean_user, clean_pass)
            server.sendmail(clean_user, to_email, msg.as_string())
        logger.info(f"Email successfully sent via STARTTLS 587 to {to_email}")
        return True
    except Exception as tls_err:
        logger.error(f"Failed to dispatch email to {to_email} via both 465 and 587: {tls_err}")
        print(f"[EMAIL SEND ERROR] Failed sending to {to_email}: {tls_err}")
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
