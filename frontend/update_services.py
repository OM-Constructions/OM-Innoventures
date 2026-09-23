import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new HTML blocks
website_design = [
    ("1-page Landing Page", "₹7,999"),
    ("3-5 page Business Website", "₹14,999"),
    ("5-8 page Professional Website", "₹24,999"),
    ("Business + Contact/Enquiry Forms", "₹29,999"),
    ("Dynamic Business Website", "₹39,999"),
    ("E-commerce Website", "₹49,999+"),
    ("Advanced E-commerce", "₹74,999+"),
    ("Custom Web Application", "₹99,999+"),
    ("AI-powered Website", "₹74,999+"),
    ("AI Web Application", "₹1,49,999+"),
    ("Custom SaaS/Web Platform", "₹2,49,999+")
]

data_ai_services = [
    ("Excel Data Cleaning", "₹4,999"),
    ("Excel Data Analysis", "₹7,999"),
    ("Excel Automation", "₹9,999"),
    ("SQL Data Analysis", "₹9,999"),
    ("Power BI Dashboard", "₹12,999"),
    ("Advanced Power BI Dashboard", "₹19,999"),
    ("Python Data Analysis", "₹14,999"),
    ("Python + SQL Analytics", "₹19,999"),
    ("Business/Data Analytics", "₹24,999"),
    ("Sales Analytics", "₹14,999"),
    ("HR Analytics", "₹14,999"),
    ("Financial Analytics", "₹19,999"),
    (" Analytics", "₹19,999"),
    ("Predictive Analytics", "₹34,999"),
    ("Machine Learning Model", "₹39,999"),
    ("Advanced ML Project", "₹59,999"),
    ("ML + API Deployment", "₹74,999"),
    ("AI Chatbot", "₹49,999"),
    ("AI/RAG Knowledge Assistant", "₹69,999"),
    ("AI Business Automation", "₹59,999"),
    ("AI + ML Custom Solution", "₹99,999+"),
    ("Custom Data/AI Software", "₹1,49,999+")
]

accounting_services = [
    ("Accounting", "Starting ₹4,999"),
    ("Auditing", "Starting ₹19,999"),
    ("Audit + Accounting", "Starting ₹49,999"),
    ("Corporate Audit & Accounting", "Starting ₹99,999")
]

def to_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def create_cards(services, start_index, default_img="service_nlp.jpg"):
    html = '<div class="services-grid">\n'
    for i, (title, price) in enumerate(services):
        index = start_index + i
        slug = to_slug(title)
        html += f'''                    <a href="services/{slug}/index.html" class="service-card" data-index="{index}">
                        <span class="service-number">{index:02d}</span>
                        <h3 class="service-title">{title}</h3>
                        <div class="service-price-block">
                            <span class="price-label">PRICE</span>
                            <span class="price-value">{price}</span>
                        </div>
                        <div class="service-hover-image">
                            <img src="assets/ai_images/{default_img}" alt="{title}">
                        </div>
                    </a>\n'''
    html += '                </div>'
    return html

website_html = create_cards(website_design, 1, "service_vision.jpg")
data_ai_html = create_cards(data_ai_services, 1, "service_ml.jpg")
accounting_html = create_cards(accounting_services, 1, "service_analytics.jpg")

new_services_section = f'''        <!-- SERVICES - WEBSITE DESIGN -->
        <section id="services-website" class="section-gray">
            <div class="container">
                <span class="eyebrow">OUR DIGITAL SERVICES</span>
                <h2 class="section-title">Website Design & Development</h2>
                <p class="section-subtitle">Premium web platforms built for speed, conversion, and intelligence.</p>
                {website_html}
            </div>
        </section>

        <!-- SERVICES - DATA & AI -->
        <section id="services-ai" class="section-gray" style="background-color: var(--dark-bg); color: var(--text-light);">
            <div class="container">
                <span class="eyebrow">OUR INTELLIGENCE SERVICES</span>
                <h2 class="section-title" style="color: var(--gold-accent);">Data Analytics & AI Solutions</h2>
                <p class="section-subtitle" style="color: #999;">Advanced machine learning, predictive analytics, and automated AI agents.</p>
                {data_ai_html}
            </div>
        </section>

        <!-- SERVICES - ACCOUNTING -->
        <section id="services-accounting" class="section-gray">
            <div class="container">
                <span class="eyebrow">OUR ASSURANCE SERVICES</span>
                <h2 class="section-title">Accounting & Auditing</h2>
                <p class="section-subtitle">Precise financial management, compliance, and auditing services delivered by qualified professionals.</p>
                {accounting_html}
            </div>
        </section>'''

# Replace the existing services section
pattern = r'<!-- SERVICES -->\s*<section id="services" class="section-gray">.*?</section>'
content = re.sub(pattern, new_services_section, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
