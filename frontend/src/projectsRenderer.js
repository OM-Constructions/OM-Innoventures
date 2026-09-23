import { getPublishedProjects } from "./auth.js";

function formatServiceName(slug) {
  if (!slug) return "Engineering Solution";
  return slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
}

function formatDate(isoStr) {
  if (!isoStr) return "";
  try {
    return new Date(isoStr).toLocaleDateString("en-IN", {
      month: "short",
      year: "numeric",
    });
  } catch {
    return "";
  }
}

function renderStars(rating) {
  const r = Math.min(5, Math.max(1, parseInt(rating, 10) || 5));
  return "★".repeat(r) + "☆".repeat(5 - r);
}

/**
 * Render published projects with approved client reviews
 * @param {string} containerId - DOM ID of the container element
 * @param {string} [serviceSlug] - Optional filter for service detail pages
 */
export async function renderPublishedProjects(containerId = "publishedProjectsContainer", serviceSlug = null) {
  const container = document.getElementById(containerId);
  if (!container) return;

  // Show loading skeleton
  container.innerHTML = `
    <div style="grid-column: 1 / -1; text-align: center; padding: 40px 20px;">
      <div style="width: 32px; height: 32px; border: 3px solid rgba(218, 165, 32, 0.2); border-top-color: #daa520; border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 16px;"></div>
      <p style="color: #64748b; font-size: 0.95rem;">Loading verified projects &amp; client reviews...</p>
    </div>
  `;

  try {
    const projects = await getPublishedProjects(serviceSlug);

    if (!projects || projects.length === 0) {
      container.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 48px 24px; background: rgba(255, 255, 255, 0.7); border: 1px dashed #cbd5e1; border-radius: 12px; max-width: 600px; margin: 0 auto;">
          <div style="font-size: 2rem; margin-bottom: 12px;">🌟</div>
          <h4 style="font-family: var(--font-heading, sans-serif); color: #0b192c; font-size: 1.2rem; font-weight: 700; margin-bottom: 8px;">
            Verified Portfolio &amp; Reviews
          </h4>
          <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6; margin-bottom: 20px;">
            New client projects and verified reviews are published here in real time as deliveries are completed and approved.
          </p>
          <a href="#cta" class="btn-primary" style="display: inline-block; padding: 10px 24px; font-size: 0.9rem;">
            Commission a Project &rarr;
          </a>
        </div>
      `;
      return;
    }

    container.innerHTML = projects
      .map(
        (proj) => `
        <div class="project-portfolio-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 26px; box-shadow: 0 4px 14px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.25s ease, box-shadow 0.25s ease;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; gap: 8px; flex-wrap: wrap;">
              <span style="font-size: 0.78rem; font-weight: 700; text-transform: uppercase; color: #b45309; background: rgba(218, 165, 32, 0.12); padding: 4px 10px; border-radius: 4px;">
                ${formatServiceName(proj.service_slug)}
              </span>
              ${proj.completed_at ? `<span style="font-size: 0.8rem; color: #94a3b8;">${formatDate(proj.completed_at)}</span>` : ""}
            </div>

            <h3 style="font-family: var(--font-heading, sans-serif); color: #0b192c; font-size: 1.25rem; font-weight: 700; margin: 0 0 10px; line-height: 1.35;">
              ${proj.title}
            </h3>

            ${
              proj.summary
                ? `<p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin-bottom: 16px;">
                    ${proj.summary}
                  </p>`
                : ""
            }
          </div>

          <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #f1f5f9;">
            ${
              proj.rating
                ? `<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                    <div style="color: #f59e0b; font-size: 1.05rem; letter-spacing: 1px;">
                      ${renderStars(proj.rating)}
                    </div>
                    <span style="font-size: 0.78rem; font-weight: 600; color: #059669; background: #ecfdf5; padding: 2px 8px; border-radius: 4px;">
                      ✓ Verified Review
                    </span>
                  </div>`
                : ""
            }

            ${
              proj.review_text
                ? `<p style="font-size: 0.9rem; font-style: italic; color: #1e293b; line-height: 1.55; margin-bottom: 12px;">
                    "${proj.review_text}"
                  </p>`
                : ""
            }

            <div style="font-size: 0.82rem; font-weight: 600; color: #64748b;">
              &mdash; ${proj.client_display_name || "Verified Client"}
            </div>
          </div>
        </div>
      `
      )
      .join("");
  } catch (err) {
    console.error("Error loading published projects:", err);
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 32px 16px; color: #94a3b8; font-size: 0.9rem;">
        Unable to load project portfolio at this moment.
      </div>
    `;
  }
}
