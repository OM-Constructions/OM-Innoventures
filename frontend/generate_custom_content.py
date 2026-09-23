import os
import re

content_dict = {
    # WEBSITES
    "1-page-landing-page": {
        "overview": "A highly focused, high-converting 1-page landing page designed specifically to turn your visitors into qualified leads. We strip away distractions and focus entirely on your core value proposition and a strong Call to Action (CTA).",
        "cap_1": ("Conversion Optimization", "Strategic placement of CTAs, compelling headlines, and trust signals to maximize lead capture."),
        "cap_2": ("Lightning Fast Load Times", "Optimized assets and streamlined code ensure your page loads instantly, reducing bounce rates."),
        "cap_3": ("Responsive Design", "Flawless rendering and user experience across all devices, from mobile phones to ultra-wide desktop monitors."),
        "cap_4": ("Analytics Integration", "Seamless integration with Google Analytics, Facebook Pixel, and other tracking tools to monitor performance.")
    },
    "3-5-page-business-website": {
        "overview": "Establish a strong, professional online presence with a multi-page business website. Perfect for small to medium businesses needing to showcase their services, about us, and contact information with a polished digital footprint.",
        "cap_1": ("Custom Brand Alignment", "Design that perfectly reflects your corporate identity, utilizing your logos, colors, and typography."),
        "cap_2": ("Service Showcase", "Dedicated pages to deeply explain your offerings, complete with imagery and detailed descriptions."),
        "cap_3": ("SEO Foundations", "Built-in on-page SEO best practices to ensure your business can be easily found on search engines."),
        "cap_4": ("Secure Hosting Setup", "Deployment on secure, reliable infrastructure with SSL certificates to protect user data.")
    },
    "5-8-page-professional-website": {
        "overview": "A comprehensive digital platform for established professionals and businesses. This extensive website allows for deep dives into multiple service lines, team profiles, portfolios, and rich multimedia content.",
        "cap_1": ("Information Architecture", "Strategic structuring of content to ensure users can intuitively navigate through complex information."),
        "cap_2": ("Dynamic Portfolios", "Interactive galleries and case study sections to showcase your past work and success stories."),
        "cap_3": ("Advanced Contact Routing", "Custom forms that route inquiries to different departments based on user selection."),
        "cap_4": ("CMS Integration", "Easy-to-use Content Management System allowing your team to update text and images independently.")
    },
    "business-contactenquiry-forms": {
        "overview": "Streamline your lead generation with advanced, conditional logic contact and enquiry forms. We build intelligent data capture systems that integrate directly into your CRM or email marketing software.",
        "cap_1": ("Conditional Logic", "Smart forms that change questions based on previous answers, providing a personalized user experience."),
        "cap_2": ("CRM Integration", "Automatic routing of captured data into Salesforce, HubSpot, or your custom database."),
        "cap_3": ("Spam Protection", "Advanced, invisible reCAPTCHA and honeypot techniques to ensure you only receive legitimate leads."),
        "cap_4": ("Multi-step Forms", "Breaking down complex data requests into digestible, high-converting multi-step processes.")
    },
    "dynamic-business-website": {
        "overview": "A website that adapts to your users. We build dynamic, database-driven business websites that can display personalized content, manage user accounts, and update in real-time without manual intervention.",
        "cap_1": ("Database Architecture", "Robust SQL or NoSQL databases structuring your business data for rapid retrieval and display."),
        "cap_2": ("User Authentication", "Secure login portals allowing clients or employees to access restricted, personalized content."),
        "cap_3": ("Dynamic Content Rendering", "Pages generated on-the-fly based on user interaction, search queries, or real-time data feeds."),
        "cap_4": ("Admin Dashboards", "Custom administrative interfaces to manage users, content, and site settings effortlessly.")
    },
    "e-commerce-website": {
        "overview": "Launch your digital storefront with a robust, scalable E-commerce website. We handle everything from product catalogs and shopping carts to secure payment gateways and inventory management systems.",
        "cap_1": ("Secure Payment Processing", "Integration with Stripe, PayPal, Razorpay, and other major gateways with PCI compliance."),
        "cap_2": ("Inventory Management", "Real-time stock tracking, low-inventory alerts, and automated SKU management."),
        "cap_3": ("Optimized Checkout Flow", "Frictionless, one-page or multi-step checkout processes designed to minimize cart abandonment."),
        "cap_4": ("Product Search & Filtering", "Advanced search algorithms and faceted navigation to help users find exactly what they want.")
    },
    "advanced-e-commerce": {
        "overview": "Enterprise-grade E-commerce solutions for high-volume retailers. Featuring multi-vendor capabilities, complex pricing algorithms, personalized product recommendations, and deep ERP integrations.",
        "cap_1": ("AI Product Recommendations", "Machine learning algorithms that suggest products based on user browsing history and purchase patterns."),
        "cap_2": ("Multi-Vendor Architecture", "Marketplace capabilities allowing third-party sellers to manage their own products and orders."),
        "cap_3": ("ERP & Logistics Integration", "Seamless connection with your backend inventory, shipping providers, and accounting software."),
        "cap_4": ("High-Traffic Scalability", "Cloud-native architecture designed to handle massive traffic spikes during sales and holiday seasons.")
    },
    "custom-web-application": {
        "overview": "Transform your complex business logic into a sleek, accessible custom web application. We build highly interactive, responsive applications that function like native software directly in the browser.",
        "cap_1": ("Single Page Applications", "React, Vue, or Angular frontends providing instant, page-refresh-free user experiences."),
        "cap_2": ("Microservices Backend", "Scalable backend architecture allowing independent development and deployment of different features."),
        "cap_3": ("Real-Time Data Sync", "WebSockets and server-sent events for live updates, chat features, and collaborative tools."),
        "cap_4": ("Cross-Platform Compatibility", "Progressive Web App (PWA) capabilities allowing installation on mobile and offline functionality.")
    },
    "ai-powered-website": {
        "overview": "Next-generation websites that utilize Artificial Intelligence to adapt, personalize, and optimize the user journey. From dynamic content generation to smart search, your website becomes an active participant in sales.",
        "cap_1": ("Dynamic Personalization", "AI algorithms that alter page layouts, messaging, and offers based on individual visitor behavior."),
        "cap_2": ("Smart Search Capabilities", "NLP-powered search bars that understand context and typos to deliver exact results."),
        "cap_3": ("Automated Content Tagging", "Computer vision and NLP automatically categorize and tag uploaded images and text."),
        "cap_4": ("Predictive Lead Scoring", "Background algorithms that score visitor engagement to alert sales teams of high-intent prospects.")
    },
    "ai-web-application": {
        "overview": "Deeply integrated Artificial Intelligence applications built into robust web platforms. We create tools capable of complex data analysis, generative content, and automated decision-making natively in the browser.",
        "cap_1": ("LLM Integration", "Connecting your application to OpenAI, Claude, or custom LLMs for generative text features."),
        "cap_2": ("Data Processing Pipelines", "Frontend interfaces controlling complex, heavy backend machine learning operations."),
        "cap_3": ("Interactive Data Visualizations", "D3.js and WebGL rendering complex AI outputs into understandable, actionable charts and graphs."),
        "cap_4": ("Agentic Workflows", "Multi-agent AI systems that can execute complex, multi-step tasks initiated by the user.")
    },
    "custom-saasweb-platform": {
        "overview": "End-to-end development of Software as a Service (SaaS) platforms. We architect secure, multi-tenant environments with robust subscription billing, user role management, and scalable cloud infrastructure.",
        "cap_1": ("Multi-Tenant Architecture", "Secure data isolation while maintaining a single, easily updatable codebase for all clients."),
        "cap_2": ("Subscription Billing & Usage Tracking", "Complex integrations with Stripe Billing to handle tiered plans, metered usage, and prorations."),
        "cap_3": ("Role-Based Access Control", "Granular permission systems allowing your clients to manage their own teams and data access."),
        "cap_4": ("Automated Provisioning", "Zero-touch onboarding pipelines that automatically spin up resources for new paying customers.")
    },
    
    # DATA & AI
    "excel-data-cleaning": {
        "overview": "Transform messy, unstructured spreadsheets into pristine, analyzable datasets. We use advanced macros, Power Query, and custom scripts to remove duplicates, standardize formats, and handle missing values.",
        "cap_1": ("Data Standardization", "Uniform formatting of dates, text casing, addresses, and numerical values across massive sheets."),
        "cap_2": ("Deduplication & Merging", "Fuzzy matching algorithms to identify and merge duplicate records accurately."),
        "cap_3": ("Error Identification", "Automated flagging of outliers, illogical data points, and formatting inconsistencies."),
        "cap_4": ("Power Query Pipelines", "Building repeatable ETL processes directly in Excel so future data drops are cleaned instantly.")
    },
    "excel-data-analysis": {
        "overview": "Extract actionable business intelligence from your spreadsheets. We utilize advanced formulas, complex pivot tables, and statistical functions to turn raw numbers into clear strategic insights.",
        "cap_1": ("Advanced Pivot Tables", "Multi-dimensional data summarization providing quick answers to complex business questions."),
        "cap_2": ("Complex Formulas", "Mastery of INDEX/MATCH, array formulas, and dynamic logic to automate calculations."),
        "cap_3": ("Trend & Variance Analysis", "Identifying historical patterns and highlighting deviations from expected financial or operational metrics."),
        "cap_4": ("Custom Dashboards", "Creating interactive, visually appealing executive dashboards directly within Excel.")
    },
    "excel-automation": {
        "overview": "Eliminate hours of manual data entry and repetitive tasks. We develop robust VBA macros and Office Scripts to automate your entire Excel workflow, from data import to final report generation.",
        "cap_1": ("VBA Macro Development", "Custom programming to automate highly specific, multi-step spreadsheet tasks."),
        "cap_2": ("Automated Reporting", "Scripts that automatically generate, format, and email daily or weekly PDF reports."),
        "cap_3": ("External Data Integration", "Macros that pull live data from external APIs, SQL databases, or web scraping."),
        "cap_4": ("Custom Ribbon Interfaces", "Building user-friendly buttons and menus so your team can run complex automations easily.")
    },
    "sql-data-analysis": {
        "overview": "Deep dive into your relational databases to extract powerful insights. We write complex, highly optimized SQL queries to join disparate tables, aggregate massive datasets, and answer critical business questions.",
        "cap_1": ("Complex Query Development", "Advanced use of window functions, CTEs, and multi-level joins to extract precise data points."),
        "cap_2": ("Query Optimization", "Refactoring slow, inefficient queries to run exponentially faster and reduce server load."),
        "cap_3": ("Data Warehousing Support", "Designing schemas and views to make data more accessible for Business Intelligence tools."),
        "cap_4": ("Ad-Hoc Reporting", "Rapid turnaround on complex, custom data requests from executive and operational teams.")
    },
    "power-bi-dashboard": {
        "overview": "Bring your data to life with interactive, visually stunning Power BI dashboards. We connect your data sources, build robust data models, and design intuitive interfaces that empower your team to make decisions.",
        "cap_1": ("Data Modeling (DAX)", "Creating complex calculated measures and columns to define your unique business metrics."),
        "cap_2": ("Interactive Visualizations", "Designing intuitive charts, maps, and matrices that allow users to drill down into the details."),
        "cap_3": ("Automated Data Refresh", "Setting up gateways to ensure your dashboards always display up-to-the-minute information."),
        "cap_4": ("Row-Level Security", "Implementing access controls so managers only see data relevant to their specific departments.")
    },
    "advanced-power-bi-dashboard": {
        "overview": "Enterprise-level Business Intelligence solutions. We integrate massive, multi-source datasets, utilize advanced DAX for predictive modeling, and embed custom visual capabilities into highly sophisticated dashboards.",
        "cap_1": ("Multi-Source Integration", "Seamlessly blending data from SQL, APIs, Salesforce, and flat files into a single cohesive model."),
        "cap_2": ("Advanced DAX & Time Intelligence", "Complex calculations for YTD growth, moving averages, and dynamic forecasting."),
        "cap_3": ("Embedded Analytics", "Integrating Power BI reports directly into your custom web applications or corporate portals."),
        "cap_4": ("Performance Tuning", "Optimizing massive data models to ensure dashboards load and filter instantly.")
    },
    "python-data-analysis": {
        "overview": "Leverage the power of Python (Pandas, NumPy) to analyze datasets too large or complex for traditional spreadsheet software. We conduct deep statistical analysis and uncover hidden correlations.",
        "cap_1": ("Exploratory Data Analysis", "Comprehensive statistical profiling and visualization using Matplotlib and Seaborn."),
        "cap_2": ("Big Data Handling", "Processing datasets with millions of rows efficiently using optimized Pandas operations or Dask."),
        "cap_3": ("Time Series Analysis", "Advanced techniques to analyze trends, seasonality, and cyclic patterns in chronological data."),
        "cap_4": ("Statistical Hypothesis Testing", "Rigorous A/B testing and statistical validation of business assumptions.")
    },
    "python-sql-analytics": {
        "overview": "The ultimate combination of data extraction and advanced analysis. We write highly efficient SQL to extract targeted data, then use Python to perform complex machine learning and statistical modeling.",
        "cap_1": ("ETL Pipeline Development", "Automated Python scripts that extract data from SQL databases, transform it, and load it into analytical tools."),
        "cap_2": ("Advanced Aggregation", "Using SQL for heavy lifting and Python for intricate statistical manipulations."),
        "cap_3": ("Predictive Modeling Integration", "Feeding clean SQL data directly into Scikit-Learn models for predictive analytics."),
        "cap_4": ("Automated Reporting Systems", "Python scripts that query databases and automatically generate and distribute PDF/HTML reports.")
    },
    "businessdata-analytics": {
        "overview": "Strategic analytics focused entirely on driving business growth. We translate complex data into actionable business strategies, focusing on KPIs, ROI, customer acquisition costs, and operational efficiency.",
        "cap_1": ("KPI Definition & Tracking", "Working with executives to define and monitor the metrics that actually matter to your bottom line."),
        "cap_2": ("Customer Segmentation", "Analyzing behavioral data to group customers for targeted marketing and product development."),
        "cap_3": ("Churn Prediction", "Identifying the leading indicators of customer cancellation to enable proactive retention strategies."),
        "cap_4": ("Operational Bottleneck Analysis", "Using process data to identify inefficiencies and recommend strategic improvements.")
    },
    "sales-analytics": {
        "overview": "Supercharge your sales team with data-driven insights. We analyze CRM data, pipeline velocity, and rep performance to accurately forecast revenue and optimize the entire sales process.",
        "cap_1": ("Pipeline Velocity Analysis", "Identifying where deals get stuck and calculating the true conversion rates between sales stages."),
        "cap_2": ("Sales Forecasting", "Accurate, data-driven revenue predictions based on historical win rates and current pipeline volume."),
        "cap_3": ("Rep Performance Scorecards", "Objective, metric-driven dashboards evaluating individual sales representative efficiency."),
        "cap_4": ("Win/Loss Analysis", "Statistical evaluation of why deals are won or lost against specific competitors.")
    },
    "hr-analytics": {
        "overview": "Optimize your workforce with People Analytics. We analyze recruitment data, employee engagement surveys, and turnover rates to help you attract, retain, and develop top talent.",
        "cap_1": ("Turnover & Retention Modeling", "Predictive analytics identifying departments or roles at high risk of employee flight."),
        "cap_2": ("Recruitment Funnel Optimization", "Analyzing time-to-hire and source-of-hire data to improve recruiting efficiency."),
        "cap_3": ("Compensation Analysis", "Statistical benchmarking to ensure internal equity and external market competitiveness."),
        "cap_4": ("Employee Sentiment Analysis", "NLP analysis of employee surveys and feedback to gauge overall company morale.")
    },
    "financial-analytics": {
        "overview": "Deep financial modeling and quantitative analysis to ensure your company's fiscal health. We provide cash flow forecasting, profitability analysis, and rigorous scenario planning.",
        "cap_1": ("Cash Flow Forecasting", "Dynamic models predicting future liquidity based on historical trends and payable/receivable schedules."),
        "cap_2": ("Profitability by Segment", "Granular analysis breaking down margins by product line, customer demographic, or geographic region."),
        "cap_3": ("Scenario Modeling (Monte Carlo)", "Simulating thousands of economic scenarios to stress-test your financial stability."),
        "cap_4": ("Working Capital Optimization", "Data-driven strategies to improve inventory turnover and optimize accounts receivable.")
    },
    "-analytics": {
        "overview": "Specialized data solutions for the  industry. We analyze project timelines, budget variances, resource allocation, and safety records to ensure your projects finish on time and under budget.",
        "cap_1": ("Budget Variance Tracking", "Real-time comparison of estimated vs. actual costs across materials, labor, and equipment."),
        "cap_2": ("Schedule Optimization", "Critical path analysis to identify potential delays before they impact the final delivery date."),
        "cap_3": ("Resource Allocation Forecasting", "Predicting equipment and labor needs across multiple concurrent project sites."),
        "cap_4": ("Safety & Risk Analytics", "Analyzing incident reports to identify risk factors and proactively improve site safety protocols.")
    },
    "predictive-analytics": {
        "overview": "Stop reacting to the past and start anticipating the future. We build sophisticated statistical models that forecast customer behavior, market trends, and operational demands with high accuracy.",
        "cap_1": ("Demand Forecasting", "Predicting future sales volumes to optimize inventory, staffing, and supply chain logistics."),
        "cap_2": ("Customer Lifetime Value (CLV)", "Projecting the long-term revenue potential of newly acquired customer cohorts."),
        "cap_3": ("Risk Scoring", "Algorithmic evaluation of credit risk, fraud probability, or equipment failure likelihood."),
        "cap_4": ("Price Elasticity Modeling", "Determining the optimal price points to maximize total revenue or market share.")
    },
    "machine-learning-model": {
        "overview": "Custom Machine Learning solutions tailored to your unique data. We design, train, and validate supervised and unsupervised models capable of making complex, automated decisions.",
        "cap_1": ("Algorithm Selection", "Strategic choice between Random Forests, Gradient Boosting, SVMs, or Neural Networks based on your data."),
        "cap_2": ("Feature Engineering", "Extracting and transforming raw variables into powerful predictive signals."),
        "cap_3": ("Model Validation", "Rigorous cross-validation and hyperparameter tuning to ensure maximum accuracy and prevent overfitting."),
        "cap_4": ("Explainable AI (XAI)", "Using SHAP values and LIME to ensure model decisions are transparent and understandable to humans.")
    },
    "advanced-ml-project": {
        "overview": "Complex, multi-layered Artificial Intelligence projects solving highly specific enterprise challenges. This includes deep learning architectures, reinforcement learning, and massive-scale data processing.",
        "cap_1": ("Deep Learning Architectures", "Custom Neural Networks utilizing PyTorch or TensorFlow for complex pattern recognition."),
        "cap_2": ("Reinforcement Learning", "Developing intelligent agents that learn optimal strategies through trial and error environments."),
        "cap_3": ("Distributed Training", "Utilizing cloud GPU clusters to train massive models on terabytes of unstructured data."),
        "cap_4": ("Continuous Learning Systems", "Architectures that automatically retrain and update themselves as new data flows in.")
    },
    "ml-api-deployment": {
        "overview": "Take your models out of the lab and into production. We specialize in MLOps, deploying your trained machine learning models as scalable, highly available REST or gRPC APIs.",
        "cap_1": ("Containerization (Docker)", "Packaging models and dependencies into isolated containers for reliable execution across environments."),
        "cap_2": ("Cloud Deployment", "Setting up scalable infrastructure on AWS SageMaker, GCP Vertex AI, or Azure ML."),
        "cap_3": ("Low-Latency Inference", "Optimizing models and API architecture to return predictions in milliseconds."),
        "cap_4": ("Model Monitoring", "Implementing dashboards to track API latency, error rates, and model drift over time.")
    },
    "ai-chatbot": {
        "overview": "Intelligent, context-aware conversational agents capable of handling complex customer service workflows, lead qualification, and internal knowledge retrieval 24/7.",
        "cap_1": ("Natural Language Understanding", "Advanced intent recognition that comprehends nuances, typos, and complex user queries."),
        "cap_2": ("Contextual Memory", "Multi-turn dialog management that remembers user information throughout the conversation."),
        "cap_3": ("System Integration", "Connecting the bot via APIs to your CRM, ticketing system, or internal databases for real actions."),
        "cap_4": ("Seamless Human Handoff", "Automatic escalation to live agents when confidence scores drop, complete with conversation history.")
    },
    "airag-knowledge-assistant": {
        "overview": "Retrieval-Augmented Generation (RAG) systems that turn your internal documents into an interactive oracle. Employees can query your entire corporate knowledge base and receive precise, cited answers instantly.",
        "cap_1": ("Vector Database Architecture", "Converting millions of documents into highly searchable vector embeddings using Pinecone or Milvus."),
        "cap_2": ("Semantic Search", "Moving beyond keyword matching to find documents based on the actual meaning of the query."),
        "cap_3": ("Generative Synthesis", "Using LLMs to read the retrieved documents and write a coherent, accurate summary answer."),
        "cap_4": ("Source Citation", "Ensuring every AI-generated claim provides direct links back to the original source documents.")
    },
    "ai-business-automation": {
        "overview": "Replace manual, error-prone administrative tasks with intelligent, autonomous AI workflows. We connect your software ecosystem (Email, CRM, ERP) with AI decision engines to automate complex processes.",
        "cap_1": ("Intelligent Document Processing", "AI that can read invoices, contracts, and receipts, extracting key data and entering it into your systems."),
        "cap_2": ("Email Triage & Drafting", "NLP systems that categorize incoming emails, determine urgency, and draft contextual replies."),
        "cap_3": ("Workflow Orchestration", "Connecting disparate APIs to create seamless, multi-platform automated pipelines."),
        "cap_4": ("Exception Handling", "AI that knows its limits, automatically routing highly ambiguous cases to human supervisors.")
    },
    "ai-ml-custom-solution": {
        "overview": "Bespoke Artificial Intelligence engineering for unprecedented business challenges. If there is no off-the-shelf solution, our team of AI researchers and engineers will invent and build one from scratch.",
        "cap_1": ("First-Principles Research", "Evaluating cutting-edge academic papers to find novel algorithmic approaches to your problem."),
        "cap_2": ("Custom AI Architecture", "Designing unique neural network topologies specifically suited to your proprietary data format."),
        "cap_3": ("Hardware Optimization", "Tuning models for edge deployment, mobile devices, or specialized AI accelerators."),
        "cap_4": ("IP Generation", "Creating proprietary, defensible AI technology that becomes a core asset of your company.")
    },
    "custom-dataai-software": {
        "overview": "The complete package. We build end-to-end software platforms where Artificial Intelligence and big data processing are the core, fundamental features, not just add-ons.",
        "cap_1": ("Full-Stack AI Integration", "Seamless engineering from the database layer through the machine learning pipeline to the user interface."),
        "cap_2": ("Scalable Data Lakes", "Foundational infrastructure designed to ingest and store massive amounts of unstructured data."),
        "cap_3": ("Real-Time Processing", "Utilizing Kafka and Spark Streaming for continuous, low-latency data analysis and action."),
        "cap_4": ("Enterprise Grade Security", "Ensuring your proprietary algorithms and massive datasets are protected by military-grade encryption.")
    },
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

    # SOFTWARE & DESIGN
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

    # ACCOUNTING & FINANCE
    "accounting": {
        "overview": "Maintain absolute financial clarity and operational compliance. Our specialized accounting services provide the meticulous oversight required for sustainable business growth and risk mitigation.",
        "cap_1": ("Comprehensive Bookkeeping", "Flawless daily transaction recording, ledger maintenance, and bank reconciliations."),
        "cap_2": ("Financial Reporting", "Preparation of GAAP/IFRS compliant financial statements and executive summaries."),
        "cap_3": ("Payroll Management", "Automated, compliant payroll processing and tax withholding management."),
        "cap_4": ("Strategic Tax Planning", "Proactive tax strategies designed to optimize your financial position based on current regulations.")
    },
    "auditing": {
        "overview": "Independent, objective financial evaluations designed to build stakeholder trust and improve operational efficiency. We ensure absolute adherence to regulatory standards and internal controls.",
        "cap_1": ("Internal Control Reviews", "Deep evaluations of your financial processes to identify vulnerabilities and inefficiencies."),
        "cap_2": ("Regulatory Compliance", "Rigorous audits ensuring strict adherence to local, state, and federal financial regulations."),
        "cap_3": ("Risk Management", "Identification and strategic mitigation of enterprise-level financial risks."),
        "cap_4": ("Actionable Audit Reports", "Detailed management letters providing specific, actionable recommendations for improvement.")
    },
    "audit-accounting": {
        "overview": "A holistic financial assurance package combining meticulous daily accounting with rigorous periodic auditing. This end-to-end service guarantees your financial data is both continuously accurate and independently verified.",
        "cap_1": ("Continuous Ledger Management", "Real-time bookkeeping coupled with preemptive error checking to ensure audit-readiness at all times."),
        "cap_2": ("Interim & Annual Audits", "Comprehensive financial reviews conducted by certified professionals to validate corporate fiscal health."),
        "cap_3": ("Process Optimization", "Identifying workflow inefficiencies during the audit phase and implementing accounting software to fix them."),
        "cap_4": ("Stakeholder Reporting", "Producing certified financial statements required by investors, boards, and regulatory bodies.")
    },
    "corporate-audit-accounting": {
        "overview": "Enterprise-tier financial services designed for large organizations with complex corporate structures, international operations, and strict regulatory requirements. We provide absolute financial transparency and strategic fiscal guidance.",
        "cap_1": ("Consolidated Financials", "Managing complex ledgers across multiple subsidiaries, currencies, and international tax jurisdictions."),
        "cap_2": ("Sarbanes-Oxley (SOX) Compliance", "Rigorous internal control testing and documentation to ensure adherence to corporate governance laws."),
        "cap_3": ("Merger & Acquisition Due Diligence", "Deep forensic accounting and valuation services to assess the true financial health of target acquisitions."),
        "cap_4": ("Enterprise Risk Management", "Strategic modeling of macroeconomic, operational, and financial risks to protect corporate assets.")
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

    # SECURITY & SAAS
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

from pathlib import Path
base_dir = str(Path(__file__).resolve().parent / "services")

updated_count = 0
not_found_count = 0

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    if os.path.isdir(folder_path):
        file_path = os.path.join(folder_path, "index.html")
        if os.path.exists(file_path):
            # Find matching content
            content = content_dict.get(folder_name)
            if not content:
                print(f"Warning: No custom content defined for slug '{folder_name}'. Using a generic template.")
                # fallback content
                content = {
                    "overview": f"Comprehensive {folder_name.replace('-', ' ').title()} services tailored to your specific business needs. We deploy industry best practices to ensure optimal performance, scalability, and ROI.",
                    "cap_1": ("Strategic Implementation", "Customized deployment plans designed around your operational constraints."),
                    "cap_2": ("Advanced Technology", "Utilizing the latest frameworks and methodologies to ensure a future-proof solution."),
                    "cap_3": ("Continuous Optimization", "Ongoing monitoring and refinement to maximize efficiency and output over time."),
                    "cap_4": ("Dedicated Support", "Expert team available to resolve issues, provide training, and ensure project success.")
                }

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
            
            updated_count += 1
        else:
            not_found_count += 1

print(f"Update complete! Successfully injected detailed content into {updated_count} service pages.")
if not_found_count > 0:
    print(f"Note: {not_found_count} folders did not have an index.html file.")

