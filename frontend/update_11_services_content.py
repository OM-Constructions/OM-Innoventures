import os
import re

content_dict = {
    "data-analytics-bi": {
        "overview": "Transform your raw data into a strategic asset. Our Data Analytics & BI services provide you with the deep, actionable insights required to make intelligent, data-driven decisions that propel your business forward.",
        "cap_1": ("Data Warehousing", "Centralize your disparate data sources into a secure, single source of truth for unified analysis."),
        "cap_2": ("Interactive Dashboards", "Custom Power BI and Tableau dashboards offering real-time visibility into your core KPIs."),
        "cap_3": ("Predictive Analytics", "Advanced statistical models designed to forecast market trends and customer behaviors."),
        "cap_4": ("Data Governance", "Implement strict data quality and security protocols to ensure compliance and accuracy.")
    },
    "data-science": {
        "overview": "Harness the power of advanced statistics and algorithmic processing to solve your most complex business challenges. We build robust data science pipelines that uncover hidden patterns and optimize operational efficiency.",
        "cap_1": ("Statistical Modeling", "Rigorous application of statistical methods to understand correlations and causations in your data."),
        "cap_2": ("Big Data Processing", "Scalable data pipelines utilizing Apache Spark and Hadoop for massive datasets."),
        "cap_3": ("Algorithm Development", "Custom algorithm creation for pricing optimization, route planning, and resource allocation."),
        "cap_4": ("A/B Testing Frameworks", "Scientifically rigorous testing environments to validate product changes and marketing campaigns.")
    },
    "ai-ml-solutions": {
        "overview": "Deploy cutting-edge Artificial Intelligence and Machine Learning models tailored to your exact industry needs. From natural language processing to computer vision, we build systems that learn and adapt.",
        "cap_1": ("Machine Learning Models", "Custom supervised and unsupervised learning models built to predict outcomes and automate decisions."),
        "cap_2": ("Natural Language Processing", "Advanced text analysis, sentiment tracking, and conversational AI agents."),
        "cap_3": ("Computer Vision", "Automated image and video analysis for quality control, security, and object detection."),
        "cap_4": ("Model Deployment (MLOps)", "Scalable, containerized deployment of ML models ensuring continuous monitoring and low-latency inference.")
    },
    "software-development": {
        "overview": "Bespoke, enterprise-grade software engineering designed to modernize your operations. We build scalable, secure, and highly performant applications tailored to your specific business logic.",
        "cap_1": ("Custom Web Applications", "Responsive, high-performance single-page applications built with React, Vue, or Angular."),
        "cap_2": ("Enterprise Architecture", "Robust backend systems utilizing microservices, Node.js, Python, and cloud-native technologies."),
        "cap_3": ("API Development", "Secure REST and GraphQL APIs for seamless integration with third-party systems."),
        "cap_4": ("Legacy Modernization", "Strategic refactoring and migration of outdated legacy systems to modern cloud infrastructures.")
    },
    "product-development": {
        "overview": "Turn your visionary concept into a market-ready digital product. We provide end-to-end product lifecycle management, from initial ideation and prototyping to launch and continuous iteration.",
        "cap_1": ("MVP Development", "Rapid deployment of Minimum Viable Products to validate market demand quickly and cost-effectively."),
        "cap_2": ("Agile Lifecycle Management", "Iterative development sprints ensuring constant feedback loops and adaptable roadmaps."),
        "cap_3": ("Scalable Architecture", "Foundational engineering designed to support sudden spikes in user growth and feature expansion."),
        "cap_4": ("Post-Launch Optimization", "Continuous feature development, bug fixing, and performance tuning based on real user data.")
    },
    "ui-ux-design": {
        "overview": "Deliver exceptional digital experiences that captivate users and drive conversions. Our UI/UX design process marries stunning visual aesthetics with deep, empathetic user research.",
        "cap_1": ("User Research & Personas", "Deep dives into your target audience to understand their pain points and behavioral patterns."),
        "cap_2": ("Wireframing & Prototyping", "Interactive low and high-fidelity prototypes to visualize the user journey before coding begins."),
        "cap_3": ("Visual Design Systems", "Comprehensive design systems ensuring brand consistency across all digital touchpoints."),
        "cap_4": ("Usability Testing", "Rigorous testing with real users to identify friction points and optimize the interface.")
    },
    "graphic-design": {
        "overview": "Elevate your brand's visual identity with striking, professional graphic design. We create compelling visual assets that communicate your brand's unique value and resonate with your audience.",
        "cap_1": ("Brand Identity & Logos", "Memorable logo design and comprehensive brand guidelines that define your corporate identity."),
        "cap_2": ("Marketing Materials", "High-conversion digital assets including social media graphics, banner ads, and email templates."),
        "cap_3": ("Print & Packaging", "Professional layouts for brochures, business cards, and product packaging."),
        "cap_4": ("Custom Illustrations", "Unique, bespoke illustrations and iconography tailored specifically to your brand voice.")
    },
    "finance-accounting": {
        "overview": "Maintain absolute financial clarity and operational compliance. Our specialized accounting services provide the meticulous oversight required for sustainable business growth and risk mitigation.",
        "cap_1": ("Comprehensive Bookkeeping", "Flawless daily transaction recording, ledger maintenance, and bank reconciliations."),
        "cap_2": ("Financial Reporting", "Preparation of GAAP/IFRS compliant financial statements and executive summaries."),
        "cap_3": ("Payroll Management", "Automated, compliant payroll processing and tax withholding management."),
        "cap_4": ("Strategic Tax Planning", "Proactive tax strategies designed to optimize your financial position based on current regulations.")
    },
    "auditing-assurance": {
        "overview": "Independent, objective financial evaluations designed to build stakeholder trust and improve operational efficiency. We ensure absolute adherence to regulatory standards and internal controls.",
        "cap_1": ("Internal Control Reviews", "Deep evaluations of your financial processes to identify vulnerabilities and inefficiencies."),
        "cap_2": ("Regulatory Compliance", "Rigorous audits ensuring strict adherence to local, state, and federal financial regulations."),
        "cap_3": ("Risk Management", "Identification and strategic mitigation of enterprise-level financial risks."),
        "cap_4": ("Actionable Audit Reports", "Detailed management letters providing specific, actionable recommendations for improvement.")
    },
    "cybersecurity": {
        "overview": "Protect your most valuable digital assets against evolving threats. Our comprehensive cybersecurity services provide impenetrable defense mechanisms and proactive threat monitoring.",
        "cap_1": ("Vulnerability Assessments", "Rigorous penetration testing and scanning to identify network weaknesses before attackers do."),
        "cap_2": ("Security Architecture", "Implementation of Zero Trust frameworks, advanced firewalls, and secure access protocols."),
        "cap_3": ("Incident Response", "Rapid, decisive action plans to neutralize breaches and minimize operational downtime."),
        "cap_4": ("Compliance & Governance", "Ensuring your systems meet strict industry standards such as SOC2, HIPAA, and GDPR.")
    },
    "saas-ai-solutions": {
        "overview": "The pinnacle of digital transformation. We build scalable, multi-tenant Software-as-a-Service platforms deeply integrated with proprietary Artificial Intelligence capabilities.",
        "cap_1": ("Multi-Tenant Architecture", "Secure, scalable cloud infrastructure designed to support thousands of distinct organizations."),
        "cap_2": ("Subscription Billing", "Complex integration with payment gateways for tiered pricing and usage-based billing models."),
        "cap_3": ("Embedded AI Features", "Integration of LLMs and predictive models directly into the SaaS product for end-users."),
        "cap_4": ("Automated Provisioning", "Self-serve onboarding pipelines and role-based access control for enterprise clients.")
    }
}

base_dir = "/home/dilli/OM -AI/frontend/services"

for slug, content in content_dict.items():
    file_path = os.path.join(base_dir, slug, "index.html")
    
    if not os.path.exists(file_path):
        print(f"Skipping {slug}, file not found: {file_path}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace Overview
    overview_pattern = r'(<span class="sp-label">01 &mdash; OVERVIEW</span>\s*)<p>.*?</p>'
    html = re.sub(overview_pattern, r'\1<p>' + content['overview'] + r'</p>', html, flags=re.DOTALL)
    
    # Replace Capabilities
    focus_items = re.findall(r'<div class="sp-focus-item">.*?</div>', html, flags=re.DOTALL)
    
    if len(focus_items) == 4:
        for i in range(4):
            cap_key = f'cap_{i+1}'
            cap_title, cap_desc = content[cap_key]
            
            new_item = f'''<div class="sp-focus-item">
                        <h3>{cap_title}</h3>
                        <p>{cap_desc}</p>
                    </div>'''
            html = html.replace(focus_items[i], new_item, 1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Successfully updated content for all 11 services.")
