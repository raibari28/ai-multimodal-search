import sys, os
import types
import asyncio
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import browser

class DummyLink:
    def __init__(self, page):
        self.page = page
    async def click(self):
        self.page.clicked = True

class DummyPage:
    def __init__(self, final_html, unusual=False, raise_exc=False, no_links=False):
        self.final_html = final_html
        self.unusual = unusual
        self.raise_exc = raise_exc
        self.no_links = no_links
        self.goto_url = None
        self.clicked = False

    async def set_extra_http_headers(self, headers):
        pass

    async def goto(self, url, timeout=60000):
        self.goto_url = url

    async def content(self):
        if not self.clicked:
            if self.unusual:
                return "detected unusual traffic"
            return "<html>results</html>"
        return self.final_html

    async def wait_for_selector(self, selector, timeout=10000):
        if self.raise_exc:
            raise Exception("selector not found")

    async def query_selector_all(self, selector):
        if self.no_links:
            return []
        return [DummyLink(self)]

    async def wait_for_load_state(self, state):
        pass

class DummyBrowser:
    def __init__(self, page):
        self.page = page
    async def new_page(self, user_agent):
        return self.page
    async def close(self):
        pass

class DummyPlaywright:
    def __init__(self, page):
        self.page = page
    @property
    def chromium(self):
        return self
    async def launch(self, headless=True):
        return DummyBrowser(self.page)

class DummyContext:
    def __init__(self, page):
        self.playwright = DummyPlaywright(page)
    async def __aenter__(self):
        return self.playwright
    async def __aexit__(self, exc_type, exc, tb):
        pass

def make_async_playwright(page):
    def _async_playwright():
        return DummyContext(page)
    return _async_playwright

def test_google_search_success(monkeypatch):
    page = DummyPage('<final>content</final>')
    monkeypatch.setattr(browser, 'async_playwright', make_async_playwright(page))
    result = asyncio.run(browser.google_search_and_scrape('foo'))
    assert page.goto_url.endswith('foo')
    assert result == '<final>content</final>'

def test_google_search_blocked(monkeypatch):
    page = DummyPage('<final>', unusual=True)
    monkeypatch.setattr(browser, 'async_playwright', make_async_playwright(page))
    result = asyncio.run(browser.google_search_and_scrape('foo'))
    assert result is None

def test_google_search_error(monkeypatch):
    page = DummyPage('<final>', raise_exc=True)
    monkeypatch.setattr(browser, 'async_playwright', make_async_playwright(page))
    result = asyncio.run(browser.google_search_and_scrape('foo'))
    assert result is None
