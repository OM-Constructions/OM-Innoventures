/**
 * OM Innoventures & Build AI Technologies
 * Centralized API Module
 */

const API_BASE = (typeof window !== 'undefined' && (
    window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1' ||
    window.location.hostname === '0.0.0.0'
  ) && (window.location.port !== "" && window.location.port !== "80" && window.location.port !== "443" && window.location.port !== "8000"))
  ? `${window.location.protocol}//${window.location.hostname}:8000/api`
  : 'https://om-innoventures-sori.vercel.app/api';


const Api = {
  getToken() {
    return localStorage.getItem('om_innoventures_token');
  },

  setToken(token) {
    if (token) {
      localStorage.setItem('om_innoventures_token', token);
    } else {
      localStorage.removeItem('om_innoventures_token');
    }
  },

  getUser() {
    try {
      const user = localStorage.getItem('om_innoventures_user');
      return user ? JSON.parse(user) : null;
    } catch {
      return null;
    }
  },

  setUser(user) {
    if (user) {
      localStorage.setItem('om_innoventures_user', JSON.stringify(user));
    } else {
      localStorage.removeItem('om_innoventures_user');
    }
  },

  clearSession() {
    localStorage.removeItem('om_innoventures_token');
    localStorage.removeItem('om_innoventures_user');
  },

  async request(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    };

    const token = this.getToken();
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(url, { ...options, headers });
      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        let errorMsg = `Request failed with status ${response.status}`;
        if (typeof data.detail === 'string') {
          errorMsg = data.detail;
        } else if (Array.isArray(data.detail)) {
          errorMsg = data.detail.map(e => (e && e.msg) ? e.msg : JSON.stringify(e)).join(', ');
        } else if (typeof data.message === 'string') {
          errorMsg = data.message;
        }
        throw new Error(errorMsg);
      }

      return data;
    } catch (err) {
      console.error(`[API Error] ${endpoint}:`, err);
      throw err;
    }
  },

  // Services
  async getServices() {
    return this.request('/services');
  },

  async getService(slug) {
    return this.request(`/services/${slug}`);
  },

  // Contact / Enquiry
  async submitEnquiry(payload) {
    return this.request('/contact', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  // Auth
  async signup(name, email, password, phone) {
    const data = await this.request('/auth/signup', {
      method: 'POST',
      body: JSON.stringify({ name, email, password, phone }),
    });
    if (data.access_token) {
      this.setToken(data.access_token);
      this.setUser(data.user);
    }
    return data;
  },

  async login(email, password) {
    const data = await this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    if (data.access_token) {
      this.setToken(data.access_token);
      this.setUser(data.user);
    }
    return data;
  },

  async getProfile() {
    return this.request('/auth/me');
  },

  // Client Enquiries Dashboard
  async getMyRequests() {
    return this.request('/me/requests');
  },

  // AI Assistant
  async askAssistant(query, service_slug = null) {
    return this.request('/assistant', {
      method: 'POST',
      body: JSON.stringify({ query, service_slug }),
    });
  }
};

window.Api = Api;
