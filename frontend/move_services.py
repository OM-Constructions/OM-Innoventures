import re

# Read services.html
with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

# Extract from <!-- SERVICES - WEBSITE DESIGN --> up to <!-- FOOTER -->
match = re.search(r'(<!-- SERVICES - WEBSITE DESIGN -->.*?)<!-- FOOTER -->', services_content, re.DOTALL)
if not match:
    # Maybe up to </main> ?
    match = re.search(r'(<!-- SERVICES - WEBSITE DESIGN -->.*?)</main>', services_content, re.DOTALL)
    if not match:
        print("Could not find services block in services.html")
        exit(1)

extracted_services_html = match.group(1).strip()

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# In index.html, we replace from <!-- SERVICES --> to <!-- ENGINEERING CAPABILITIES -->
index_match = re.search(r'(<!-- SERVICES -->.*?)(<!-- ENGINEERING CAPABILITIES -->)', index_content, re.DOTALL)
if not index_match:
    print("Could not find services block in index.html")
    exit(1)

# Replace
wrapped_services = f'<!-- SERVICES -->\n<div id="services">\n{extracted_services_html}\n</div>\n\n'
new_index_content = index_content.replace(index_match.group(1), wrapped_services)

# Update nav links in index.html to point to #services instead of services.html
new_index_content = new_index_content.replace('href="services.html"', 'href="#services"')
new_index_content = new_index_content.replace("href='services.html'", "href='#services'")

# Some internal scripts in index.html might also point to services.html
# e.g., location.href = "services.html"
new_index_content = new_index_content.replace('services.html', '#services')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_content)

print("Successfully merged services into index.html")
