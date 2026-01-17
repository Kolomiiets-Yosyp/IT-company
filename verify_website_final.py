import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        base_url = "http://127.0.0.1:8000"

        # 1. Home page
        await page.goto(base_url)
        await page.screenshot(path="verification/01_home_page_final.png")

        # 2. Solutions page
        await page.goto(f"{base_url}/solutions")
        await page.screenshot(path="verification/02_solutions_page_final.png")

        # 3. The Lab page
        await page.goto(f"{base_url}/lab")
        await page.screenshot(path="verification/03_lab_page_final.png")

        # 4. About page
        await page.goto(f"{base_url}/about")
        await page.screenshot(path="verification/04_about_page_final.png")

        # 5. Connect page
        await page.goto(f"{base_url}/connect")
        await page.screenshot(path="verification/05_connect_page_final.png")

        # 6. Contact modal functionality
        await page.goto(base_url)
        await page.click('button:has-text("CONTACT US")')
        await page.wait_for_selector('#contact-modal', state='visible')
        await page.screenshot(path="verification/06_contact_modal_open_final.png")
        await page.click('#close-modal-btn')

        # 7. Build page
        await page.goto(f"{base_url}/build")
        await page.screenshot(path="verification/07_build_page.png")

        # 8. Grid page
        await page.goto(f"{base_url}/grid")
        await page.screenshot(path="verification/08_grid_page.png")

        # 9. Core page
        await page.goto(f"{base_url}/core")
        await page.screenshot(path="verification/09_core_page.png")

        # 10. Directory page
        await page.goto(f"{base_url}/directory")
        await page.screenshot(path="verification/10_directory_page.png")

        # 11. The Vault page
        await page.goto(f"{base_url}/the_vault")
        await page.screenshot(path="verification/11_the_vault_page.png")

        # 12. Nodes page
        await page.goto(f"{base_url}/nodes")
        await page.screenshot(path="verification/12_nodes_page.png")

        await browser.close()

asyncio.run(main())
