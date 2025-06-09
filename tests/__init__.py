import os
import sys
import types

# Provide dummy environment variables for tests
os.environ.setdefault('OPENAI_API_KEY', 'test-key')
os.environ.setdefault('SERPAPI_KEY', 'test-key')

# Stub openai module if not installed
if 'openai' not in sys.modules:
    openai_module = types.ModuleType('openai')

    class DummyChatCompletions:
        def __init__(self):
            self.create = lambda *args, **kwargs: None

    class DummyChat:
        def __init__(self):
            self.completions = DummyChatCompletions()

    class DummyOpenAI:
        def __init__(self, api_key=None):
            self.chat = DummyChat()

    openai_module.OpenAI = DummyOpenAI
    sys.modules['openai'] = openai_module

# Stub trafilatura if missing
if 'trafilatura' not in sys.modules:
    trafilatura_module = types.ModuleType('trafilatura')
    def _extract(html, include_comments=False, include_tables=False):
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            if soup.body:
                return soup.body.get_text(separator='\n')
            return soup.get_text(separator='\n')
        except Exception:
            return None
    trafilatura_module.extract = _extract
    sys.modules['trafilatura'] = trafilatura_module

# Minimal stub for playwright.async_api to satisfy imports
if 'playwright.async_api' not in sys.modules:
    playwright_module = types.ModuleType('playwright')
    async_api_module = types.ModuleType('playwright.async_api')
    async_api_module.async_playwright = lambda: None
    playwright_module.async_api = async_api_module
    sys.modules['playwright'] = playwright_module
    sys.modules['playwright.async_api'] = async_api_module
