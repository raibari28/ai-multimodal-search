from playwright.async_api import async_playwright

async def google_search_and_scrape(query):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ))
        await page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})
        await page.goto(f"https://www.google.com/search?q={query}", timeout=60000)
        html = await page.content()
        if "detected unusual traffic" in html or "I'm not a robot" in html or "Our systems have detected" in html:
            await browser.close()
            return None  # Google block or CAPTCHA
        try:
            await page.wait_for_selector("h3", timeout=10000)
            links = await page.query_selector_all("h3")
            if links:
                await links[0].click()
                await page.wait_for_load_state("domcontentloaded")
                html = await page.content()
                await browser.close()
                return html
        except Exception:
            html = await page.content()
            await browser.close()
            return None
        await browser.close()
    return None

async def duckduckgo_search_and_scrape(query):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ))
        await page.goto(f"https://duckduckgo.com/?q={query}", timeout=60000)
        # Wait longer, print HTML for debugging if needed
        try:
            await page.wait_for_selector("a.result__a", timeout=30000)
            links = await page.query_selector_all("a.result__a")
            if not links:
                # Fallback to all links if DuckDuckGo layout changed
                links = await page.query_selector_all("a[href]")
            if links:
                await links[0].click()
                await page.wait_for_load_state("domcontentloaded")
                html = await page.content()
                await browser.close()
                return html
            else:
                html = await page.content()
                print("NO DUCKDUCKGO RESULTS HTML:", html[:1000])
                await browser.close()
                return None
        except Exception as e:
            html = await page.content()
            print("DUCKDUCKGO ERROR HTML:", html[:1000])
            await browser.close()
            return None
