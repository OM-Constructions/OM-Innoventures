export const API_BASE_URL = 
  (typeof window !== "undefined" && window.API_BASE_URL) ||
  (typeof window !== "undefined" && (
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1" ||
    window.location.hostname === "0.0.0.0" ||
    window.location.hostname.endsWith(".local") ||
    (window.location.port !== "" && window.location.port !== "80" && window.location.port !== "443" && window.location.port !== "8000")
  )
    ? `${window.location.protocol}//${window.location.hostname === "0.0.0.0" ? "localhost" : window.location.hostname}:8000`
    : "https://om-innoventures-sori.vercel.app");


export function getStoredToken() {
  try {
    return localStorage.getItem("om_auth_token") || null;
  } catch (e) {
    return null;
  }
}

export function setStoredToken(token) {
  try {
    if (token) {
      localStorage.setItem("om_auth_token", token);
    } else {
      localStorage.removeItem("om_auth_token");
    }
  } catch (e) {}
}

export function getAuthHeaders(extraHeaders = {}) {
  const token = getStoredToken();
  const headers = { ...extraHeaders };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }
  return headers;
}

export function formatApiErrorMessage(data, fallback = "An unexpected error occurred") {
  if (!data) return fallback;
  if (typeof data === "string") return data;
  if (typeof data.detail === "string") return data.detail;
  if (Array.isArray(data.detail)) {
    const msgs = data.detail.map((err) => {
      if (typeof err === "string") return err;
      if (err && err.msg) {
        const field = Array.isArray(err.loc) ? err.loc.filter((l) => l !== "body").join(".") : "";
        return field ? `${field}: ${err.msg}` : err.msg;
      }
      return JSON.stringify(err);
    });
    return msgs.join("; ") || fallback;
  }
  if (data.detail && typeof data.detail === "object") {
    return data.detail.msg || data.detail.message || JSON.stringify(data.detail);
  }
  if (typeof data.message === "string") return data.message;
  if (typeof data.error === "string") return data.error;
  return fallback;
}

/**
 * Register a new customer account
 * @param {{ name: string, email: string, password: string }}
 * @returns {Promise<{ success: boolean, message: string }>}
 */
export async function signup({ name, email, password }) {
  const res = await fetch(`${API_BASE_URL}/api/v1/auth/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ name, email, password }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(formatApiErrorMessage(data, "Unable to create account"));
  }
  try {
    if (data.access_token || data.token) {
      localStorage.setItem("om_logged_in", "true");
      const userName = (data.user && data.user.name) || data.name || name;
      const token = data.access_token || data.token;
      if (userName) localStorage.setItem("om_user_name", userName);
      if (token) setStoredToken(token);
      _cachedUser = { name: userName, email: email || (data.user && data.user.email) || "" };
      _authLoading = false;
    }
  } catch (e) {}
  return data;
}

/**
 * Log in with email and password
 * @param {{ email: string, password: string }}
 * @returns {Promise<{ success: boolean, name: string, token?: string }>}
 */
export async function login({ email, password }) {
  const res = await fetch(`${API_BASE_URL}/api/v1/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ email, password }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const errorMsg = formatApiErrorMessage(data, "Invalid email or password");
    const err = new Error(errorMsg);
    err.status = res.status;
    err.code = data.error || (data.detail === "email_not_verified" ? "email_not_verified" : null);
    throw err;
  }
  try {
    localStorage.setItem("om_logged_in", "true");
    // Support both formats: {token, name} (live) and {access_token, user: {name}} (local)
    const name = data.name || (data.user && data.user.name) || "";
    const token = data.token || data.access_token || null;
    if (name) localStorage.setItem("om_user_name", name);
    if (token) setStoredToken(token);
    _cachedUser = { name, email: email || (data.user && data.user.email) || "" };
    _authLoading = false;
  } catch (e) {}
  return data;
}

/**
 * Verify 6-digit OTP code and set session cookie
 * @param {{ email: string, otp: string }}
 * @returns {Promise<{ success: boolean, name: string }>}
 */
export async function verifyOtp(arg1, arg2) {
  let email, otp;
  if (typeof arg1 === "object" && arg1 !== null) {
    email = arg1.email;
    otp = arg1.otp;
  } else {
    email = arg1;
    otp = arg2;
  }
  const res = await fetch(`${API_BASE_URL}/api/v1/auth/verify-otp`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ email: email ? email.trim() : "", otp: otp ? otp.trim() : "" }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const errorMsg = formatApiErrorMessage(data, "Invalid or expired code");
    const err = new Error(errorMsg);
    err.status = res.status;
    throw err;
  }
  try {
    localStorage.setItem("om_logged_in", "true");
    if (data.name) localStorage.setItem("om_user_name", data.name);
    if (data.token) setStoredToken(data.token);
    _cachedUser = { name: data.name || "", email: email || "" };
    _authLoading = false;
  } catch (e) {}
  return data;
}

/**
 * Resend 6-digit OTP code
 * @param {string} email
 * @returns {Promise<{ success: boolean, message: string }>}
 */
export async function resendOtp(email) {
  const res = await fetch(`${API_BASE_URL}/api/v1/auth/resend-otp`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const errorMsg = formatApiErrorMessage(data, "Unable to resend code");
    const err = new Error(errorMsg);
    err.status = res.status;
    throw err;
  }
  return data;
}

/**
 * Log out and clear session cookie & stored auth tokens
 * @returns {Promise<{ success: boolean, message: string }>}
 */
export async function logout() {
  const headers = getAuthHeaders();
  try {
    localStorage.removeItem("om_logged_in");
    localStorage.removeItem("om_user_name");
    setStoredToken(null);
    _cachedUser = null;
    _authLoading = false;
    _authPromise = null;
  } catch (e) {}
  const res = await fetch(`${API_BASE_URL}/api/v1/auth/logout`, {
    method: "POST",
    headers,
    credentials: "include",
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(data.detail || "Failed to log out");
  }
  return data;
}

/**
 * Synchronous check for stored login flag
 * @returns {boolean}
 */
export function isStoredUserLoggedIn() {
  try {
    return localStorage.getItem("om_logged_in") === "true" || !!getStoredToken();
  } catch (e) {
    return false;
  }
}

let _authLoading = true;
let _cachedUser = null;
let _authPromise = null;

export function initAuth() {
  if (!_authPromise) {
    _authLoading = true;
    _authPromise = (async () => {
      try {
        const user = await getCurrentUser();
        _cachedUser = user;
      } catch (err) {
        if (isStoredUserLoggedIn()) {
          const name = localStorage.getItem("om_user_name") || "Client";
          _cachedUser = { name, email: "" };
        } else {
          _cachedUser = null;
        }
      } finally {
        _authLoading = false;
      }
      return _cachedUser;
    })();
  }
  return _authPromise;
}

export async function waitForAuth() {
  if (!_authPromise) {
    return initAuth();
  }
  return _authPromise;
}

export function isAuthLoading() {
  return _authLoading;
}

export function getCachedUser() {
  return _cachedUser;
}

/**
 * Fetch helper with strict timeout to prevent infinite hanging
 */
export async function fetchWithTimeout(resource, options = {}, timeoutMs = 12000) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(resource, {
      ...options,
      signal: controller.signal
    });
    return response;
  } finally {
    clearTimeout(timer);
  }
}

/**
 * Check if the user is logged in
 * @returns {Promise<{ name: string, email: string } | null>}
 */
export async function getCurrentUser() {
  try {
    const res = await fetchWithTimeout(`${API_BASE_URL}/api/v1/auth/me`, {
      method: "GET",
      headers: getAuthHeaders(),
      credentials: "include",
    }, 20000);
    
    if (!res.ok) {
      // Only clear storage if explicitly rejected as unauthenticated
      if (res.status === 401 || res.status === 403) {
        try {
          localStorage.removeItem("om_logged_in");
          localStorage.removeItem("om_user_name");
          setStoredToken(null);
          _cachedUser = null;
        } catch (e) {}
        return null;
      }
      throw new Error(`Server returned HTTP ${res.status}`);
    }
    const data = await res.json();
    try {
      localStorage.setItem("om_logged_in", "true");
      if (data && data.name) localStorage.setItem("om_user_name", data.name);
      _cachedUser = data;
    } catch (e) {}
    return data;
  } catch (err) {
    console.warn("getCurrentUser check encountered network or server error:", err.message);
    const networkErr = new Error(err.message || "Connection timeout");
    networkErr.isNetworkError = true;
    throw networkErr;
  }
}

/**
 * Fetch the logged-in customer's own enquiries
 * @returns {Promise<Array<{ id: number, name: string, project_type: string, message: string, status: string, created_at: string }>>}
 */
export async function getMySubmissions() {
  const res = await fetchWithTimeout(`${API_BASE_URL}/api/v1/me/requests`, {
    method: "GET",
    headers: getAuthHeaders(),
    credentials: "include",
  }, 20000);
  
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(formatApiErrorMessage(data, `Failed to load submissions (${res.status})`));
  }
  return data;
}

/**
 * Fetch the logged-in client's own projects and their review status
 * @returns {Promise<Array<{ id: number, title: string, service_slug: string, summary: string, status: string, completed_at: string, review: object }>>}
 */
export async function getMyProjects() {
  const res = await fetchWithTimeout(`${API_BASE_URL}/api/v1/projects/me`, {
    method: "GET",
    headers: getAuthHeaders(),
    credentials: "include",
  }, 20000);

  const data = await res.json().catch(() => ([]));
  if (!res.ok) {
    throw new Error(formatApiErrorMessage(data, `Failed to load projects (${res.status})`));
  }
  return data;
}

/**
 * Submit client review for a completed project
 * @param {number} projectId
 * @param {{ rating: number, review_text: string }} payload
 * @returns {Promise<object>}
 */
export async function submitProjectReview(projectId, { rating, review_text }) {
  const res = await fetch(`${API_BASE_URL}/api/v1/projects/${projectId}/review`, {
    method: "POST",
    headers: getAuthHeaders({ "Content-Type": "application/json" }),
    credentials: "include",
    body: JSON.stringify({ rating: Number(rating), review_text }),
  });

  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(formatApiErrorMessage(data, `Failed to submit review (${res.status})`));
  }
  return data;
}

/**
 * Fetch public published projects with verified client reviews
 * @param {string} [serviceSlug]
 * @returns {Promise<Array<{ id: number, title: string, service_slug: string, summary: string, client_display_name: string, rating: number, review_text: string, completed_at: string }>>}
 */
export async function getPublishedProjects(serviceSlug = null) {
  const url = serviceSlug 
    ? `${API_BASE_URL}/api/v1/projects/published?service_slug=${encodeURIComponent(serviceSlug)}`
    : `${API_BASE_URL}/api/v1/projects/published`;

  const res = await fetch(url, {
    method: "GET",
  });

  const data = await res.json().catch(() => ([]));
  if (!res.ok) {
    throw new Error(formatApiErrorMessage(data, "Unable to fetch published projects"));
  }
  return data;
}

