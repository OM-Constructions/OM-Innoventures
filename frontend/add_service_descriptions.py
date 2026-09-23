import re

# Comprehensive mapping of service titles to rich, concise descriptions
service_descriptions = {
    # Website Design & Development
    "1-page Landing Page": "High-converting single-page landing pages optimized for speed, mobile responsiveness, and targeted lead generation.",
    "3-5 page Business Website": "Complete corporate website with dedicated pages for company profile, core services, and contact channels.",
    "5-8 page Professional Website": "Comprehensive digital platform for established businesses featuring service catalogs, team profiles, and portfolios.",
    "Business + Contact/Enquiry Forms": "Multi-page business website equipped with smart validated enquiry forms, spam protection, and lead routing.",
    "Dynamic Business Website": "Content-driven web platform with database connectivity, CMS integration, and dynamic user interactions.",
    "E-commerce Website": "Complete online retail storefront featuring secure payment gateway integration, catalog browsing, and cart checkout.",
    "Advanced E-commerce": "Enterprise-scale retail architecture supporting multi-currency, faceted product filtering, and ERP integrations.",
    "Custom Web Application": "Bespoke full-stack web applications tailored to streamline complex business workflows and operations.",
    "AI-powered Website": "Next-generation web experience with integrated AI chatbots, intelligent search, and personalized content feeds.",
    "AI Web Application": "Specialized cloud software built on machine learning models, predictive intelligence, and natural language processing.",
    "Custom SaaS/Web Platform": "Scalable multi-tenant cloud software with subscription billing, team management, and developer API endpoints.",

    # Data Analytics & AI Solutions
    "Excel Data Cleaning": "Professional data cleansing to eliminate duplicates, normalize messy formats, and prepare pristine spreadsheets.",
    "Excel Data Analysis": "In-depth spreadsheet analysis using pivot tables, array formulas, and statistical modeling for clear business insights.",
    "Excel Automation": "Automated workflow pipelines using custom VBA macros and Power Query to save hours of manual repetitive reporting.",
    "SQL Data Analysis": "Advanced relational database querying, aggregation, and performance tuning to extract vital business intelligence.",
    "Power BI Dashboard": "Interactive visual dashboards connecting directly to your data sources for real-time executive KPI monitoring.",
    "Advanced Power BI Dashboard": "Enterprise BI solutions with row-level security, incremental data refresh, and advanced DAX measure modeling.",
    "Python Data Analysis": "Deep exploratory data analysis using Pandas, NumPy, and statistical packages on large-scale datasets.",
    "Python + SQL Analytics": "End-to-end data pipeline extracting database records with SQL and running machine learning algorithms in Python.",
    "Business/Data Analytics": "Strategic business intelligence consulting to define performance KPIs, audit data maturity, and guide growth.",
    "Sales Analytics": "Sales pipeline velocity tracking, win/loss modeling, and revenue forecasting to boost team performance.",
    "HR Analytics": "Workforce analytics covering employee retention, performance metrics, hiring velocity, and compensation benchmarks.",
    "Financial Analytics": "Financial statement analysis, cash flow forecasting, variance analysis, and unit economics modeling.",
    "Logistics / Operations Analytics": "Supply chain optimization, inventory turnover analysis, and route efficiency forecasting.",
    "Predictive Analytics": "Machine learning regression and classification models to forecast future trends, demand, and customer churn.",
    "Machine Learning Model": "Custom supervised and unsupervised ML models trained on your proprietary data for high accuracy inference.",
    "Advanced ML Project": "End-to-end machine learning engineering including feature pipelines, hyperparameter tuning, and cross-validation.",
    "ML + API Deployment": "Production deployment of trained machine learning models via secure, low-latency REST and FastAPI endpoints.",
    "AI Chatbot": "Custom AI conversational agents trained on your business data to handle customer queries and support 24/7.",
    "AI/RAG Knowledge Assistant": "Retrieval-Augmented Generation (RAG) assistant that indexes your documents to deliver accurate verified answers.",
    "AI Business Automation": "Intelligent workflow automation replacing manual repetitive tasks with autonomous AI agents.",
    "AI + ML Custom Solution": "End-to-end custom artificial intelligence system designed for proprietary enterprise operational challenges.",
    "Custom Data/AI Software": "Full-stack enterprise data software integrating databases, analytics dashboards, and AI inference engines.",

    # Finance & Accounting Services
    "Accounting & Bookkeeping": "Precise transaction recording, general ledger management, and compliant financial statements preparation.",
    "Auditing & Assurance": "Independent financial audits, risk assessments, internal control reviews, and regulatory compliance verification.",
    "Taxation & Regulatory Filing": "End-to-end tax planning, GST/corporate tax returns, compliance filing, and advisory services.",
    "CFO & Advisory Services": "Strategic financial planning, capital budgeting, fundraising advisory, and executive cash management."
}

def update_index_services():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match service cards:
    # <a ... class="service-card ..."> ... </a>
    card_pattern = re.compile(r'(<a\s+href="([^"]+)"\s+class="([^"]*service-card[^"]*)"[^>]*>)(.*?)(</a>)', re.DOTALL)

    def replace_card(match):
        open_tag = match.group(1)
        card_content = match.group(4)
        close_tag = match.group(5)

        # Extract title
        title_match = re.search(r'<h3 class="service-title">([^<]+)</h3>', card_content)
        if not title_match:
            return match.group(0)
        
        title = title_match.group(1).strip()
        
        # Determine description
        desc = service_descriptions.get(title)
        if not desc:
            # Fallback matching if minor title mismatch
            for key, val in service_descriptions.items():
                if key.lower() in title.lower() or title.lower() in key.lower():
                    desc = val
                    break
        if not desc:
            desc = f"Professional {title} solutions engineered for performance, precision, and business growth."

        # If card already has service-desc, replace it, otherwise insert after service-price-block
        if '<p class="service-desc">' in card_content:
            card_content = re.sub(r'<p class="service-desc">.*?</p>', f'<p class="service-desc">{desc}</p>', card_content, flags=re.DOTALL)
        else:
            # Insert before service-hover-image or at the end
            desc_html = f'\n                        <p class="service-desc">{desc}</p>'
            if '<div class="service-hover-image">' in card_content:
                card_content = card_content.replace('<div class="service-hover-image">', f'{desc_html}\n                        <div class="service-hover-image">')
            else:
                card_content += desc_html

        return f"{open_tag}{card_content}{close_tag}"

    new_content = card_pattern.sub(replace_card, content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Successfully updated service cards in index.html with rich descriptions!")

if __name__ == '__main__':
    update_index_services()
