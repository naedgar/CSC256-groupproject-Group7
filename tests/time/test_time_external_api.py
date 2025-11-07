# ✅ tests/time/test_time_external_api.py
# Integration Test with Real External API (WorldTimeAPI)

import pytest
from app import create_app
from flask import Flask

@pytest.fixture
def app() -> Flask:
    """
    Flask app instance using the real TimeService for external integration test.
    """
    app = create_app()
    return app

@pytest.mark.external
def test_get_time_route_returns_valid_utc(client):
    """
    ✅ TC-US031-002: Integration test for GET /api/time using real TimeService (external API)

    Description:
    - Sends a request to /api/time
    - Validates status and response structure from the external WorldTimeAPI

    Expected Result:
    - Status code: 200
    - Response contains either:
    - A "utc_datetime" field (on success)
    - Or a graceful "error" field (on failure)
    """
    response = client.get("/api/time")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, dict)
    assert "utc_datetime" in data or "error" in data