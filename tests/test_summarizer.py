import importlib
import os
import sys
import pytest

# Remove module from cache to force reimport

def test_summarizer_raises_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    sys.modules.pop("utils.summarizer", None)
    with pytest.raises(RuntimeError):
        import utils.summarizer  # noqa: F401


