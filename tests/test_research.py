import sys
import os
import importlib
from fastapi.testclient import TestClient


def test_research_returns_500_when_keys_missing(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("SERPAPI_KEY", raising=False)
    import api.research as research
    client = TestClient(research.app)
    response = client.post("/research", json={"text": "test"})
    assert response.status_code == 500
    assert "OPENAI_API_KEY" in response.json()["detail"]

