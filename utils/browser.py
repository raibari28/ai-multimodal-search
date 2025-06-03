from playwright.async_api import async_playwright

async def google_search_and_scrape(query):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(f"https://www.google.com/search?q={query}")
        await page.wait_for_selector("h3")
        links = await page.query_selector_all("h3")
        if links:
            await links[0].click()
            await page.wait_for_load_state("domcontentloaded")
            html = await page.content()
            await browser.close()
            return html
        await browser.close()
    return None
