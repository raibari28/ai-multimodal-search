import trafilatura
from bs4 import BeautifulSoup

def extract_main_text(html):
    if not html:
        return ""
    text = trafilatura.extract(html, include_comments=False, include_tables=False)
    if text:
        return text
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n")
