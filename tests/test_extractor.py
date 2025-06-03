import sys, os
import pytest

# Ensure the repository root is on the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.extractor import extract_main_text


def test_extract_main_text_simple_html():
    html = "<html><head><title>Test</title></head><body><h1>Hello</h1><p>World</p></body></html>"
    result = extract_main_text(html)
    assert result.strip() == "Hello\nWorld"
