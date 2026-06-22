"""Unit tests for API endpoints."""

# ruff: noqa: E402
from unittest.mock import MagicMock
import sys
from fastapi.testclient import TestClient
from app.backend.main import app

sys.modules["google.adk"] = MagicMock()
sys.modules["google.adk.agents"] = MagicMock()
sys.modules["google.adk.tools"] = MagicMock()

client = TestClient(app)


def test_home() -> None:
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200  # nosec B101
