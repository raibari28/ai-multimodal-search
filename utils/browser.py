from playwright.sync_api import sync_playwright

def google_search_and_scrape(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.google.com/search?q={query}")
        page.wait_for_selector("h3")
        links = page.query_selector_all("h3")
        if links:
            links[0].click()
            page.wait_for_load_state("domcontentloaded")
            html = page.content()
            browser.close()
            return html
        browser.close()
    return None
