import importlib
import os
import sys
import pytest
import types
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import summarizer

class DummyResponse:
    def __init__(self, content):
        self.choices = [types.SimpleNamespace(message=types.SimpleNamespace(content=content))]


def test_gpt_generate_query(monkeypatch):
    def fake_create(*args, **kwargs):
        return DummyResponse('search query')
    monkeypatch.setattr(summarizer.client.chat.completions, 'create', fake_create)
    assert summarizer.gpt_generate_query('anything') == 'search query'


def test_gpt_summarize(monkeypatch):
    def fake_create(*args, **kwargs):
        return DummyResponse('summary text')
    monkeypatch.setattr(summarizer.client.chat.completions, 'create', fake_create)
    assert summarizer.gpt_summarize('text to summarize') == 'summary text'


def test_gpt_summarize_no_text(monkeypatch):
    calls = []

    def fake_create(*args, **kwargs):
        calls.append(1)
        return DummyResponse('should not be used')

    monkeypatch.setattr(summarizer.client.chat.completions, 'create', fake_create)
    result = summarizer.gpt_summarize('')
    assert result == 'No article text available.'
    assert not calls
