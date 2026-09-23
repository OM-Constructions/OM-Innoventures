/**
 * OM Innoventures & Build AI Technologies
 * Authentication & Session Management Module
 */

document.addEventListener('DOMContentLoaded', () => {
  Auth.updateNavAuth();
  Auth.initLoginForm();
  Auth.initSignupForm();
  Auth.initMyRequests();
});

const Auth = {
  updateNavAuth() {
    const navActions = document.getElementById('navAuthActions');
    const mobileNavActions = document.getElementById('mobileNavAuthActions');
    const user = Api.getUser();

    const authHtml = user ? `
      <a href="/my-requests.html" class="btn btn-outline btn-sm" title="Client Portal">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        <span>${escapeHtml(user.name.split(' ')[0])}</span>
      </a>
      <button onclick="Auth.logout()" class="btn btn-text btn-sm" title="Log Out">Log Out</button>
    ` : `
      <a href="/login.html" class="btn btn-text btn-sm">Log In</a>
      <a href="/signup.html" class="btn btn-outline btn-sm">Sign Up</a>
    `;

    if (navActions) navActions.innerHTML = authHtml;
    if (mobileNavActions) mobileNavActions.innerHTML = authHtml;
  },

  logout() {
    Api.clearSession();
    window.location.href = '/login.html';
  },

  initLoginForm() {
    const form = document.getElementById('loginForm');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim();
      const password = document.getElementById('loginPassword').value;
      const errorBox = document.getElementById('loginError');
      const submitBtn = form.querySelector('button[type="submit"]');

      if (errorBox) errorBox.style.display = 'none';
      submitBtn.disabled = true;
      submitBtn.textContent = 'Authenticating...';

      try {
        await Api.login(email, password);
        window.location.href = '/my-requests.html';
      } catch (err) {
        if (errorBox) {
          errorBox.textContent = err.message || 'Login failed. Please check your credentials.';
          errorBox.style.display = 'block';
        }
        submitBtn.disabled = false;
        submitBtn.textContent = 'Log In';
      }
    });
  },

  initSignupForm() {
    const form = document.getElementById('signupForm');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const name = document.getElementById('signupName').value.trim();
      const email = document.getElementById('signupEmail').value.trim();
      const phone = document.getElementById('signupPhone').value.trim();
      const password = document.getElementById('signupPassword').value;
      const errorBox = document.getElementById('signupError');
      const submitBtn = form.querySelector('button[type="submit"]');

      if (errorBox) errorBox.style.display = 'none';
      submitBtn.disabled = true;
      submitBtn.textContent = 'Creating Account...';

      try {
        await Api.signup(name, email, password, phone);
        window.location.href = '/my-requests.html';
      } catch (err) {
        if (errorBox) {
          errorBox.textContent = err.message || 'Signup failed. Please try again.';
          errorBox.style.display = 'block';
        }
        submitBtn.disabled = false;
        submitBtn.textContent = 'Create Account';
      }
    });
  },

  async initMyRequests() {
    const tableBody = document.getElementById('requestsTableBody');
    const emptyState = document.getElementById('requestsEmptyState');
    const loadingState = document.getElementById('requestsLoading');
    if (!tableBody) return;

    const user = Api.getUser();
    if (!user) {
      window.location.href = '/login.html';
      return;
    }

    const userNameEl = document.getElementById('dashboardUserName');
    if (userNameEl) userNameEl.textContent = user.name;

    try {
      if (loadingState) loadingState.style.display = 'block';
      const requests = await Api.getMyRequests();
      if (loadingState) loadingState.style.display = 'none';

      if (!requests || requests.length === 0) {
        if (emptyState) emptyState.style.display = 'block';
        return;
      }

      tableBody.innerHTML = requests.map(req => {
        const dateFormatted = new Date(req.created_at).toLocaleDateString('en-US', {
          month: 'short',
          day: 'numeric',
          year: 'numeric'
        });

        let statusBadge = `<span class="status-pill status-received"><span class="status-dot"></span> ${escapeHtml(req.status)}</span>`;
        if (req.status === 'In Progress') {
          statusBadge = `<span class="status-pill status-progress"><span class="status-dot"></span> In Progress</span>`;
        } else if (req.status === 'Completed' || req.status === 'Contacted') {
          statusBadge = `<span class="status-pill status-completed"><span class="status-dot"></span> ${escapeHtml(req.status)}</span>`;
        }

        return `
          <tr>
            <td><strong>#REQ-${req.id.toString().padStart(4, '0')}</strong></td>
            <td><span style="color: var(--color-cyan); font-weight: 600;">${escapeHtml(req.service)}</span></td>
            <td>${dateFormatted}</td>
            <td>${statusBadge}</td>
            <td style="max-width: 320px; font-size: 0.88rem; color: var(--text-muted);">${escapeHtml(req.message)}</td>
          </tr>
        `;
      }).join('');
    } catch (err) {
      if (loadingState) loadingState.style.display = 'none';
      console.error('Error fetching enquiries:', err);
    }
  }
};

function escapeHtml(str) {
  if (!str) return '';
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

window.Auth = Auth;
