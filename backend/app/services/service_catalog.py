from typing import Dict, Any

SERVICES: Dict[str, Dict[str, Any]] = {
    "data-analytics-bi": {
        "slug": "data-analytics-bi",
        "name": "Data Analytics & BI",
        "company_intro": "a data analytics & BI enquiry",
        "client_line": "Our data team will review your requirements and reach out with next steps.",
        "category": "AI & Technology",
        "tagline": "Transform complex data streams into actionable executive intelligence.",
        "description": "We build real-time reporting pipelines, unified enterprise data warehouses, and interactive Business Intelligence dashboards (PowerBI, Tableau, Superset) that empower leaders to make confident, data-driven decisions.",
        "icon": "chart-bar",
        "number": "01",
        "deliverables": [
            "Executive and operational BI dashboards",
            "ETL/ELT data pipeline engineering",
            "Data warehouse modeling (Snowflake, BigQuery, Postgres)",
            "Automated KPI alerts and scheduled reports",
            "Self-service BI enablement and training"
        ],
        "technologies": ["PowerBI", "Tableau", "Apache Superset", "dbt", "Snowflake", "PostgreSQL"]
    },
    "data-science": {
        "slug": "data-science",
        "name": "Data Science",
        "company_intro": "a data science enquiry",
        "client_line": "Our data science team will review your project scope and follow up shortly.",
        "category": "AI & Technology",
        "tagline": "Extract deep predictive patterns and statistical insights from enterprise data.",
        "description": "From customer churn forecasting and demand optimization to exploratory statistical modeling, our data science team turns latent data into high-value competitive advantages.",
        "icon": "flask-conical",
        "number": "02",
        "deliverables": [
            "Predictive modeling & statistical forecasting",
            "Customer segmentation & lifetime value modeling",
            "Time-series analysis and anomaly detection",
            "Feature engineering & exploratory data analysis",
            "Model interpretability and explainability reports"
        ],
        "technologies": ["Python", "Pandas", "NumPy", "SciPy", "Statsmodels", "Jupyter"]
    },
    "ai-ml-solutions": {
        "slug": "ai-ml-solutions",
        "name": "AI / ML Solutions",
        "company_intro": "an AI/ML solutions enquiry",
        "client_line": "Our AI/ML engineers will review your use case and get back to you with next steps.",
        "category": "AI & Technology",
        "tagline": "Production-grade machine learning, computer vision, and GenAI agent systems.",
        "description": "Custom LLM integrations, retrieval-augmented generation (RAG) knowledge engines, autonomous agents, and deep learning architectures engineered for security, speed, and real-world ROI.",
        "icon": "brain-circuit",
        "number": "03",
        "deliverables": [
            "Retrieval-Augmented Generation (RAG) systems",
            "Autonomous multi-agent workflow automations",
            "Computer vision & document OCR pipelines",
            "Fine-tuned LLMs on private enterprise knowledge",
            "Scalable MLOps & inference optimization"
        ],
        "technologies": ["LangChain", "LlamaIndex", "PyTorch", "Hugging Face", "Vector DBs", "TensorFlow"]
    },
    "software-development": {
        "slug": "software-development",
        "name": "Software Development",
        "company_intro": "a software development enquiry",
        "client_line": "Our development team will review your requirements and reach out shortly.",
        "category": "AI & Technology",
        "tagline": "Robust, high-throughput cloud software engineered to scale effortlessly.",
        "description": "Full-stack enterprise applications, microservices, API platforms, and distributed systems built using modern cloud-native architectures with strict security and high test coverage.",
        "icon": "code-xml",
        "number": "04",
        "deliverables": [
            "Full-stack web applications and SaaS platforms",
            "RESTful & GraphQL microservice APIs",
            "Cloud migration and infrastructure refactoring",
            "Third-party integrations & payment gateways",
            "Automated CI/CD pipelines & test suites"
        ],
        "technologies": ["Python / FastAPI", "Node.js / Express", "React", "Next.js", "Docker", "AWS"]
    },
    "full-stack-development": {
        "slug": "full-stack-development",
        "name": "Full Stack Development",
        "company_intro": "a full stack development enquiry",
        "client_line": "Our full stack engineering team will review your application requirements and reach out with next steps.",
        "category": "AI & Technology",
        "tagline": "End-to-end full stack web, mobile, and cloud architectures built for speed and scale.",
        "description": "Seamless integration of reactive, high-performance frontends (React, Next.js, Vue) with resilient backend APIs (Python FastAPI, Node.js), relational & NoSQL databases, authentication, and automated cloud deployments.",
        "icon": "layers",
        "number": "04B",
        "deliverables": [
            "Modern frontend SPAs & SSR applications (React, Next.js, TypeScript)",
            "Scalable backend APIs & microservices (Python FastAPI, Node.js)",
            "Database architecture, ORM design & schema indexing (PostgreSQL, MongoDB, Redis)",
            "Authentication, role-based access control (RBAC) & OAuth2",
            "Full DevOps integration: Docker, Kubernetes, CI/CD pipelines & AWS/GCP"
        ],
        "technologies": ["Next.js", "React", "Python / FastAPI", "Node.js", "PostgreSQL", "MongoDB", "Redis", "Docker", "AWS"]
    },
    "product-development": {
        "slug": "product-development",
        "name": "Product Development",
        "company_intro": "a product development enquiry",
        "client_line": "Our product team will review your idea and follow up to discuss scope.",
        "category": "AI & Technology",
        "tagline": "From concept validation and wireframing to rapid MVP launch and scale.",
        "description": "We partner with visionary founders and enterprise innovation units to define product roadmaps, build high-converting MVPs, and iteratively refine product-market fit with agile velocity.",
        "icon": "box",
        "number": "05",
        "deliverables": [
            "MVP scoping, technical feasibility & roadmap",
            "Rapid clickable prototyping and user testing",
            "Full-lifecycle agile product engineering",
            "Analytics, onboarding & conversion funnels",
            "Continuous post-launch feature iteration"
        ],
        "technologies": ["Figma", "Agile / Scrum", "Next.js", "PostgreSQL", "Mixpanel", "Stripe"]
    },
    "ui-ux-design": {
        "slug": "ui-ux-design",
        "name": "UI / UX Design",
        "company_intro": "a UI/UX design enquiry",
        "client_line": "Our design team will review your project and reach out with next steps.",
        "category": "AI & Technology",
        "tagline": "Intuitive, human-centric digital interfaces designed to delight and convert.",
        "description": "User research, information architecture, design systems, and responsive interfaces that blend aesthetic beauty with seamless usability across web, tablet, and mobile surfaces.",
        "icon": "palette",
        "number": "06",
        "deliverables": [
            "Comprehensive UX wireframes and user flows",
            "Figma design systems and atomic UI components",
            "High-fidelity interactive prototypes",
            "Accessibility (WCAG) audit and compliance",
            "Micro-interaction and motion design guidelines"
        ],
        "technologies": ["Figma", "FigJam", "Design Systems", "Prototyping", "Design Tokens"]
    },
    "graphic-design": {
        "slug": "graphic-design",
        "name": "Graphic Design",
        "company_intro": "a graphic design enquiry",
        "client_line": "Our creative team will review your brief and follow up shortly.",
        "category": "AI & Technology",
        "tagline": "Compelling visual identities, marketing collateral, and brand narratives.",
        "description": "Impactful visual assets that elevate your brand presence—from corporate identity packages and brand guidelines to digital advertising, pitch decks, and print-ready collateral.",
        "icon": "pen-tool",
        "number": "07",
        "deliverables": [
            "Brand identity guidelines & vector logo design",
            "Investor pitch decks & executive presentations",
            "Digital marketing graphics & social media kits",
            "Print-ready brochures, banners & corporate stationery",
            "Custom iconography and illustrative assets"
        ],
        "technologies": ["Adobe Illustrator", "Photoshop", "InDesign", "Figma", "Vector Graphics"]
    },
    "finance-accounting": {
        "slug": "finance-accounting",
        "name": "Finance & Accounting Services",
        "company_intro": "a finance & accounting services enquiry",
        "client_line": "Our finance team will review your requirements and reach out shortly.",
        "category": "Professional Services",
        "tagline": "End-to-end corporate financial management, compliance, and book-keeping.",
        "description": "Full-spectrum financial bookkeeping, GST filings, corporate tax planning, financial statement preparation, and virtual CFO services for startups and high-growth corporations.",
        "icon": "receipt",
        "number": "08",
        "deliverables": [
            "Bookkeeping, ledger maintenance & reconciliations",
            "GST, TDS & corporate statutory tax filing",
            "Financial modeling, budget forecasting & cashflow management",
            "Virtual CFO advisory and fundraising support",
            "Payroll processing and statutory compliance"
        ],
        "technologies": ["Tally Prime", "QuickBooks", "Zoho Books", "Advanced Excel", "SAP"]
    },
    "auditing-assurance": {
        "slug": "auditing-assurance",
        "name": "Auditing & Assurance Services",
        "company_intro": "an auditing & assurance enquiry",
        "client_line": "Our audit team will review your scope and follow up with next steps.",
        "category": "Professional Services",
        "tagline": "Rigorous internal, statutory, and forensic audits ensuring compliance.",
        "description": "Thorough audit methodologies that reinforce corporate governance, safeguard financial integrity, mitigate organizational risks, and satisfy all regulatory audit mandates.",
        "icon": "shield-check",
        "number": "09",
        "deliverables": [
            "Statutory and internal risk-based audit reviews",
            "Internal financial control (IFC) assessments",
            "Compliance audits for regulatory frameworks",
            "Forensic accounting & fraud investigation reviews",
            "Audit report certification and management recommendations"
        ],
        "technologies": ["Audit Automation", "CaseWare", "Risk Frameworks", "IFRS", "GAAP"]
    },
    "cybersecurity": {
        "slug": "cybersecurity",
        "name": "Cybersecurity Services",
        "company_intro": "a cybersecurity services enquiry",
        "client_line": "Our security team will review your requirements and reach out shortly.",
        "category": "Professional Services",
        "tagline": "Proactive vulnerability assessments, cloud hardening, and threat mitigation.",
        "description": "Defend your digital assets with comprehensive penetration testing (VAPT), cloud infrastructure posture evaluations, threat modeling, and zero-trust security architectures.",
        "icon": "lock-keyhole",
        "number": "10",
        "deliverables": [
            "Web, Mobile, and API Vulnerability Assessment & Pen-Testing (VAPT)",
            "Cloud security posture review (AWS / Azure / GCP)",
            "Compliance audit readiness (ISO 27001, SOC 2, GDPR)",
            "Security policy architecture & incident response plans",
            "Employee cybersecurity awareness & phishing simulations"
        ],
        "technologies": ["Burp Suite", "OWASP ZAP", "Nessus", "Wireshark", "CloudTrail", "SonarQube"]
    },
    "saas-ai-solutions": {
        "slug": "saas-ai-solutions",
        "name": "SaaS & AI Powered Solutions",
        "company_intro": "a SaaS & AI solutions enquiry",
        "client_line": "Our solutions team will review your requirements and follow up with next steps.",
        "category": "Professional Services",
        "tagline": "Turnkey enterprise SaaS platforms enhanced with intelligent automation.",
        "description": "Customizable, ready-to-deploy software-as-a-service ecosystems engineered for workforce operations, property management,  workflows, and automated enterprise communications.",
        "icon": "sparkles",
        "number": "11",
        "deliverables": [
            "White-label SaaS platform customization",
            "Intelligent automation workflows & bot integrations",
            "Multi-tenant database and security architectures",
            "Subscription, billing & role-based access controls",
            "Dedicated cloud deployment and 24/7 SLA maintenance"
        ],
        "technologies": ["Multi-Tenant Architecture", "Stripe Billing", "FastAPI", "Next.js", "Redis", "Docker"]
    }
}

FALLBACK_SERVICE = {
    "slug": "general-consultation",
    "name": "General Consultation & Project Planning",
    "company_intro": "a general consultation & project planning enquiry",
    "client_line": "Our senior AI & software team will review your scope and get in touch within 24 hours.",
    "category": "General",
    "tagline": "Comprehensive advisory, technical scoping, and strategic technology roadmapping.",
    "description": "Discuss your goals with our senior engineering architects and tech advisors to formulate the optimal tech stack, team composition, and delivery roadmap.",
    "icon": "compass",
    "number": "00"
}


def get_service(slug: str) -> Dict[str, Any]:
    if slug in SERVICES:
        return SERVICES[slug]
    if slug == "general-consultation":
        return FALLBACK_SERVICE
    return {
        "slug": slug,
        "name": slug.replace("-", " ").title(),
        "company_intro": f"an enquiry regarding {slug.replace('-', ' ')}",
        "client_line": "Our team will review your requirements and reach out shortly.",
        "category": "Technology & Services",
        "tagline": "Professional solutions tailored to your operational objectives.",
        "description": "Tailored engineering and advisory services designed to solve specific operational challenges.",
        "icon": "layers",
        "number": "--"
    }


def get_all_services():
    return list(SERVICES.values())
