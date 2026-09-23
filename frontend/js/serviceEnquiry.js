/**
 * OM Innoventures & Build AI Technologies
 * Public Project Enquiry Form Handler
 */

document.addEventListener('DOMContentLoaded', () => {
  initServiceEnquiryForm();
});

async function initServiceEnquiryForm() {
  const form = document.getElementById('projectEnquiryForm');
  const serviceSelect = document.getElementById('enquiryService');
  const successBox = document.getElementById('enquirySuccessBox');
  const formContent = document.getElementById('enquiryFormContent');

  if (!form) return;

  // Pre-select service from URL query parameter (e.g. ?service=ai-ml-solutions)
  const urlParams = new URLSearchParams(window.location.search);
  const requestedService = urlParams.get('service');
  if (requestedService && serviceSelect) {
    serviceSelect.value = requestedService;
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('enquiryName').value.trim();
    const email = document.getElementById('enquiryEmail').value.trim();
    const phone = document.getElementById('enquiryPhone').value.trim();
    const service = document.getElementById('enquiryService').value;
    const message = document.getElementById('enquiryMessage').value.trim();
    const errorEl = document.getElementById('enquiryError');
    const submitBtn = document.getElementById('enquirySubmitBtn');

    if (errorEl) errorEl.style.display = 'none';

    if (!name || !email || !message) {
      if (errorEl) {
        errorEl.textContent = 'Please complete all required fields.';
        errorEl.style.display = 'block';
      }
      return;
    }

    submitBtn.disabled = true;
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = 'Sending Project Enquiry...';

    try {
      const payload = { name, email, phone, service, message };
      const response = await window.Api.submitEnquiry(payload);

      if (formContent) formContent.style.display = 'none';
      if (successBox) {
        const clientLineEl = document.getElementById('successClientLine');
        if (clientLineEl && response.service && response.service.client_line) {
          clientLineEl.textContent = response.service.client_line;
        }
        successBox.classList.add('active');
        successBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    } catch (err) {
      if (errorEl) {
        errorEl.textContent = err.message || 'Unable to send enquiry. Please check your connection or contact us directly.';
        errorEl.style.display = 'block';
      }
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
    }
  });
}

function resetEnquiryForm() {
  const form = document.getElementById('projectEnquiryForm');
  const successBox = document.getElementById('enquirySuccessBox');
  const formContent = document.getElementById('enquiryFormContent');
  const submitBtn = document.getElementById('enquirySubmitBtn');

  if (form) form.reset();
  if (formContent) formContent.style.display = 'block';
  if (successBox) successBox.classList.remove('active');
  if (submitBtn) {
    submitBtn.disabled = false;
    submitBtn.innerHTML = 'Send Project Enquiry &rarr;';
  }
}

window.initServiceEnquiryForm = initServiceEnquiryForm;
window.resetEnquiryForm = resetEnquiryForm;
