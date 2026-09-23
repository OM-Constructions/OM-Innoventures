import os
import re

def to_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

content_dict = {
    "1-page Landing Page": {
        "overview": "Our 1-page landing page solutions are hyper-focused on conversion, optimized for speed, and designed to capture leads effectively.",
        "cap_1": ("Conversion Optimization", "Strategic placement of CTAs and clear value propositions to maximize user engagement and lead generation."),
        "cap_2": ("Responsive Design", "Flawless rendering on mobile, tablet, and desktop devices for a seamless user experience."),
        "cap_3": ("Performance Tuning", "Lightning-fast load times through optimized assets and modern web standards."),
        "cap_4": ("Analytics Integration", "Built-in tracking pixels and event monitoring to measure campaign success instantly.")
    },
    "3-5 page Business Website": {
        "overview": "Establish a strong digital footprint with a professional multi-page website that communicates your brand's core offerings and builds trust.",
        "cap_1": ("Brand Identity", "Custom styling aligned with your corporate guidelines to ensure brand consistency."),
        "cap_2": ("Service Showcasing", "Dedicated sections to clearly communicate your value propositions and service details."),
        "cap_3": ("SEO Foundation", "Built with semantic HTML and optimized metadata to improve search engine visibility."),
        "cap_4": ("Content Management", "Easy-to-update structures allowing your team to modify text and images seamlessly.")
    },
    "5-8 page Professional Website": {
        "overview": "A comprehensive digital platform designed for established businesses needing to detail multiple services, team profiles, and detailed portfolios.",
        "cap_1": ("Advanced Architecture", "Logical sitemaps and intuitive navigation for complex content structures."),
        "cap_2": ("Dynamic Portfolios", "Engaging galleries and case study layouts to showcase your past successes."),
        "cap_3": ("Interactive Elements", "Engaging micro-animations and hover states to elevate the user experience."),
        "cap_4": ("Lead Routing", "Advanced contact forms that route inquiries to specific departments automatically.")
    },
    "Business + Contact/Enquiry Forms": {
        "overview": "Maximize your inbound lead capture with customized, secure, and smart enquiry forms integrated directly into a professional business site.",
        "cap_1": ("Form Validation", "Real-time client-side and server-side validation to ensure high-quality data capture."),
        "cap_2": ("Spam Protection", "Integrated CAPTCHA and honeypot techniques to keep your inbox clean."),
        "cap_3": ("CRM Integration", "Automatic routing of submitted data directly into your existing CRM or email platform."),
        "cap_4": ("Custom Workflows", "Multi-step form logic based on user selections to gather precise requirements.")
    },
    "Dynamic Business Website": {
        "overview": "Engage your audience with a website featuring dynamic content, database integrations, and customized user experiences.",
        "cap_1": ("CMS Integration", "Powerful backend systems (like WordPress or Headless CMS) for complete content control."),
        "cap_2": ("User Authentication", "Secure login portals for client-specific dashboards or restricted content access."),
        "cap_3": ("Database Management", "Robust data storage for user profiles, dynamic articles, and inventory."),
        "cap_4": ("API Connectivity", "Seamless integration with third-party services and data providers.")
    },
    "E-commerce Website": {
        "overview": "Launch your online retail presence with a secure, scalable, and conversion-optimized e-commerce platform.",
        "cap_1": ("Product Management", "Intuitive dashboards to manage inventory, variations, and pricing effortlessly."),
        "cap_2": ("Secure Checkout", "PCI-compliant payment gateways integration for safe and smooth transactions."),
        "cap_3": ("Order Tracking", "Automated email notifications and customer dashboards for order status updates."),
        "cap_4": ("Promotional Tools", "Built-in support for discount codes, flash sales, and abandoned cart recovery.")
    },
    "Advanced E-commerce": {
        "overview": "Enterprise-grade retail platforms capable of handling massive SKU counts, complex shipping logic, and multi-vendor integrations.",
        "cap_1": ("ERP Integration", "Real-time synchronization with enterprise resource planning systems."),
        "cap_2": ("Advanced Filtering", "Faceted search and instantaneous filtering for massive product catalogs."),
        "cap_3": ("Multi-currency Support", "Dynamic pricing and localized experiences for global customer bases."),
        "cap_4": ("Performance Scaling", "Cloud-native architecture designed to handle traffic spikes during major sales events.")
    },
    "Custom Web Application": {
        "overview": "Bespoke web software tailored specifically to solve your unique business challenges, built from the ground up for maximum efficiency.",
        "cap_1": ("Custom Architecture", "Scalable backend frameworks and responsive frontend single-page applications."),
        "cap_2": ("Complex Logic", "Implementation of highly specific business rules and proprietary algorithms."),
        "cap_3": ("Security First", "Rigorous security protocols, role-based access control, and data encryption."),
        "cap_4": ("Cloud Deployment", "Automated CI/CD pipelines targeting AWS, Azure, or Google Cloud platforms.")
    },
    "AI-powered Website": {
        "overview": "Future-proof your online presence with integrated artificial intelligence features like smart search, personalization, and automated support.",
        "cap_1": ("Smart Search", "NLP-driven search bars that understand user intent and typos automatically."),
        "cap_2": ("Dynamic Personalization", "Content that adapts in real-time based on user behavior and demographics."),
        "cap_3": ("Automated Assistance", "Integrated AI chatbots to handle common customer inquiries 24/7."),
        "cap_4": ("Predictive Analytics", "Backend insights that forecast user trends and optimize conversion paths.")
    },
    "AI Web Application": {
        "overview": "Complex software applications centered entirely around machine learning models, natural language processing, or computer vision.",
        "cap_1": ("Model Integration", "Seamless deployment of proprietary or pre-trained ML models via API endpoints."),
        "cap_2": ("Real-time Processing", "Optimized pipelines for processing audio, video, or text data instantaneously."),
        "cap_3": ("Data Visualization", "Interactive dashboards that translate complex AI outputs into actionable insights."),
        "cap_4": ("Continuous Learning", "Feedback loops that allow models to improve based on user interaction over time.")
    },
    "Custom SaaS/Web Platform": {
        "overview": "Build the next great Software-as-a-Service product with a multi-tenant architecture designed for subscription billing and massive scale.",
        "cap_1": ("Multi-tenant Architecture", "Secure data isolation and scalable infrastructure for thousands of distinct organizations."),
        "cap_2": ("Subscription Billing", "Complex Stripe integration for tiered pricing, usage-based billing, and prorations."),
        "cap_3": ("User Provisioning", "Advanced role-based access control and organizational team management."),
        "cap_4": ("API Development", "Comprehensive REST or GraphQL APIs for third-party developer integrations.")
    },
    
    # DATA & AI
    "Excel Data Cleaning": {
        "overview": "Transform messy, unstructured spreadsheets into pristine datasets ready for advanced analysis or database import.",
        "cap_1": ("Deduplication", "Advanced algorithms to identify and merge duplicate records accurately."),
        "cap_2": ("Format Standardization", "Consistent formatting of dates, currencies, and text strings across massive files."),
        "cap_3": ("Missing Value Imputation", "Statistical methodologies to estimate and fill in missing data points safely."),
        "cap_4": ("Validation Rules", "Implementation of strict data validation to prevent future corruption.")
    },
    "Excel Data Analysis": {
        "overview": "Extract actionable business insights from your existing spreadsheets using advanced formulas, pivot tables, and statistical functions.",
        "cap_1": ("Complex Formulas", "Utilization of advanced array formulas and lookups to connect disparate data."),
        "cap_2": ("Pivot Table Mastery", "Dynamic summarization of millions of rows into readable, interactive reports."),
        "cap_3": ("Trend Analysis", "Identification of historical patterns and seasonal variations within your data."),
        "cap_4": ("What-if Scenarios", "Scenario manager and goal seek implementations for financial forecasting.")
    },
    "Excel Automation": {
        "overview": "Eliminate hours of manual data entry and reporting with custom VBA macros and advanced Power Query automations.",
        "cap_1": ("VBA Macro Development", "Custom scripts to automate repetitive tasks and interface with other Office apps."),
        "cap_2": ("Power Query Pipelines", "Automated data extraction, transformation, and loading from external sources."),
        "cap_3": ("Automated Reporting", "One-click generation and email distribution of complex weekly or monthly reports."),
        "cap_4": ("Custom UI Forms", "User-friendly input forms built directly into Excel to standardize data entry.")
    },
    "SQL Data Analysis": {
        "overview": "Dive deep into your relational databases to run complex queries, aggregate vast datasets, and uncover hidden business intelligence.",
        "cap_1": ("Complex Querying", "Advanced JOINs, window functions, and subqueries to extract precise metrics."),
        "cap_2": ("Performance Optimization", "Query refactoring and index recommendations for faster execution times."),
        "cap_3": ("Data Aggregation", "Consolidation of massive transactional datasets into analytical summary tables."),
        "cap_4": ("ETL Scripting", "Custom scripts to extract data from operational databases into data warehouses.")
    },
    "Power BI Dashboard": {
        "overview": "Visualize your business performance with interactive, real-time Power BI dashboards connecting to your core data sources.",
        "cap_1": ("Data Modeling", "Creation of robust star-schema data models optimized for filtering and speed."),
        "cap_2": ("Interactive Visuals", "Custom charts, matrices, and maps that allow drill-down analysis."),
        "cap_3": ("DAX Calculations", "Advanced DAX measures for complex business logic, YTD calculations, and ratios."),
        "cap_4": ("Scheduled Refresh", "Automated data synchronization via Power BI Gateway.")
    },
    "Advanced Power BI Dashboard": {
        "overview": "Enterprise-level Power BI implementations featuring row-level security, incremental refresh, and highly customized visual storytelling.",
        "cap_1": ("Row-Level Security", "Dynamic data filtering based on user login to ensure strict data governance."),
        "cap_2": ("Incremental Refresh", "Optimized loading strategies for datasets exceeding tens of millions of rows."),
        "cap_3": ("Custom Visuals", "Implementation of Python/R scripts or third-party visuals for unique requirements."),
        "cap_4": ("Cross-report Drillthrough", "Seamless navigation between high-level summary dashboards and detailed reports.")
    },
    "Python Data Analysis": {
        "overview": "Leverage the power of Python, Pandas, and NumPy to perform complex statistical analysis on datasets too large for traditional spreadsheets.",
        "cap_1": ("Pandas Processing", "High-speed manipulation, merging, and reshaping of gigabyte-sized datasets."),
        "cap_2": ("Statistical Analysis", "Implementation of SciPy and StatsModels for rigorous statistical testing."),
        "cap_3": ("Exploratory Data Analysis", "Comprehensive univariate and bivariate analysis to discover underlying patterns."),
        "cap_4": ("Jupyter Notebooks", "Fully documented analytical processes delivered in interactive notebook formats.")
    },
    "Python + SQL Analytics": {
        "overview": "The ultimate analytical stack. Extract vast amounts of data via SQL and process complex algorithms using Python's scientific libraries.",
        "cap_1": ("Database Connectivity", "Secure integration with PostgreSQL, MySQL, Snowflake, or BigQuery using SQLAlchemy."),
        "cap_2": ("Hybrid Processing", "Optimizing workloads by pushing aggregations to SQL and machine learning to Python."),
        "cap_3": ("Automated Pipelines", "Python scripts that run daily SQL extractions, process insights, and save results."),
        "cap_4": ("Data Warehouse Integration", "Direct integration with modern cloud data warehouses for enterprise scale.")
    },
    "Business/Data Analytics": {
        "overview": "Comprehensive business intelligence consulting focused on defining KPIs, auditing data quality, and aligning analytics with corporate strategy.",
        "cap_1": ("KPI Definition", "Collaborative workshops to define actionable metrics aligned with business goals."),
        "cap_2": ("Data Auditing", "Thorough assessment of existing data collection methods and quality issues."),
        "cap_3": ("Strategy Development", "Creating long-term roadmaps for data maturity and technology adoption."),
        "cap_4": ("Executive Reporting", "High-level summary reports designed specifically for C-suite decision making.")
    },
    "Sales Analytics": {
        "overview": "Optimize your sales funnel, forecast revenue, and evaluate team performance using data-driven insights from your CRM.",
        "cap_1": ("Pipeline Velocity", "Analysis of deal movement speed to identify bottlenecks in the sales process."),
        "cap_2": ("Win/Loss Analysis", "Statistical modeling to determine the key factors that lead to closed deals."),
        "cap_3": ("Revenue Forecasting", "Predictive models estimating future revenue based on historical conversion rates."),
        "cap_4": ("Territory Optimization", "Data-driven alignment of sales reps based on geographical potential and workload.")
    },
    "HR Analytics": {
        "overview": "Transform human resources from an administrative function to a strategic partner through predictive attrition modeling and performance analysis.",
        "cap_1": ("Attrition Prediction", "Machine learning models identifying employees at high risk of leaving."),
        "cap_2": ("Compensation Analysis", "Internal equity and market competitiveness studies using statistical distributions."),
        "cap_3": ("Recruitment Funnel", "Analysis of sourcing channels to determine the highest quality of hire."),
        "cap_4": ("Diversity & Inclusion", "Detailed demographic tracking and pay-gap analysis reporting.")
    },
    "Financial Analytics": {
        "overview": "Deep financial modeling, variance analysis, and cash flow forecasting using advanced statistical techniques.",
        "cap_1": ("Variance Analysis", "Automated breakdown of budget vs. actual performance drivers."),
        "cap_2": ("Cash Flow Forecasting", "Rolling predictive models for working capital optimization."),
        "cap_3": ("Profitability Analysis", "Deep dives into product, customer, or channel profitability margins."),
        "cap_4": ("Risk Modeling", "Monte Carlo simulations to assess financial risk under uncertain economic conditions.")
    },
    " Analytics": {
        "overview": "Specialized data solutions for the built environment, analyzing project costs, equipment utilization, and schedule variances.",
        "cap_1": ("Earned Value Management", "Advanced tracking of project progress against cost and schedule baselines."),
        "cap_2": ("Equipment Utilization", "Telematics data analysis to optimize fleet deployment and maintenance schedules."),
        "cap_3": ("Supply Chain Analytics", "Predictive modeling for material cost fluctuations and delivery delays."),
        "cap_4": ("Safety Analytics", "Statistical analysis of near-misses to predict and prevent future incidents.")
    },
    "Predictive Analytics": {
        "overview": "Move beyond looking at the past. Utilize statistical modeling to forecast future trends, customer behaviors, and market shifts.",
        "cap_1": ("Time Series Forecasting", "ARIMA and Prophet models for highly accurate seasonal demand planning."),
        "cap_2": ("Customer Churn", "Classification models predicting exactly which clients are likely to cancel services."),
        "cap_3": ("Lead Scoring", "Algorithmic ranking of prospects based on their statistical likelihood to convert."),
        "cap_4": ("Inventory Optimization", "Predicting optimal stock levels to prevent stockouts while minimizing holding costs.")
    },
    "Machine Learning Model": {
        "overview": "Custom-trained machine learning algorithms designed to solve specific classification, regression, or clustering problems for your business.",
        "cap_1": ("Feature Engineering", "Expert transformation of raw data into powerful predictive variables."),
        "cap_2": ("Algorithm Selection", "Rigorous testing of Random Forests, Gradient Boosting, and SVMs for optimal accuracy."),
        "cap_3": ("Hyperparameter Tuning", "Grid search optimization to squeeze maximum performance from the model."),
        "cap_4": ("Model Evaluation", "Comprehensive validation using cross-validation, ROC curves, and confusion matrices.")
    },
    "Advanced ML Project": {
        "overview": "Complex, multi-stage machine learning pipelines utilizing ensemble methods and deep learning for highly nuanced problem spaces.",
        "cap_1": ("Deep Learning", "Implementation of neural networks using TensorFlow or PyTorch for unstructured data."),
        "cap_2": ("Ensemble Architectures", "Combining multiple independent models to drastically reduce variance and error."),
        "cap_3": ("Anomaly Detection", "Unsupervised learning techniques for fraud detection and system monitoring."),
        "cap_4": ("Optimization Algorithms", "Genetic algorithms and simulated annealing for complex resource allocation problems.")
    },
    "ML + API Deployment": {
        "overview": "Bridge the gap between data science and software engineering by deploying your trained models as scalable, secure REST APIs.",
        "cap_1": ("Containerization", "Packaging models via Docker for completely reproducible deployment environments."),
        "cap_2": ("API Architecture", "Building robust FastAPI or Flask endpoints for sub-millisecond model inference."),
        "cap_3": ("Load Balancing", "Configuring cloud infrastructure to handle massive spikes in prediction requests."),
        "cap_4": ("Model Monitoring", "Tracking data drift and prediction accuracy degradation in production environments.")
    },
    "AI Chatbot": {
        "overview": "Intelligent conversational agents capable of understanding context, handling complex customer service workflows, and integrating with your CRM.",
        "cap_1": ("Intent Recognition", "Advanced Natural Language Understanding (NLU) to correctly route user queries."),
        "cap_2": ("Multi-turn Conversations", "Context-aware dialog management that remembers previous user inputs."),
        "cap_3": ("System Integration", "Connecting the bot to Zendesk, Salesforce, or custom internal databases via API."),
        "cap_4": ("Human Handoff", "Seamless transfer to live agents when confidence scores fall below acceptable thresholds.")
    },
    "AI/RAG Knowledge Assistant": {
        "overview": "Empower your team with a Retrieval-Augmented Generation (RAG) assistant that can instantly query and summarize your proprietary documents securely.",
        "cap_1": ("Vector Embeddings", "Converting your PDFs, manuals, and databases into high-dimensional vector space."),
        "cap_2": ("Semantic Search", "Retrieving highly relevant contextual information using cosine similarity."),
        "cap_3": ("LLM Integration", "Feeding retrieved context to GPT-4 or Claude for accurate, hallucination-free answers."),
        "cap_4": ("Strict Data Privacy", "Deploying open-source LLMs locally to guarantee your data never leaves your servers.")
    },
    "AI Business Automation": {
        "overview": "Revolutionize your operational efficiency by replacing manual, repetitive workflows with intelligent, autonomous AI agents.",
        "cap_1": ("Document Extraction", "Using OCR and LLMs to automatically parse invoices, receipts, and contracts."),
        "cap_2": ("Email Triage", "AI models that read, categorize, and draft responses to incoming support tickets."),
        "cap_3": ("Agentic Workflows", "Deploying LangChain agents capable of making decisions and using software tools."),
        "cap_4": ("RPA Integration", "Combining AI decision making with traditional Robotic Process Automation (RPA) bots.")
    },
    "AI + ML Custom Solution": {
        "overview": "A completely bespoke AI architecture designed from the ground up to solve your industry's most complex, previously unsolvable challenges.",
        "cap_1": ("Feasibility Studies", "Rigorous initial R&D phases to determine technical viability before massive investment."),
        "cap_2": ("Custom Architecture", "Designing novel neural network topologies specific to your data type."),
        "cap_3": ("Proprietary Data Moats", "Strategies for continuous data collection to maintain a competitive AI advantage."),
        "cap_4": ("End-to-End Delivery", "Full lifecycle management from data pipeline creation to cloud infrastructure deployment.")
    },
    "Custom Data/AI Software": {
        "overview": "The ultimate enterprise solution: a fully functional web application seamlessly wrapped around a core of proprietary machine learning and AI technology.",
        "cap_1": ("Full-Stack Integration", "Seamless marriage of React/Next.js frontends with Python/PyTorch backends."),
        "cap_2": ("Real-time Inference", "Streaming architectures utilizing Kafka for instantaneous AI processing."),
        "cap_3": ("Enterprise Security", "SOC2-compliant architectures ensuring absolute protection of sensitive training data."),
        "cap_4": ("Scalable Infrastructure", "Kubernetes-orchestrated deployments ensuring massive scalability under load.")
    },

    # ACCOUNTING
    "Accounting": {
        "overview": "Comprehensive, precise, and compliant accounting services tailored to streamline your financial operations and provide crystal-clear visibility.",
        "cap_1": ("Bookkeeping", "Accurate daily transaction recording and strict ledger maintenance."),
        "cap_2": ("Financial Statements", "Preparation of GAAP/IFRS compliant balance sheets and income statements."),
        "cap_3": ("Payroll Processing", "Automated, compliant payroll management and tax withholding calculations."),
        "cap_4": ("Reconciliation", "Rigorous monthly bank and credit card reconciliation to prevent discrepancies.")
    },
    "Auditing": {
        "overview": "Independent, objective assurance and consulting services designed to add value, improve operations, and guarantee regulatory compliance.",
        "cap_1": ("Internal Controls", "Thorough evaluation of existing financial controls to identify vulnerabilities."),
        "cap_2": ("Compliance Audits", "Ensuring strict adherence to local, state, and federal financial regulations."),
        "cap_3": ("Risk Assessment", "Identification and mitigation strategies for enterprise financial risks."),
        "cap_4": ("Actionable Reporting", "Detailed management letters outlining specific areas for operational improvement.")
    },
    "Audit + Accounting": {
        "overview": "A holistic financial package combining meticulous day-to-day accounting management with rigorous periodic internal auditing.",
        "cap_1": ("End-to-End Management", "Seamless transition between daily bookkeeping and annual audit preparation."),
        "cap_2": ("Continuous Auditing", "Real-time anomaly detection integrated directly into your accounting workflows."),
        "cap_3": ("Tax Strategy", "Proactive tax planning based on real-time, audited financial data."),
        "cap_4": ("Board Presentations", "Professional, verified financial presentations prepared for investors and boards.")
    },
    "Corporate Audit & Accounting": {
        "overview": "Enterprise-tier financial services designed for massive scale, complex subsidiary structures, and stringent international compliance requirements.",
        "cap_1": ("Consolidated Financials", "Complex aggregation of multi-entity, multi-currency corporate structures."),
        "cap_2": ("Forensic Accounting", "Deep investigative auditing for dispute resolution and fraud detection."),
        "cap_3": ("Mergers & Acquisitions", "Rigorous financial due diligence for corporate restructuring and buyouts."),
        "cap_4": ("SOX Compliance", "Comprehensive testing and documentation for Sarbanes-Oxley requirements.")
    }
}

base_dir = "/home/dilli/OM -AI/frontend/services"

for service_name, content in content_dict.items():
    slug = to_slug(service_name)
    file_path = os.path.join(base_dir, slug, "index.html")
    
    if not os.path.exists(file_path):
        print(f"Skipping {service_name}, file not found: {file_path}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace Overview
    # The current overview looks like this:
    # <span class="sp-label">01 &mdash; OVERVIEW</span>
    # <p>At OM Innoventures, we believe that exceptional software begins with a deep understanding of your business purpose. Our ...</p>
    
    overview_pattern = r'(<span class="sp-label">01 &mdash; OVERVIEW</span>\s*)<p>.*?</p>'
    html = re.sub(overview_pattern, r'\1<p>' + content['overview'] + r'</p>', html, flags=re.DOTALL)
    
    # Replace Capabilities
    # The current capabilities look like this:
    # <div class="sp-focus-item">
    #     <h3>Strategy & Planning</h3>
    #     <p>Providing exact, professional outcomes focused on practical value and precision.</p>
    # </div>
    
    # We will find all sp-focus-item blocks and replace them sequentially.
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
        
print("Successfully updated content for all 37 services.")
