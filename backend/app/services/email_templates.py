import html
from typing import Dict, Any


def render_email(title: str, content_html: str) -> str:
    """
    Renders the branded HTML email wrapper for OM Innoventures & Build AI Technologies.
    Uses navy #0A1F3D, cyan #4FC3F7, clean white cards, and modern typography.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <style>
    body {{
      margin: 0;
      padding: 0;
      background-color: #050d1a;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      -webkit-font-smoothing: antialiased;
    }}
    .email-container {{
      max-width: 620px;
      margin: 30px auto;
      background: #ffffff;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 10px 25px rgba(10, 31, 61, 0.25);
      border: 1px solid #16325c;
    }}
    .header-bar {{
      background: #0A1F3D;
      padding: 26px 32px;
      border-bottom: 3px solid #4FC3F7;
      text-align: left;
    }}
    .brand-title {{
      margin: 0;
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.5px;
      color: #ffffff;
      line-height: 1.2;
    }}
    .brand-accent {{
      color: #4FC3F7;
    }}
    .brand-sub {{
      margin-top: 4px;
      font-size: 11px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #94a3b8;
      font-weight: 600;
    }}
    .content-body {{
      padding: 32px;
      color: #334155;
      font-size: 15px;
      line-height: 1.65;
    }}
    .heading-underline {{
      position: relative;
      padding-bottom: 8px;
      margin-top: 0;
      color: #0A1F3D;
      font-size: 20px;
      font-weight: 700;
    }}
    .heading-underline::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 44px;
      height: 3px;
      background-color: #4FC3F7;
      border-radius: 2px;
    }}
    .table-details {{
      width: 100%;
      border-collapse: collapse;
      margin: 22px 0;
      background: #f8fafc;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #e2e8f0;
    }}
    .table-details th {{
      width: 32%;
      padding: 12px 16px;
      text-align: left;
      font-size: 13px;
      color: #64748b;
      font-weight: 600;
      border-bottom: 1px solid #e2e8f0;
      background: #f1f5f9;
    }}
    .table-details td {{
      padding: 12px 16px;
      font-size: 14px;
      color: #0A1F3D;
      font-weight: 500;
      border-bottom: 1px solid #e2e8f0;
    }}
    .table-details tr:last-child th,
    .table-details tr:last-child td {{
      border-bottom: none;
    }}
    .highlight-card {{
      background: #ecfeff;
      border-left: 4px solid #4FC3F7;
      padding: 16px 18px;
      border-radius: 0 8px 8px 0;
      margin: 22px 0;
      color: #0e7490;
      font-size: 14px;
    }}
    .otp-card {{
      background: #f8fafc;
      border: 2px dashed #4FC3F7;
      border-radius: 10px;
      padding: 24px;
      text-align: center;
      margin: 24px 0;
    }}
    .otp-code {{
      font-size: 34px;
      font-weight: 800;
      letter-spacing: 8px;
      color: #0A1F3D;
      font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
      margin: 12px 0 6px;
    }}
    .btn {{
      display: inline-block;
      background: #0A1F3D;
      color: #ffffff !important;
      text-decoration: none;
      padding: 12px 24px;
      font-weight: 600;
      border-radius: 6px;
      border: 1px solid #4FC3F7;
      margin-top: 16px;
    }}
    .footer-bar {{
      background: #06152b;
      padding: 22px 32px;
      border-top: 1px solid #16325c;
      text-align: center;
      color: #94a3b8;
      font-size: 12px;
      line-height: 1.6;
    }}
    .footer-brand {{
      color: #ffffff;
      font-weight: 600;
      margin-bottom: 4px;
    }}
    .footer-divider {{
      color: #C9A34E;
      margin: 0 8px;
    }}
    a {{
      color: #1666A8;
      text-decoration: none;
    }}
    a:hover {{
      color: #4FC3F7;
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <div class="email-container">
    <div class="header-bar">
      <div class="brand-title">
        <span class="brand-accent">OM Innoventures</span> & Build AI Technologies
      </div>
      <div class="brand-sub">Intelligent Solutions for a Smarter Future</div>
    </div>
    
    <div class="content-body">
      {content_html}
    </div>
    
    <div class="footer-bar">
      <div class="footer-brand">OM INNOVENTURES & BUILD AI TECHNOLOGIES</div>
      <div>Basaveshwaranagar, Bengaluru – 560079 <span class="footer-divider">◆</span> Phone: +91 83101 60257</div>
      <div style="margin-top: 6px; color: #64748b; font-size: 11px;">
        Sister enterprise to OM Innoventures & Build AI technologies
      </div>
    </div>
  </div>
</body>
</html>"""


def build_otp_verification_html(name: str, otp: str) -> str:
    """Builds a secure branded email template for OTP email verification."""
    client_name = html.escape(name or "Valued Client")
    otp_escaped = html.escape(str(otp))
    
    content = f"""
      <h2 class="heading-underline">Verify Your Email Address</h2>
      <p>Hello <strong>{client_name}</strong>,</p>
      <p>Thank you for registering with <strong>OM Innoventures & Build AI Technologies</strong>. To complete your account registration and access your client portal, please use the 6-digit verification code below:</p>
      
      <div class="otp-card">
        <div style="font-size: 13px; font-weight: 600; text-transform: uppercase; color: #64748b; letter-spacing: 1px;">Your Verification Code</div>
        <div class="otp-code">{otp_escaped}</div>
        <div style="font-size: 12px; color: #94a3b8; margin-top: 4px;">Expires in 10 minutes</div>
      </div>
      
      <div class="highlight-card">
        <strong>Security Notice:</strong> Never share this code with anyone. OM Innoventures engineers will never ask for your verification code.
      </div>
      
      <p style="font-size: 14px; color: #64748b; margin-top: 20px;">
        If you did not initiate this request, you can safely disregard this email.
      </p>
      
      <p style="margin-top: 24px; color: #0A1F3D; font-weight: 600;">
        Warm regards,<br>
        <span style="color: #1666A8;">The Engineering & Identity Team</span><br>
        OM Innoventures & Build AI Technologies
      </p>
    """
    return render_email("Your OM Innoventures Verification Code", content)


def build_company_notification_html(enquiry: Dict[str, Any], service_info: Dict[str, Any]) -> str:
    service_name = service_info.get("name", enquiry.get("service", "General Consultation"))
    client_name = html.escape(enquiry.get("name", "Prospective Client"))
    email = html.escape(enquiry.get("email", "Not provided"))
    phone = html.escape(enquiry.get("phone", "Not provided")) or "Not provided"
    message = html.escape(enquiry.get("message", "")).replace("\n", "<br>")
    client_ip = html.escape(enquiry.get("client_ip", "Unknown"))
    
    content = f"""
      <h2 class="heading-underline">New Project Enquiry Received</h2>
      <p>A client has submitted <strong>{html.escape(service_info.get('company_intro', 'a new project enquiry'))}</strong> via the OM Innoventures platform.</p>
      
      <table class="table-details">
        <tr>
          <th>Client Name</th>
          <td>{client_name}</td>
        </tr>
        <tr>
          <th>Email Address</th>
          <td><a href="mailto:{email}">{email}</a></td>
        </tr>
        <tr>
          <th>Phone / WhatsApp</th>
          <td>{phone}</td>
        </tr>
        <tr>
          <th>Service Requested</th>
          <td><span style="color: #1666A8; font-weight: 700;">{html.escape(service_name)}</span></td>
        </tr>
        <tr>
          <th>Project Scope</th>
          <td>{message}</td>
        </tr>
        <tr>
          <th>Client IP Address</th>
          <td><code style="background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-size: 12px;">{client_ip}</code></td>
        </tr>
      </table>
      
      <div class="highlight-card">
        <strong>Action Required:</strong> Please review this requirement and respond to the client within the 24-hour SLA.
      </div>
      
      <a href="mailto:{email}?subject=Regarding%20your%20{html.escape(service_name)}%20enquiry%20-%20OM%20Innoventures" class="btn">
        Reply to {client_name} &rarr;
      </a>
    """
    return render_email(f"New enquiry: {service_name} - {client_name}", content)


def build_client_confirmation_html(enquiry: Dict[str, Any], service_info: Dict[str, Any]) -> str:
    service_name = service_info.get("name", enquiry.get("service", "General Consultation"))
    client_name = html.escape(enquiry.get("name", "Valued Client"))
    client_line = html.escape(service_info.get("client_line", "Our senior AI & software team will review your scope and follow up shortly."))
    message = html.escape(enquiry.get("message", "")).replace("\n", "<br>")
    
    content = f"""
      <h2 class="heading-underline">We've Received Your Enquiry</h2>
      <p>Hello <strong>{client_name}</strong>,</p>
      <p>Thank you for reaching out to <strong>OM Innoventures & Build AI Technologies</strong>. We have successfully registered your interest in <strong>{html.escape(service_name)}</strong>.</p>
      
      <div class="highlight-card">
        <strong>What happens next:</strong> {client_line}
      </div>
      
      <h3 style="color: #0A1F3D; margin-top: 24px; font-size: 16px;">Summary of Your Submission:</h3>
      <table class="table-details">
        <tr>
          <th>Service</th>
          <td><strong>{html.escape(service_name)}</strong></td>
        </tr>
        <tr>
          <th>Project Overview</th>
          <td>{message}</td>
        </tr>
      </table>
      
      <p style="font-size: 14px; color: #475569;">
        If you have urgent technical briefs or additional architecture diagrams to share, you can directly reply to this email or reach us on WhatsApp at <strong>+91 83101 60257</strong>.
      </p>
      
      <p style="margin-top: 24px; color: #0A1F3D; font-weight: 600;">
        Warm regards,<br>
        <span style="color: #1666A8;">The Engineering & Solutions Team</span><br>
        OM Innoventures & Build AI Technologies
      </p>
    """
    return render_email(f"Thank you for contacting OM Innoventures - {service_name}", content)
