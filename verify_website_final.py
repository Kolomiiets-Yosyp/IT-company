import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        base_url = "http://127.0.0.1:8000"

        # 1. Home page
        await page.goto(base_url)
        await page.screenshot(path="verification/01_home_page_final.png", full_page=True)

        # 2. Solutions page
        await page.goto(f"{base_url}/solutions")
        await page.screenshot(path="verification/02_solutions_page_final.png", full_page=True)

        # 3. The Lab page
        await page.goto(f"{base_url}/lab")
        await page.screenshot(path="verification/03_lab_page_final.png", full_page=True)

        # 4. About page (was 'Connect' before)
        await page.goto(f"{base_url}/about")
        await page.screenshot(path="verification/04_about_page_final.png", full_page=True)

        # 5. Connect page (was contact form)
        await page.goto(f"{base_url}/connect")
        await page.screenshot(path="verification/05_connect_page_final.png", full_page=True)

        # 6. Build page (new content)
        await page.goto(f"{base_url}/build")
        await page.screenshot(path="verification/06_build_page_final.png", full_page=True)

        # 7. Grid page (new content)
        await page.goto(f"{base_url}/grid")
        await page.screenshot(path="verification/07_grid_page_final.png", full_page=True)

        # 8. Core page (new content)
        await page.goto(f"{base_url}/core")
        await page.screenshot(path="verification/08_core_page_final.png", full_page=True)

        # 9. Directory page (new content)
        await page.goto(f"{base_url}/directory")
        await page.screenshot(path="verification/09_directory_page_final.png", full_page=True)

        # 10. The Vault page (new content)
        await page.goto(f"{base_url}/the_vault")
        await page.screenshot(path="verification/10_the_vault_page_final.png", full_page=True)

        # 11. Nodes page (new content)
        await page.goto(f"{base_url}/nodes")
        await page.screenshot(path="verification/11_nodes_page_final.png", full_page=True)

        await browser.close()

asyncio.run(main())
