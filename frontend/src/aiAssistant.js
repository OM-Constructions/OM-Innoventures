/**
 * OM AI Assistant - Interactive Engineering &  Consultant
 * Provides real-time guidance on architectural design, structural engineering,
 * estimation & costing, tech capabilities, and project consultation.
 */
import { askAssistant } from './api.js';

export function initAIAssistant() {
    if (document.getElementById('om-ai-widget')) return;

    const isServicePage = window.location.pathname.includes('/services/');
    const basePath = isServicePage ? '../../' : '';
    const atlasAvatarPath = `${basePath}assets/atlas-avatar.png`;

    // 1. Create Widget DOM Container
    const container = document.createElement('div');
    container.id = 'om-ai-widget';
    container.className = 'om-ai-widget-container';
    container.innerHTML = `
        <!-- Floating Teaser Prompt -->
        <div class="om-ai-teaser" id="om-ai-teaser">
            <div class="om-ai-teaser-content">
                <span class="om-ai-teaser-icon">✨</span>
                <span class="om-ai-teaser-text">Have a project? Ask <strong>Atlas</strong></span>
            </div>
            <button class="om-ai-teaser-close" id="om-ai-teaser-close" aria-label="Close teaser">&times;</button>
        </div>

        <!-- Floating Action Button -->
        <button class="om-ai-launcher" id="om-ai-launcher" aria-label="Open Atlas Assistant">
            <div class="om-ai-launcher-icon">
                <img src="${atlasAvatarPath}" alt="Atlas" onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 24 24\\' fill=\\'%2307152F\\'><circle cx=\\'12\\' cy=\\'12\\' r=\\'11\\' fill=\\'%2307152F\\' stroke=\\'%23C99722\\' stroke-width=\\'1.5\\'/><path d=\\'M12 7a4 4 0 0 1 4 4v2a4 4 0 0 1-8 0v-2a4 4 0 0 1 4-4z\\' fill=\\'%23ffffff\\'/><circle cx=\\'10\\' cy=\\'11\\' r=\\'1\\' fill=\\'%2307152F\\'/><circle cx=\\'14\\' cy=\\'11\\' r=\\'1\\' fill=\\'%2307152F\\'/></svg>';" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">
            </div>
            <span class="om-ai-status-indicator" title="Atlas Active"></span>
        </button>

        <!-- AI Assistant Chat Window -->
        <div class="om-ai-window" id="om-ai-window" aria-hidden="true">
            <!-- Header -->
            <div class="om-ai-header">
                <div class="om-ai-header-info">
                    <div class="om-ai-avatar">
                        <img src="${atlasAvatarPath}" alt="Atlas" onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 24 24\\' fill=\\'%2307152F\\'><circle cx=\\'12\\' cy=\\'12\\' r=\\'11\\' fill=\\'%2307152F\\' stroke=\\'%23C99722\\' stroke-width=\\'1.5\\'/><path d=\\'M12 7a4 4 0 0 1 4 4v2a4 4 0 0 1-8 0v-2a4 4 0 0 1 4-4z\\' fill=\\'%23ffffff\\'/><circle cx=\\'10\\' cy=\\'11\\' r=\\'1\\' fill=\\'%2307152F\\'/><circle cx=\\'14\\' cy=\\'11\\' r=\\'1\\' fill=\\'%2307152F\\'/></svg>';" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">
                    </div>
                    <div>
                        <div class="om-ai-title">Atlas</div>
                        <div class="om-ai-subtitle"><span class="om-ai-green-dot"></span> Virtual Engineering Consultant &bull; Always Online</div>
                    </div>
                </div>
                <div class="om-ai-controls">
                    <button class="om-ai-btn-icon" id="om-ai-reset-btn" title="Restart conversation">
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
                    </button>
                    <button class="om-ai-btn-icon" id="om-ai-close-btn" title="Close chat">
                        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
                    </button>
                </div>
            </div>

            <!-- Quick Action Chips Carousel -->
            <div class="om-ai-chips-wrapper">
                <div class="om-ai-chips" id="om-ai-chips">
                    <button class="om-ai-chip" data-query="services">🏗️ Our 10 Services</button>
                    <button class="om-ai-chip" data-query="estimator">📐 Cost & Timeline Estimator</button>
                    <button class="om-ai-chip" data-query="structural">🏢 Structural & Soil Safety</button>
                    <button class="om-ai-chip" data-query="tech">🤖 AI & Tech Stack</button>
                    <button class="om-ai-chip" data-query="contact">📞 Book Consultation</button>
                </div>
            </div>

            <!-- Chat Message List -->
            <div class="om-ai-messages" id="om-ai-messages" role="log" aria-live="polite">
                <!-- Welcome message is injected via JS -->
            </div>

            <!-- Input Area -->
            <form class="om-ai-input-area" id="om-ai-form">
                <input 
                    type="text" 
                    id="om-ai-input" 
                    class="om-ai-input" 
                    placeholder="Ask about architectural plans, structural safety, costs..." 
                    autocomplete="off"
                    aria-label="Your question"
                />
                <button type="submit" class="om-ai-send-btn" id="om-ai-send-btn" aria-label="Send message">
                    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
                        <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                    </svg>
                </button>
            </form>

            <div class="om-ai-footer-brand">
                Powered by <strong>OM Innoventures & Build AI technologies</strong> Engineering Intelligence
            </div>
        </div>
    `;

    document.body.appendChild(container);

    // 2. Initialize Logic & Event Listeners
    setupAIAssistantEvents(atlasAvatarPath);
}

/**
 * Knowledge Base & Intent Resolution for OM Innoventures & Build AI technologies
 */
const KNOWLEDGE_BASE = {
    services: {
        title: "AI, Software & Data Intelligence Services",
        content: `At **OM Innoventures & Build AI technologies**, we provide end-to-end digital and AI solutions from concept to deployment:

1. 🌐 **Full Stack Web & Mobile Development**: High-performance React, Next.js, Node.js, and FastAPI platforms.
2. 🤖 **Generative AI & Custom LLM Agents**: RAG pipelines, intelligent customer support bots, and autonomous AI agents.
3. 🧠 **Machine Learning & Predictive Modeling**: Custom ML algorithms, churn prediction, classification, and forecasting.
4. 📊 **Power BI & Business Intelligence**: Interactive executive dashboards, DAX modeling, and automated KPI reports.
5. 🧹 **Excel & Data Automation**: Data cleaning, advanced financial modeling, and automated VBA/Python ETL pipelines.
6. ☁️ **Cloud Architecture & MLOps**: Scalable microservices, Docker, Kubernetes, and automated CI/CD deployment on AWS/GCP.
7. 🔒 **Cybersecurity & Data Governance**: Enterprise-grade access control, encryption, and vulnerability management.
8. 💼 **Accounting & Auditing Software Solutions**: Automated ledger bookkeeping, compliance, and financial reporting systems.

Would you like details on a specific service or an instant consultation?`,
        actions: [
            { text: "🤖 Explore AI & ML", query: "tech" },
            { text: "🌐 Web Development", query: "services" },
            { text: "📞 Book Free Consultation", query: "contact" }
        ]
    },

    tech: {
        title: "Technology Capabilities & AI Engineering",
        content: `OM Innoventures combines cutting-edge computational intelligence with robust software engineering:

- 🤖 **Gen AI & LLMs**: Custom AI agents, contextual RAG search, OpenAI/Claude/Gemini API integrations, and fine-tuning.
- 🧠 **Machine Learning**: Deep learning neural networks, computer vision, NLP, PyTorch & TensorFlow pipelines.
- ☁️ **Cloud & MLOps**: Scalable serverless backends on AWS, GCP & Azure with automated model monitoring.
- 📱 **Modern Full Stack**: High-throughput REST & GraphQL APIs in Python FastAPI/Node.js with reactive React/Next.js frontends.
- 🗄️ **Data & Vector DBs**: Vector databases (Pinecone, ChromaDB, pgvector) alongside PostgreSQL, MySQL & Redis.`,
        actions: [
            { text: "🚀 Explore All Services", query: "services" },
            { text: "📞 Discuss Tech Partnerships", query: "contact" }
        ]
    },

    industries: {
        title: "Industries We Serve",
        content: `We build intelligent digital solutions across key modern industries:

- 🏥 **Healthcare & Life Sciences**: Clinical predictive analytics, HIPAA-compliant patient management, and AI diagnostics.
- 💳 **Finance, Banking & Fintech**: Algorithmic risk models, fraud detection, and automated accounting workflows.
- 🛍️ **E-Commerce & Retail**: Recommendation engines, dynamic pricing, inventory optimization, and full storefronts.
- 🏭 **Manufacturing & Logistics**: Supply chain analytics, predictive maintenance, and IoT fleet tracking.
- 🎓 **Education & EdTech**: Adaptive AI tutoring, student analytics, and institutional LMS portals.
- 🛡️ **Cybersecurity & Public Sector**: Threat detection, compliance audit systems, and automated data workflows.`,
        actions: [
            { text: "🚀 Explore Services", query: "services" },
            { text: "📞 Talk to Us", query: "contact" }
        ]
    },

    estimator: {
        title: "Project Scope & Investment Estimator",
        content: `To help you plan your initiative, here are standard indicative investment tiers for our services:

🌐 **Web & Full Stack Platforms**:
- Landing Pages & Business Websites: Starting ₹9,999 - ₹24,999
- Advanced E-Commerce & Web Applications: Starting ₹49,999 - ₹1,49,999+

🤖 **AI, Machine Learning & Analytics**:
- Excel Data Cleaning & Power BI Dashboards: Starting ₹4,999 - ₹14,999
- Custom ML Models & AI Agent Deployment: Starting ₹49,999 - ₹1,99,999+

Would you like a customized scope and milestone estimate tailored to your exact project requirements?`,
        actions: [
            { text: "🚀 Submit Project Enquiry", action: "scrollToCta" },
            { text: "📞 Contact Engineering Team", query: "contact" },
            { text: "🌐 View Services", query: "services" }
        ]
    },

    contact: {
        title: "Get in Touch with OM Innoventures",
        content: `We'd love to help you build your digital and AI solutions!

- 📍 **Headquarters**: OM Innoventures & Build AI technologies
- 📞 **Direct Contact**: Reach out via phone or email to discuss project architecture
- 💬 **Fast Turnaround**: Comprehensive quotation and timeline within 24-48 hours
- 📋 **Specialties**: Full Stack Development, AI Solutions, Machine Learning, Data Analytics & Power BI.

You can also submit your details directly using the contact form below.`,
        actions: [
            { text: "🚀 Go to Contact Section", action: "scrollToCta" },
            { text: "📐 Project Estimator", query: "estimator" },
            { text: "🌐 Explore Services", query: "services" }
        ]
    }
};

/**
 * Intelligent Query Classifier
 */
function resolveQuery(input) {
    const text = input.toLowerCase().trim();

    if (!text) return null;

    // Direct key matches
    if (text === 'services' || text === 'all services' || text.includes('what services') || text.includes('service') || text.includes('what do you do') || text.includes('offering')) {
        return KNOWLEDGE_BASE.services;
    }
    if (text === 'structural' || text.includes('structure') || text.includes('soil') || text.includes('earthquake') || text.includes('seismic') || text.includes('geotechnical') || text.includes('bearing capacity') || text.includes('foundation')) {
        return KNOWLEDGE_BASE.structural;
    }
    if (text === 'architectural' || text.includes('architect') || text.includes('2d') || text.includes('floor plan') || text.includes('blue print') || text.includes('vaastu') || text.includes('vastu') || text.includes('layout')) {
        return KNOWLEDGE_BASE.architectural;
    }
    if (text === 'rendering' || text.includes('render') || text.includes('3d') || text.includes('elevation') || text.includes('interior') || text.includes('walkthrough')) {
        return KNOWLEDGE_BASE.rendering;
    }
    if (text === 'tech' || text.includes('technology') || text.includes('ai') || text.includes('llm') || text.includes('machine learning') || text.includes('cloud') || text.includes('software') || text.includes('devops')) {
        return KNOWLEDGE_BASE.tech;
    }
    if (text === 'estimator' || text.includes('cost') || text.includes('price') || text.includes('budget') || text.includes('rate') || text.includes('estimate') || text.includes('timeline') || text.includes('duration') || text.includes('how much') || text.includes('sq ft') || text.includes('square feet')) {
        return KNOWLEDGE_BASE.estimator;
    }
    if (text === 'contact' || text.includes('contact') || text.includes('phone') || text.includes('call') || text.includes('email') || text.includes('reach') || text.includes('address') || text.includes('location') || text.includes('hire') || text.includes('book') || text.includes('consultation')) {
        return KNOWLEDGE_BASE.contact;
    }
    if (text.includes('industry') || text.includes('sector') || text.includes('commercial') || text.includes('residential') || text.includes('warehouse') || text.includes('factory')) {
        return KNOWLEDGE_BASE.industries;
    }

    // Smart compound match
    if (text.includes('data') || text.includes('analytics') || text.includes('power bi') || text.includes('dashboard') || text.includes('excel') || text.includes('report')) {
        return {
            title: "Data Analytics & Business Intelligence",
            content: `Our **Data Analytics & BI division** transforms raw records into actionable executive intelligence:
- **Power BI & Dashboards**: Interactive executive dashboards with live multi-source sync and custom DAX metrics.
- **Excel Automation & ETL**: Cleaning messy spreadsheets, automated reconciliation macros, and Python pipelines.
- **SQL & Data Warehousing**: High-speed schema design, complex query optimization, and automated reporting.`,
            actions: [
                { text: "📊 Explore Analytics Services", query: "services" },
                { text: "📞 Book Analytics Consultation", query: "contact" }
            ]
        };
    }

    if (text.includes('web') || text.includes('app') || text.includes('website') || text.includes('frontend') || text.includes('backend') || text.includes('full stack')) {
        return {
            title: "Full Stack & Web Development",
            content: `We build modern, scalable, and responsive web platforms:
- **High Conversion Websites**: Single-page and multi-page professional corporate portals.
- **Full Stack Applications**: Reactive React/Next.js frontends with Python FastAPI and Node.js backends.
- **E-Commerce Solutions**: Complete storefronts with secure payment gateway integrations.`,
            actions: [
                { text: "🌐 View Web Services", query: "services" },
                { text: "📞 Start a Project", query: "contact" }
            ]
        };
    }

    // Lead detection: If user provided a phone number or email
    const phoneRegex = /(?:\+?\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}|\d{10}/;
    const emailRegex = /[\w.-]+@[\w.-]+\.\w+/;
    if (phoneRegex.test(text) || emailRegex.test(text)) {
        return {
            title: "Inquiry Received! 🤝",
            content: `Thank you for sharing your contact information. Our engineering and AI consultation team will review your request and reach out shortly to discuss your project requirements!

In the meantime, feel free to explore our services or calculate indicative costs.`,
            actions: [
                { text: "📐 Scope & Cost Estimator", query: "estimator" },
                { text: "🌐 Explore Services", query: "services" }
            ]
        };
    }

    // Unmatched query: return null to trigger real AI backend
    return null;
}

/**
 * Event handling and UI interactions
 */
function setupAIAssistantEvents(atlasAvatarPath) {
    const launcher = document.getElementById('om-ai-launcher');
    const windowEl = document.getElementById('om-ai-window');
    const teaser = document.getElementById('om-ai-teaser');
    const teaserClose = document.getElementById('om-ai-teaser-close');
    const closeBtn = document.getElementById('om-ai-close-btn');
    const resetBtn = document.getElementById('om-ai-reset-btn');
    const form = document.getElementById('om-ai-form');
    const input = document.getElementById('om-ai-input');
    const messagesEl = document.getElementById('om-ai-messages');
    const chips = document.getElementById('om-ai-chips');

    let isOpen = false;
    let isTyping = false;
    let chatHistory = [];
    let userMessageCount = 0;
    const SESSION_CAP = 20;

    // Show initial greeting
    function renderWelcome() {
        messagesEl.innerHTML = '';
        addBotMessage({
            title: "",
            content: `Hello! I am Atlas, your Virtual AI & Engineering Consultant for OM Innoventures & Build AI technologies.

I can guide you through our **AI, Machine Learning, Full Stack & Data Intelligence services**, calculate an **indicative project scope & investment estimate**, or help you book a **free architectural consultation**.

Choose a topic below or type any question!`,
            actions: [
                { text: "🌐 All Services", query: "services" },
                { text: "🤖 AI & Machine Learning", query: "tech" },
                { text: "📐 Scope & Investment Estimator", query: "estimator" },
                { text: "📞 Book Free Consultation", query: "contact" }
            ]
        }, false);
        messagesEl.scrollTop = 0;
    }

    renderWelcome();

    // Toggle window open / close
    function toggleChat(open) {
        isOpen = open !== undefined ? open : !isOpen;
        if (isOpen) {
            windowEl.classList.add('om-ai-open');
            windowEl.setAttribute('aria-hidden', 'false');
            launcher.classList.add('om-ai-launcher-active');
            if (teaser) teaser.style.display = 'none';
            setTimeout(() => input.focus(), 250);
            if (messagesEl.children.length <= 1) {
                messagesEl.scrollTop = 0;
            } else {
                messagesEl.scrollTop = messagesEl.scrollHeight;
            }
        } else {
            windowEl.classList.remove('om-ai-open');
            windowEl.setAttribute('aria-hidden', 'true');
            launcher.classList.remove('om-ai-launcher-active');
        }
    }

    launcher.addEventListener('click', () => toggleChat());
    closeBtn.addEventListener('click', () => toggleChat(false));

    if (teaser) {
        teaser.addEventListener('click', (e) => {
            if (e.target !== teaserClose) {
                toggleChat(true);
            }
        });
        teaserClose.addEventListener('click', (e) => {
            e.stopPropagation();
            teaser.style.display = 'none';
        });
    }

    resetBtn.addEventListener('click', () => {
        chatHistory = [];
        userMessageCount = 0;
        renderWelcome();
    });

    // Handle Form Submit
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = input.value.trim();
        if (!query || isTyping) return;

        input.value = '';
        addUserMessage(query);
        userMessageCount++;

        // 1. First check instant zero-token match from hardcoded knowledge base
        const localMatch = resolveQuery(query);
        if (localMatch) {
            isTyping = true;
            showTypingIndicator();
            chatHistory.push({ role: 'user', content: query });
            chatHistory.push({ role: 'assistant', content: localMatch.content });
            setTimeout(() => {
                removeTypingIndicator();
                addBotMessage(localMatch, true);
                isTyping = false;
            }, 350 + Math.random() * 200);
            return;
        }

        // 2. Check session cap for open-ended queries
        if (userMessageCount > SESSION_CAP) {
            isTyping = true;
            showTypingIndicator();
            setTimeout(() => {
                removeTypingIndicator();
                addBotMessage({
                    title: "Consultation Limit Reached",
                    content: "You've asked several questions in this session. For custom structural reviews, site soil testing, or detailed project quotations, please submit an enquiry below to speak directly with our senior engineering consultants.",
                    actions: [
                        { text: "🚀 Submit Project Enquiry", action: "scrollToCta" },
                        { text: "📞 Book Free Consultation", query: "contact" }
                    ]
                }, true);
                isTyping = false;
            }, 350);
            return;
        }

        // 3. Fallback to real AI backend for open-ended queries
        isTyping = true;
        showTypingIndicator();
        chatHistory.push({ role: 'user', content: query });

        try {
            // Pass last few exchanges to keep token usage small and predictable
            const recentHistory = chatHistory.slice(-12);
            const data = await askAssistant(query, recentHistory);
            removeTypingIndicator();
            const replyText = data && data.reply ? data.reply : "Thank you for your enquiry. Please submit your project details to speak with our engineering team.";
            chatHistory.push({ role: 'assistant', content: replyText });
            addBotMessage({
                content: replyText,
                actions: [
                    { text: "🚀 Submit Project Enquiry", action: "scrollToCta" },
                    { text: "🏗️ View 10 Services", query: "services" }
                ]
            }, true);
        } catch (err) {
            console.error('[ATLAS ASSISTANT ERROR]', err);
            removeTypingIndicator();
            const fallbackMsg = "I'd be glad to assist with that! At **OM Innoventures & Build AI technologies**, we specialize in Full Stack Development, Custom AI & Machine Learning, Power BI Dashboards, and Enterprise Cloud Solutions. Please submit your project details below to consult directly with our engineers.";
            chatHistory.push({ role: 'assistant', content: fallbackMsg });
            addBotMessage({
                title: "OM Technology Consultation",
                content: fallbackMsg,
                actions: [
                    { text: "🚀 Submit Project Enquiry", action: "scrollToCta" },
                    { text: "🌐 View Services", query: "services" },
                    { text: "📞 Contact Engineering Team", query: "contact" }
                ]
            }, true);
        } finally {
            isTyping = false;
        }
    });

    // Handle Quick Action Chips
    chips.addEventListener('click', (e) => {
        const btn = e.target.closest('.om-ai-chip');
        if (!btn || isTyping) return;
        const query = btn.getAttribute('data-query');
        triggerQuery(query, btn.textContent);
    });

    // Handle message actions
    messagesEl.addEventListener('click', (e) => {
        const btn = e.target.closest('.om-ai-action-btn');
        if (!btn || isTyping) return;

        const actionType = btn.getAttribute('data-action');
        const query = btn.getAttribute('data-query');

        if (actionType === 'scrollToCta') {
            toggleChat(false);
            const cta = document.getElementById('cta');
            if (cta) {
                cta.scrollIntoView({ behavior: 'smooth' });
            }
            return;
        }


        if (query) {
            triggerQuery(query, btn.textContent);
        }
    });

    function triggerQuery(key, displayText) {
        addUserMessage(displayText || key);
        const response = KNOWLEDGE_BASE[key] || resolveQuery(key);
        if (response) {
            chatHistory.push({ role: 'user', content: displayText || key });
            chatHistory.push({ role: 'assistant', content: response.content });
            isTyping = true;
            showTypingIndicator();

            setTimeout(() => {
                removeTypingIndicator();
                addBotMessage(response, true);
                isTyping = false;
            }, 350 + Math.random() * 200);
        }
    }

    function addUserMessage(text) {
        const msg = document.createElement('div');
        msg.className = 'om-ai-msg om-ai-msg-user';
        msg.innerHTML = `
            <div class="om-ai-msg-bubble">${escapeHTML(text)}</div>
        `;
        messagesEl.appendChild(msg);
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function showTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.className = 'om-ai-msg om-ai-msg-bot om-ai-typing-indicator';
        indicator.id = 'om-ai-typing';
        indicator.innerHTML = `
            <div class="om-ai-msg-avatar">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="#C99722"><circle cx="12" cy="12" r="8"/></svg>
            </div>
            <div class="om-ai-msg-bubble om-ai-dots">
                <span></span><span></span><span></span>
            </div>
        `;
        messagesEl.appendChild(indicator);
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function removeTypingIndicator() {
        const indicator = document.getElementById('om-ai-typing');
        if (indicator) indicator.remove();
    }

    function addBotMessage(responseObj, stream = false) {
        const msg = document.createElement('div');
        msg.className = 'om-ai-msg om-ai-msg-bot';

        let formattedText = formatMarkdown(responseObj.content);

        let actionsHTML = '';
        if (responseObj.actions && responseObj.actions.length > 0) {
            actionsHTML = `
                <div class="om-ai-msg-actions">
                    ${responseObj.actions.map(act => `
                        <button class="om-ai-action-btn" 
                                ${act.query ? `data-query="${act.query}"` : ''} 
                                ${act.action ? `data-action="${act.action}"` : ''}>
                            ${act.text}
                        </button>
                    `).join('')}
                </div>
            `;
        }

        msg.innerHTML = `
            <div class="om-ai-msg-avatar">
                <img src="${atlasAvatarPath}" alt="Atlas" onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 24 24\\' fill=\\'%2307152F\\'><circle cx=\\'12\\' cy=\\'12\\' r=\\'11\\' fill=\\'%2307152F\\' stroke=\\'%23C99722\\' stroke-width=\\'1.5\\'/><path d=\\'M12 7a4 4 0 0 1 4 4v2a4 4 0 0 1-8 0v-2a4 4 0 0 1 4-4z\\' fill=\\'%23ffffff\\'/><circle cx=\\'10\\' cy=\\'11\\' r=\\'1\\' fill=\\'%2307152F\\'/><circle cx=\\'14\\' cy=\\'11\\' r=\\'1\\' fill=\\'%2307152F\\'/></svg>';" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">
            </div>
            <div class="om-ai-msg-body">
                ${responseObj.title ? `<div class="om-ai-msg-heading">${escapeHTML(responseObj.title)}</div>` : ''}
                <div class="om-ai-msg-bubble om-ai-stream-target">${formattedText}</div>
                ${actionsHTML}
            </div>
        `;

        messagesEl.appendChild(msg);
        messagesEl.scrollTop = messagesEl.scrollHeight;

        if (stream) {
            const target = msg.querySelector('.om-ai-stream-target');
            target.classList.add('om-ai-stream-fade');
            messagesEl.scrollTop = messagesEl.scrollHeight;
        }
    }

    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, 
            tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag));
    }

    function formatMarkdown(str) {
        if (!str) return '';
        let html = str
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/(?:^|\n)- (.*?)(?=\n|$)/g, '<br>&bull; $1')
            .replace(/(?:^|\n)(\d+)\. (.*?)(?=\n|$)/g, '<br><strong>$1.</strong> $2')
            .replace(/\n\n/g, '<br><br>')
            .replace(/\n/g, '<br>');
        
        // Trim leading <br> if generated by first bullet
        if (html.startsWith('<br>')) {
            html = html.substring(4);
        }
        return html;
    }
}
