import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find blocks that look like this:
# <a href="#" class="service-card reveal-card" data-index="1" >
#     <span class="service-number">01</span>
#     <h3 class="service-title">1-page Landing Page</h3>
#
# And replace href="#" with href="services/slug/index.html"

def slugify(title):
    # This needs to match the exact slugs in the services array
    # e.g., "1-page Landing Page" -> "1-page-landing-page"
    # "Data Analytics & BI" -> "data-analytics-bi"
    
    slug = title.lower()
    slug = slug.replace(' & ', '-')
    slug = slug.replace(' / ', '-')
    slug = slug.replace('/', '')
    slug = slug.replace(' ', '-')
    slug = slug.replace('+', '')
    
    # Custom mapping for known inconsistencies
    if "business-contactenquiry" in slug:
        return "business-contactenquiry-forms"
    if "business-data" in slug:
        return "businessdata-analytics"
    
    # Just a general clean up
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    return slug

pattern = re.compile(r'(<a href=")#[^"]*(" class="service-card[^>]*>.*?<h3 class="service-title">)(.*?)(</h3>)', re.DOTALL)

def replace_link(match):
    title = match.group(3)
    slug = slugify(title)
    
    # Specific known mappings to match existing directories
    mapping = {
        "1-page-landing-page": "1-page-landing-page",
        "3-5-page-business-website": "3-5-page-business-website",
        "5-8-page-professional-website": "5-8-page-professional-website",
        "business-contactenquiry-forms": "business-contactenquiry-forms",
        "dynamic-business-website": "dynamic-business-website",
        "e-commerce-website": "e-commerce-website",
        "advanced-e-commerce": "advanced-e-commerce",
        "custom-web-application": "custom-web-application",
        "ai-powered-website": "ai-powered-website",
        "ai-web-application": "ai-web-application",
        "custom-saasweb-platform": "custom-saasweb-platform",
        "excel-data-cleaning": "excel-data-cleaning",
        "excel-data-analysis": "excel-data-analysis",
        "excel-automation": "excel-automation",
        "sql-data-analysis": "sql-data-analysis",
        "power-bi-dashboard": "power-bi-dashboard",
        "advanced-power-bi-dashboard": "advanced-power-bi-dashboard",
        "python-data-analysis": "python-data-analysis",
        "python-sql-analytics": "python-sql-analytics",
        "businessdata-analytics": "businessdata-analytics",
        "sales-analytics": "sales-analytics",
        "hr-analytics": "hr-analytics",
        "financial-analytics": "financial-analytics",
        "-analytics": "-analytics",
        "predictive-analytics": "predictive-analytics",
        "machine-learning-model": "machine-learning-model",
        "advanced-ml-project": "advanced-ml-project",
        "ml-api-deployment": "ml-api-deployment",
        "ai-chatbot": "ai-chatbot",
        "airag-knowledge-assistant": "airag-knowledge-assistant",
        "ai-business-automation": "ai-business-automation",
        "ai-ml-custom-solution": "ai-ml-custom-solution",
        "custom-dataai-software": "custom-dataai-software",
        "data-analytics-bi": "data-analytics-bi",
        "data-science": "data-science",
        "ai-ml-solutions": "ai-ml-solutions",
        "software-development": "software-development",
        "product-development": "product-development",
        "ui-ux-design": "ui-ux-design",
        "graphic-design": "graphic-design",
        "accounting": "accounting",
        "auditing": "auditing",
        "audit-accounting": "audit-accounting",
        "corporate-audit-accounting": "corporate-audit-accounting",
        "finance-accounting": "finance-accounting",
        "auditing-assurance": "auditing-assurance",
        "cybersecurity": "cybersecurity",
        "saas-ai-solutions": "saas-ai-solutions",
    }
    
    # Try to find a match, or just use the slug
    found_slug = slug
    for k in mapping.keys():
        if k in slug or slug in k:
            found_slug = k
            break
            
    # Fix a few edge cases based on known titles
    if "contactenquiry" in slug:
        found_slug = "business-contactenquiry-forms"
    if "business-data" in slug:
        found_slug = "businessdata-analytics"
        
    return match.group(1) + f"services/{found_slug}/index.html" + match.group(2) + title + match.group(4)

new_content = pattern.sub(replace_link, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated links in index.html")
