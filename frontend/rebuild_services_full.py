import os
import re

services = [
    '1-page-landing-page', '3-5-page-business-website', '5-8-page-professional-website',
    'accounting', 'advanced-e-commerce', 'advanced-ml-project', 'advanced-power-bi-dashboard',
    'ai-business-automation', 'ai-chatbot', 'ai-ml-custom-solution', 'ai-ml-solutions',
    'ai-powered-website', 'airag-knowledge-assistant', 'ai-web-application', 'audit-accounting',
    'auditing', 'auditing-assurance', 'business-contactenquiry-forms', 'businessdata-analytics',
    '-analytics', 'corporate-audit-accounting', 'custom-dataai-software',
    'custom-saasweb-platform', 'custom-web-application', 'cybersecurity', 'data-analytics-bi',
    'data-science', 'dynamic-business-website', 'e-commerce-website', 'excel-automation',
    'excel-data-analysis', 'excel-data-cleaning', 'finance-accounting', 'financial-analytics',
    'graphic-design', 'hr-analytics', 'machine-learning-model', 'ml-api-deployment',
    'power-bi-dashboard', 'predictive-analytics', 'product-development', 'python-data-analysis',
    'python-sql-analytics', 'saas-ai-solutions', 'sales-analytics', 'software-development',
    'sql-data-analysis', 'ui-ux-design'
]

def get_category(slug):
    if 'ai' in slug or 'ml' in slug or 'chatbot' in slug or 'automation' in slug or 'predictive' in slug:
        return 'ai'
    if 'data' in slug or 'excel' in slug or 'sql' in slug or 'analytics' in slug or 'power-bi' in slug:
        return 'data'
    if 'web' in slug or 'landing' in slug or 'ecommerce' in slug or 'saas' in slug or 'page' in slug:
        return 'web'
    if 'account' in slug or 'audit' in slug or 'finance' in slug:
        return 'finance'
    if 'design' in slug or 'ui-ux' in slug:
        return 'design'
    if 'cyber' in slug or 'security' in slug:
        return 'security'
    return 'software'

def get_tech_stack(category):
    stacks = {
        'ai': ['TensorFlow', 'PyTorch', 'OpenAI API', 'Hugging Face', 'Pinecone', 'Python'],
        'data': ['Python (Pandas/NumPy)', 'SQL Server', 'Power BI', 'Apache Spark', 'Tableau', 'Snowflake'],
        'web': ['React.js', 'Next.js', 'Node.js', 'PostgreSQL', 'AWS', 'Vercel'],
        'finance': ['QuickBooks', 'Xero', 'SAP', 'Oracle NetSuite', 'Excel (Advanced)', 'Power Query'],
        'design': ['Figma', 'Adobe XD', 'Illustrator', 'Photoshop', 'Webflow', 'InVision'],
        'security': ['Kali Linux', 'Burp Suite', 'Splunk', 'Wireshark', 'Metasploit', 'CrowdStrike'],
        'software': ['Docker', 'Kubernetes', 'Go', 'Python', 'AWS', 'GraphQL']
    }
    return stacks.get(category, stacks['software'])

def get_process():
    return [
        ("01. Discovery & Strategy", "We start by deeply understanding your business goals, current bottlenecks, and target audience."),
        ("02. Architecture & Design", "Our team drafts a comprehensive blueprint, wireframes, or data models tailored to your exact needs."),
        ("03. Agile Development", "We build your solution iteratively, providing regular updates and incorporating your feedback."),
        ("04. Testing & QA", "Rigorous testing across multiple scenarios ensures a secure, flawless deployment."),
        ("05. Launch & Optimization", "We seamlessly deploy the solution and provide ongoing support and performance tuning.")
    ]

def get_why_us():
    return [
        ("Domain Expertise", "Years of specialized experience delivering high-impact solutions in this exact field."),
        ("Data-Driven Approach", "Every decision we make is backed by rigorous analytics and verifiable metrics."),
        ("Agile & Transparent", "Complete visibility into our process with weekly sprints and open communication channels."),
        ("Enterprise-Grade Security", "We implement strict security protocols from day one to protect your critical assets.")
    ]

def generate_case_study(slug, category):
    if category == 'ai':
        return {
            "title": "Automating Customer Support for a Global Retailer",
            "metric1": "85%", "metric1_label": "Reduction in Response Time",
            "metric2": "24/7", "metric2_label": "Automated Coverage",
            "description": f"A major e-commerce client was struggling with high support volumes. We deployed a custom {slug.replace('-', ' ')} solution that integrated directly with their CRM. The system learned from historical tickets to automatically resolve level-1 inquiries, saving the company $1.2M annually while increasing customer satisfaction scores."
        }
    elif category == 'data':
        return {
            "title": "Supply Chain Optimization via Predictive Analytics",
            "metric1": "$3.4M", "metric1_label": "Logistics Savings",
            "metric2": "99.2%", "metric2_label": "Inventory Accuracy",
            "description": f"A manufacturing firm lacked visibility into their logistics pipeline. Using our {slug.replace('-', ' ')} expertise, we centralized their disparate databases and built a real-time dashboard. We applied predictive models to forecast demand spikes, allowing them to optimize warehouse storage and dramatically cut emergency shipping costs."
        }
    elif category == 'web':
        return {
            "title": "Scaling a SaaS Platform to 100k Active Users",
            "metric1": "3x", "metric1_label": "Increase in Conversions",
            "metric2": "<1s", "metric2_label": "Average Load Time",
            "description": f"An expanding startup needed their legacy platform completely rebuilt. We architected a highly scalable {slug.replace('-', ' ')} that utilized a modern microservices backend and a lightning-fast frontend. The new platform easily handled a 400% traffic surge following a successful marketing campaign without a single dropped request."
        }
    elif category == 'finance':
        return {
            "title": "Streamlining Corporate Financial Consolidation",
            "metric1": "14 Days", "metric1_label": "Faster Month-End Close",
            "metric2": "100%", "metric2_label": "Compliance Audit Pass",
            "description": f"A multinational corporation was taking three weeks to close their monthly books across 5 subsidiaries. Through our {slug.replace('-', ' ')} engagement, we automated their ledger consolidations, integrated disparate ERP systems, and established rigorous internal controls, cutting their close time in half and ensuring flawless regulatory compliance."
        }
    else:
        return {
            "title": f"Transforming Operations with {slug.replace('-', ' ').title()}",
            "metric1": "40%", "metric1_label": "Efficiency Gain",
            "metric2": "Zero", "metric2_label": "Security Breaches",
            "description": f"Our client needed a complete overhaul of their legacy processes. We delivered a customized {slug.replace('-', ' ')} that modernized their workflow, integrated their existing tooling, and established a foundation for sustainable, long-term growth. The project was delivered 2 weeks ahead of schedule."
        }

base_dir = "/home/dilli/OM -AI/frontend/services"

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE_UPPER__ | OM Innoventures</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../style.css?v=12">
    
    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
                "gsap": "https://unpkg.com/gsap@3.12.2/index.js",
                "gsap/ScrollTrigger": "https://unpkg.com/gsap@3.12.2/ScrollTrigger.js"
            }
        }
    </script>
    <style>
        /* Fallback for GSAP if JS fails */
        .gsap-reveal {
            opacity: 1 !important;
            visibility: visible !important;
            transform: none !important;
        }
        
        /* Layout specific styles for new sections */
        .sp-process-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-top: 40px;
        }
        @media(min-width: 768px) {
            .sp-process-grid { grid-template-columns: 1fr 1fr; }
        }
        @media(min-width: 1024px) {
            .sp-process-grid { grid-template-columns: 1fr 1fr 1fr; }
        }
        .sp-process-step {
            background: rgba(255,255,255,0.05);
            padding: 30px;
            border-left: 3px solid var(--gold-accent);
            border-radius: 4px;
        }
        .sp-process-step h3 { color: var(--gold-accent); font-family: 'Exo 2', sans-serif; font-size: 1.2rem; margin-bottom: 10px; }
        
        .sp-tech-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 30px;
        }
        .sp-tech-badge {
            background: var(--navy-primary);
            color: white;
            padding: 10px 20px;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 600;
            border: 1px solid rgba(255,255,255,0.1);
        }
        
        .sp-why-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 30px;
            margin-top: 40px;
        }
        @media(min-width: 768px) {
            .sp-why-grid { grid-template-columns: 1fr 1fr; }
        }
        .sp-why-item {
            display: flex;
            gap: 20px;
        }
        .sp-why-icon {
            width: 50px;
            height: 50px;
            background: rgba(234, 182, 118, 0.1);
            color: var(--gold-accent);
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            font-size: 1.5rem;
            flex-shrink: 0;
        }
        
        .sp-case-study-box {
            background: white;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            margin-top: 40px;
        }
        .sp-case-metrics {
            display: flex;
            gap: 40px;
            margin-bottom: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 30px;
        }
        .sp-metric-val {
            font-size: 2.5rem;
            font-family: 'Exo 2', sans-serif;
            font-weight: 800;
            color: var(--navy-primary);
        }
        .sp-metric-label {
            color: #666;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .sp-cta-banner {
            background: var(--navy-primary);
            color: white;
            text-align: center;
            padding: 80px 20px;
            border-radius: 12px;
            margin: 60px 0;
        }
        .sp-cta-banner h2 { color: white; margin-bottom: 20px; }
        .sp-cta-banner p { color: rgba(255,255,255,0.8); margin-bottom: 40px; max-width: 600px; margin-left: auto; margin-right: auto; }
    </style>
</head>
<body>

    <!-- NAV BAR -->
    <nav id="navbar" class="scrolled">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span class="brand-om">OM</span><span class="brand-long">Innoventures</span>
            </a>
            <div class="nav-links">
                <a href="../../index.html#hero" class="nav-link-item">Home</a>
                <a href="../../index.html#services" class="nav-link-item">Services</a>
            </div>
            <div class="nav-actions">
                <span id="nav-auth-container" class="nav-auth-group">
                    <a href="../../login.html" class="nav-auth-link nav-auth-login">Log In</a>
                    <a href="../../signup.html" class="nav-auth-link nav-auth-signup">Sign Up</a>
                </span>
                <a href="../../index.html#cta" class="btn-primary">Let's Talk</a>
            </div>
            <button class="hamburger">☰</button>
        </div>
    </nav>

    <main class="service-page-main">
        <!-- 1. HERO -->
        <section class="service-page-hero">
            <div class="container gsap-reveal">
                <span class="eyebrow">SERVICE DETAILS</span>
                <h1>__TITLE_UPPER__</h1>
                <p style="font-size: 1.2rem; max-width: 800px; margin: 0 auto; opacity: 0.9;">Professional __TITLE_CLEAN__ solutions driving innovation and efficiency.</p>
                <div style="margin-top: 30px;">
                    <a href="../../index.html#cta" class="btn-primary">Discuss Your Project</a>
                </div>
                <div class="service-hero-accent"></div>
            </div>
        </section>

        <!-- 2. OVERVIEW -->
        <section class="sp-section sp-overview">
            <div class="container gsap-reveal">
                <span class="sp-label">01 &mdash; OVERVIEW</span>
                <h2 class="sp-title">Transforming Potential into Performance</h2>
                <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;">
                    In today's fast-paced digital environment, leveraging the right __TITLE_CLEAN__ strategies is no longer optional—it's critical for survival and growth. Our __TITLE_CLEAN__ service is meticulously designed to address your specific operational bottlenecks and unlock new avenues for scalability.
                </p>
                <p style="font-size: 1.1rem; line-height: 1.8;">
                    We don't just deliver out-of-the-box solutions. We partner with you to understand the intricacies of your business, ensuring that our execution aligns perfectly with your long-term objectives. Whether you're looking to optimize costs, improve user engagement, or completely overhaul your backend architecture, our expert team provides the precision and reliability you demand.
                </p>
            </div>
        </section>

        <!-- 3. KEY OFFERINGS -->
        <section class="sp-section sp-section-gray">
            <div class="container gsap-reveal">
                <span class="sp-label" style="color: var(--navy-primary);">02 &mdash; KEY OFFERINGS</span>
                <h2 class="sp-title">Capabilities & Deliverables</h2>
                <div class="sp-focus-grid">
                    <div class="sp-focus-item">
                        <h3>Strategic Alignment</h3>
                        <p>Comprehensive audits and roadmap development tailored specifically to your __TITLE_CLEAN__ requirements.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Custom Engineering</h3>
                        <p>Bespoke development and implementation utilizing industry-leading methodologies and secure architectures.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Scalable Infrastructure</h3>
                        <p>Designing solutions built to handle massive growth, ensuring your systems never buckle under pressure.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Ongoing Optimization</h3>
                        <p>Continuous monitoring, A/B testing, and refinement to maximize your return on investment over time.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- 4. PROCESS / APPROACH -->
        <section class="sp-section">
            <div class="container gsap-reveal">
                <span class="sp-label">03 &mdash; OUR APPROACH</span>
                <h2 class="sp-title">How We Deliver Excellence</h2>
                <div class="sp-process-grid">
__PROCESS_HTML__
                </div>
            </div>
        </section>
        
        <!-- 5. TECH STACK / TOOLS -->
        <section class="sp-section sp-section-gray">
            <div class="container gsap-reveal">
                <span class="sp-label" style="color: var(--navy-primary);">04 &mdash; TECHNOLOGY</span>
                <h2 class="sp-title">Tools We Use</h2>
                <p>We utilize a modern, enterprise-grade technology stack to ensure performance, security, and maintainability.</p>
                <div class="sp-tech-grid">
__TECH_HTML__
                </div>
            </div>
        </section>
        
        <!-- 6. WHY CHOOSE US -->
        <section class="sp-section">
            <div class="container gsap-reveal">
                <span class="sp-label">05 &mdash; WHY US</span>
                <h2 class="sp-title">The OM Innoventures Advantage</h2>
                <div class="sp-why-grid">
__WHY_US_HTML__
                </div>
            </div>
        </section>
        
        <!-- 7. CASE STUDY -->
        <section class="sp-section sp-section-gray">
            <div class="container gsap-reveal">
                <span class="sp-label" style="color: var(--navy-primary);">06 &mdash; PROVEN SUCCESS</span>
                <h2 class="sp-title">Featured Case Study</h2>
                
                <div class="sp-case-study-box">
                    <h3 style="font-size: 1.8rem; margin-bottom: 30px; color: var(--navy-primary);">__CASE_TITLE__</h3>
                    <div class="sp-case-metrics">
                        <div>
                            <div class="sp-metric-val">__CASE_M1__</div>
                            <div class="sp-metric-label">__CASE_M1_L__</div>
                        </div>
                        <div>
                            <div class="sp-metric-val">__CASE_M2__</div>
                            <div class="sp-metric-label">__CASE_M2_L__</div>
                        </div>
                    </div>
                    <p style="font-size: 1.1rem; line-height: 1.8; color: #444;">
                        "__CASE_DESC__"
                    </p>
                </div>
            </div>
        </section>
        
        <!-- 8. CLOSING CTA BANNER -->
        <section class="sp-section">
            <div class="container gsap-reveal">
                <div class="sp-cta-banner">
                    <h2 class="sp-title">Ready to Elevate Your Business?</h2>
                    <p>Let's discuss how our __TITLE_CLEAN__ expertise can solve your most pressing challenges and accelerate your growth.</p>
                    <a href="../../index.html#cta" class="btn-primary" style="background: var(--gold-accent); color: var(--navy-primary);">Schedule a Free Consultation</a>
                </div>
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>OM INNOVENTURES</h3>
                    <p>&amp; AI TECHNOLOGIES</p>
                </div>
                <div class="footer-col">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="../../index.html#hero">Home</a></li>
                        <li><a href="../../index.html#services">Services</a></li>
                        <li><a href="../../index.html#capabilities">Capabilities</a></li>
                        <li><a href="../../index.html#about">About</a></li>
                        <li><a href="../../index.html#cta">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 OM Innoventures. All rights reserved.</span>
            </div>
        </div>
    </footer>

    <script type="module" src="../../src/main.js"></script>

    <!-- FIXED GSAP IMPORT -->
    <script type="module">
        import gsap from 'https://unpkg.com/gsap@3.12.2/index.js';
        import ScrollTrigger from 'https://unpkg.com/gsap@3.12.2/ScrollTrigger.js';
        
        gsap.registerPlugin(ScrollTrigger);

        // Remove CSS fallback so GSAP can handle animation
        const reveals = document.querySelectorAll('.gsap-reveal');
        reveals.forEach(el => {
            el.style.opacity = '0';
            el.style.visibility = 'hidden';
        });

        setTimeout(() => {
            reveals.forEach((el) => {
                gsap.fromTo(el, 
                    { opacity: 0, y: 50, visibility: 'hidden' }, 
                    {
                        scrollTrigger: {
                            trigger: el,
                            start: "top 85%",
                            toggleActions: "play none none none"
                        },
                        opacity: 1,
                        y: 0,
                        visibility: 'visible',
                        duration: 1,
                        ease: "power2.out",
                        clearProps: "all" 
                    }
                );
            });
        }, 100);
    </script>
</body>
</html>
"""

updated_count = 0
not_found_count = 0

for slug in services:
    slug_path = os.path.join(base_dir, slug)
    if not os.path.isdir(slug_path):
        not_found_count += 1
        continue
    
    file_path = os.path.join(slug_path, "index.html")
    
    title_clean = slug.replace('-', ' ')
    title_upper = title_clean.upper()
    category = get_category(slug)
    
    # Process HTML
    process_html = ""
    for title, desc in get_process():
        process_html += f'                    <div class="sp-process-step"><h3>{title}</h3><p>{desc}</p></div>\n'
        
    # Tech HTML
    tech_html = ""
    for tech in get_tech_stack(category):
        tech_html += f'                    <span class="sp-tech-badge">{tech}</span>\n'
        
    # Why Us HTML
    why_us_html = ""
    for title, desc in get_why_us():
        why_us_html += f'                    <div class="sp-why-item"><div class="sp-why-icon">✦</div><div><h3 style="color: var(--navy-primary); margin-bottom: 8px;">{title}</h3><p>{desc}</p></div></div>\n'
        
    # Case Study
    case_study = generate_case_study(slug, category)
    
    html = html_template.replace("__TITLE_UPPER__", title_upper)
    html = html.replace("__TITLE_CLEAN__", title_clean.title())
    html = html.replace("__PROCESS_HTML__", process_html.rstrip())
    html = html.replace("__TECH_HTML__", tech_html.rstrip())
    html = html.replace("__WHY_US_HTML__", why_us_html.rstrip())
    html = html.replace("__CASE_TITLE__", case_study['title'])
    html = html.replace("__CASE_M1__", case_study['metric1'])
    html = html.replace("__CASE_M1_L__", case_study['metric1_label'])
    html = html.replace("__CASE_M2__", case_study['metric2'])
    html = html.replace("__CASE_M2_L__", case_study['metric2_label'])
    html = html.replace("__CASE_DESC__", case_study['description'])
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    updated_count += 1

print(f"Successfully rebuilt {updated_count} service pages with the full 8-section template and GSAP fix.")
if not_found_count > 0:
    print(f"Note: {not_found_count} directories were not found.")
