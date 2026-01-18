
from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        page.goto("http://localhost:8000")

        # Open the modal
        page.click("#open-modal-btn")

        # Fill out the form
        page.fill("input[name='name']", "Test User")
        page.fill("input[name='email']", "test@example.com")
        page.fill("textarea[name='message']", "This is a test message.")

        # Submit the form
        page.click("button[type='submit']")

        # Check for success message
        success_message = page.locator("#response-message-modal")
        expect(success_message).to_have_text("Your message has been sent successfully!")

        # Take a screenshot
        page.screenshot(path="verification/contact_form_success.png")

    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
