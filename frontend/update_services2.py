import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# All services combined into one list
all_services = [
    # Website Design Services
    ("1-page Landing Page", "₹7,999", "service_vision.jpg"),
    ("3-5 page Business Website", "₹14,999", "service_vision.jpg"),
    ("5-8 page Professional Website", "₹24,999", "service_vision.jpg"),
    ("Business + Contact/Enquiry Forms", "₹29,999", "service_vision.jpg"),
    ("Dynamic Business Website", "₹39,999", "service_vision.jpg"),
    ("E-commerce Website", "₹49,999+", "service_vision.jpg"),
    ("Advanced E-commerce", "₹74,999+", "service_vision.jpg"),
    ("Custom Web Application", "₹99,999+", "service_vision.jpg"),
    ("AI-powered Website", "₹74,999+", "service_vision.jpg"),
    ("AI Web Application", "₹1,49,999+", "service_vision.jpg"),
    ("Custom SaaS/Web Platform", "₹2,49,999+", "service_vision.jpg"),
    
    # Data & AI Services
    ("Excel Data Cleaning", "₹4,999", "service_ml.jpg"),
    ("Excel Data Analysis", "₹7,999", "service_ml.jpg"),
    ("Excel Automation", "₹9,999", "service_ml.jpg"),
    ("SQL Data Analysis", "₹9,999", "service_ml.jpg"),
    ("Power BI Dashboard", "₹12,999", "service_ml.jpg"),
    ("Advanced Power BI Dashboard", "₹19,999", "service_ml.jpg"),
    ("Python Data Analysis", "₹14,999", "service_ml.jpg"),
    ("Python + SQL Analytics", "₹19,999", "service_ml.jpg"),
    ("Business/Data Analytics", "₹24,999", "service_ml.jpg"),
    ("Sales Analytics", "₹14,999", "service_ml.jpg"),
    ("HR Analytics", "₹14,999", "service_ml.jpg"),
    ("Financial Analytics", "₹19,999", "service_ml.jpg"),
    (" Analytics", "₹19,999", "service_ml.jpg"),
    ("Predictive Analytics", "₹34,999", "service_ml.jpg"),
    ("Machine Learning Model", "₹39,999", "service_ml.jpg"),
    ("Advanced ML Project", "₹59,999", "service_ml.jpg"),
    ("ML + API Deployment", "₹74,999", "service_ml.jpg"),
    ("AI Chatbot", "₹49,999", "service_ml.jpg"),
    ("AI/RAG Knowledge Assistant", "₹69,999", "service_ml.jpg"),
    ("AI Business Automation", "₹59,999", "service_ml.jpg"),
    ("AI + ML Custom Solution", "₹99,999+", "service_ml.jpg"),
    ("Custom Data/AI Software", "₹1,49,999+", "service_ml.jpg"),
    
    # Accounting Services
    ("Accounting", "Starting ₹4,999", "service_analytics.jpg"),
    ("Auditing", "Starting ₹19,999", "service_analytics.jpg"),
    ("Audit + Accounting", "Starting ₹49,999", "service_analytics.jpg"),
    ("Corporate Audit & Accounting", "Starting ₹99,999", "service_analytics.jpg")
]

# Generate the single grid
grid_html = ""
for i, (title, price, img) in enumerate(all_services):
    index = i + 1
    grid_html += f'''                    <a href="#" class="service-card" data-index="{index}">
                        <span class="service-number">{index:02d}</span>
                        <h3 class="service-title">{title}</h3>
                        <div class="service-price-block">
                            <span class="price-label">PRICE</span>
                            <span class="price-value">{price}</span>
                        </div>
                        <div class="service-hover-image">
                            <img src="assets/ai_images/{img}" alt="{title}">
                        </div>
                    </a>\n'''

# Construct the single section matching exactly the OM-Buildings layout
new_services_section = f'''        <!-- SERVICES -->
        <section id="services" class="section-gray">
            <div class="container">
                <span class="eyebrow">OUR ARTIFICIAL INTELLIGENCE SERVICES</span>
                <h2 class="section-title">Intelligence Excellence. Built on Trust.</h2>
                <p class="section-subtitle">We deliver comprehensive AI and machine learning solutions, prioritizing
                    accuracy, scalability, and precision from concept to completion.</p>
                
                <div class="services-grid">
{grid_html}                </div>
            </div>
        </section>'''

# Replace the three sections created previously with this single section
pattern = r'<!-- SERVICES - WEBSITE DESIGN -->.*?</section>\s*<!-- SERVICES - DATA & AI -->.*?</section>\s*<!-- SERVICES - ACCOUNTING -->.*?</section>'
content = re.sub(pattern, new_services_section, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
