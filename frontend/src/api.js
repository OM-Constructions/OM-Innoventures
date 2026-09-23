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

export async function submitEnquiry({ name, email, phone, location, serviceSlug, service, projectType, message, honeypot }) {
  const slug = service || serviceSlug || projectType || "general-consultation";
  const headers = { "Content-Type": "application/json" };
  try {
    const token = localStorage.getItem("om_auth_token");
    if (token) headers["Authorization"] = `Bearer ${token}`;
  } catch (e) {}
  const res = await fetch(`${API_BASE_URL}/api/v1/contact`, {
    method: "POST",
    headers,
    credentials: "include",
    body: JSON.stringify({
      name,
      email,
      phone: phone || null,
      location: location || null,
      service: slug,
      service_slug: slug,
      message,
      website: honeypot || "",
      honeypot: honeypot || "",
    }),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const errorMsg = formatApiErrorMessage(data, `Failed to submit enquiry (${res.status})`);
    const err = new Error(errorMsg);
    err.status = res.status;
    throw err;
  }
  return data;
}

export async function askAssistant(message, history = []) {
  const res = await fetch(`${API_BASE_URL}/api/v1/assistant/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, history }),
  });
  if (!res.ok) throw new Error("Assistant request failed");
  return res.json();
}

