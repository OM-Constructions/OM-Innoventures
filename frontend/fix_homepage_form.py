import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the location field
content = content.replace(
    '<label for="ge-location">Project Location (optional)</label>',
    '<label for="ge-location">Company Website (optional)</label>'
)
content = content.replace(
    'placeholder="City, Area or State (e.g. Bangalore)"',
    'placeholder="https://www.yourcompany.com"'
)

# Replace the built-up area field
content = content.replace(
    '<label for="ge-area">Approx. Built-up Area / Type (optional)</label>',
    '<label for="ge-area">Estimated Budget (optional)</label>'
)
content = content.replace(
    'placeholder="e.g. 2,500 sq ft, 3BHK Villa, G+2 Commercial"',
    'placeholder="e.g. $5k-$10k, Flexible"'
)

# Replace the textarea placeholder
content = content.replace(
    'placeholder="Describe what you want to build: building type, specific requirements, timeline, budget expectations, or any questions for our engineers..."',
    'placeholder="Describe what you want to build: business goals, specific software requirements, timeline, or any questions for our engineering team..."'
)

# Replace the select options
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

options_html = '<option value="general-inquiry">General Consultation & Strategy</option>\n'
for s in services:
    name = s.replace('-', ' ').title()
    options_html += f'                                        <option value="{s}">{name}</option>\n'

# Use regex to replace the options inside the select
pattern = re.compile(r'(<select id="ge-service"[^>]*>).*?(</select>)', re.DOTALL)
content = pattern.sub(r'\1\n' + options_html + r'                                    \2', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html form fields and dropdown")
