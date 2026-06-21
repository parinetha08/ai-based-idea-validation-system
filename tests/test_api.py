"""Unit tests for API endpoints and validation logic."""

from fastapi.testclient import TestClient
from app.backend.main import app

client = TestClient(app)


def test_home():
    """Test idea validation API response."""
    response = client.get("/")
    assert response.status_code == 200  # nosec B101
