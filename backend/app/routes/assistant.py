from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.services.company_info import COMPANY_INFO
from app.services.service_catalog import SERVICES

router = APIRouter(prefix="/assistant", tags=["assistant"])


class ChatRequest(BaseModel):
    query: str
    service_slug: Optional[str] = None


@router.post("")
def ask_assistant(req: ChatRequest):
    q = req.query.lower().strip()
    
    # Intelligent keyword matching for quick tech recommendations
    if any(k in q for k in ["pricing", "cost", "quote", "rate"]):
        response = (
            "Projects at OM Innoventures are scoped individually based on architecture complexity, "
            "integration needs, and delivery timeline. Please submit a project enquiry or book a "
            "General Consultation, and our senior architects will provide a tailored milestone estimate."
        )
    elif any(k in q for k in ["sentinel", "stayhub", "easybuild", "demo", "saas"]):
        response = (
            "We have live production SaaS demos available: "
            "1. Sentinel AI (Workforce Monitoring) — https://sentinelguardai.lovable.app \n"
            "2. StayHub (Smart PG Management) — https://www.stayhub.in \n"
            "3. EasyBuild ( Site OS) — https://www.easybuild.com"
        )
    elif any(k in q for k in ["", "building", "OM Innoventures & Build AI technologies", "civil"]):
        response = (
            "For physical structural engineering, building plans, and architectural design, "
            "please visit our parent brand: OM Innoventures & Build AI technologies at "
            "https://om-buildings.vercel.app/"
        )
    elif any(k in q for k in ["founder", "kishor", "ceo", "who owns"]):
        response = (
            f"{COMPANY_INFO['founder']['name']} is the {COMPANY_INFO['founder']['title']} "
            f"({COMPANY_INFO['founder']['qualifications']}). He leads both physical structural engineering "
            f"and digital intelligence systems from our Basaveshwaranagar, Bengaluru headquarters."
        )
    elif any(k in q for k in ["contact", "phone", "email", "address", "location"]):
        response = (
            f"You can reach us at {COMPANY_INFO['email']} or call/WhatsApp +91 {COMPANY_INFO['phone']}. "
            f"Our physical office is located at {COMPANY_INFO['address']['full']}."
        )
    else:
        # Check matching services
        matched = []
        for slug, svc in SERVICES.items():
            if any(term in q for term in [slug.replace("-", " "), svc["name"].lower()]):
                matched.append(svc["name"])
        
        if matched:
            response = (
                f"We specialize in {', '.join(matched)}. Our engineering team can help architect, "
                f"build, and deploy enterprise-grade solutions for your requirements. "
                f"Feel free to submit a project enquiry below!"
            )
        else:
            response = (
                "Welcome to OM Innoventures & Build AI Technologies! We build intelligent software systems, "
                "enterprise AI/ML pipelines, modern cloud applications, and provide strategic corporate consulting. "
                "How can we assist your business today?"
            )
            
    return {"reply": response}
