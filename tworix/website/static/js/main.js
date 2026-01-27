document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('contact-modal');
    const openBtn = document.getElementById('open-modal-btn');
    const closeBtn = document.getElementById('close-modal-btn');
    const form = document.getElementById('contact-form-modal');
    const responseMessage = document.getElementById('response-message-modal');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const closeMobileMenuBtn = document.getElementById('close-mobile-menu-btn');
    const mobileMenuBtnIcon = mobileMenuBtn ? mobileMenuBtn.querySelector('span') : null;

    function openModal() {
        if(modal) modal.classList.remove('hidden');
    }

    function closeModal() {
        if(modal) {
            modal.classList.add('hidden');
            if(responseMessage) responseMessage.innerHTML = '';
            if(form) form.reset();
        }
    }

    function toggleMobileMenu() {
        if (!mobileMenu) return;
        const isHidden = mobileMenu.classList.contains('hidden');
        if (isHidden) {
            mobileMenu.classList.remove('hidden');
            if (mobileMenuBtnIcon) mobileMenuBtnIcon.textContent = 'close';
        } else {
            mobileMenu.classList.add('hidden');
            if (mobileMenuBtnIcon) mobileMenuBtnIcon.textContent = 'menu';
        }
    }

    // Make functions globally available
    window.openModal = openModal;
    window.closeMobileMenu = toggleMobileMenu;

    if(openBtn) openBtn.addEventListener('click', openModal);
    if(closeBtn) closeBtn.addEventListener('click', closeModal);

    if(mobileMenuBtn) mobileMenuBtn.addEventListener('click', toggleMobileMenu);
    if(closeMobileMenuBtn) closeMobileMenuBtn.addEventListener('click', toggleMobileMenu);


    // Close modal if clicking outside the content
    if(modal) modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close modal on escape key press
    document.addEventListener('keydown', function (e) {
        if (e.key === "Escape" && modal && !modal.classList.contains('hidden')) {
            closeModal();
        }
    });

    if(form) form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(form);
        const url = form.getAttribute('data-url');
        const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                responseMessage.className = 'text-primary font-bold';
                responseMessage.textContent = data.message;
                setTimeout(closeModal, 2000); // Close modal after 2 seconds on success
            } else {
                responseMessage.className = 'text-accent font-bold';
                responseMessage.textContent = data.message || 'An error occurred.';
            }
        })
        .catch(error => {
            responseMessage.className = 'text-accent font-bold';
            responseMessage.textContent = 'A network error occurred. Please try again.';
            console.error('Error:', error);
        });
    });

    // Handle connect page form
    const connectForm = document.getElementById('contact-form-page');
    const responseMessageConnect = document.getElementById('response-message-page');

    if (connectForm) {
        connectForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(connectForm);
            const url = connectForm.getAttribute('data-url');
            const csrfToken = connectForm.querySelector('input[name="csrfmiddlewaretoken"]').value;

            fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    responseMessageConnect.className = 'text-primary font-bold mt-4';
                    responseMessageConnect.textContent = data.message;
                    connectForm.reset();
                } else {
                    responseMessageConnect.className = 'text-accent font-bold mt-4';
                    responseMessageConnect.textContent = data.message || 'An error occurred.';
                }
            })
            .catch(error => {
                responseMessageConnect.className = 'text-accent font-bold mt-4';
                responseMessageConnect.textContent = 'A network error occurred. Please try again.';
                console.error('Error:', error);
            });
        });
    }
});