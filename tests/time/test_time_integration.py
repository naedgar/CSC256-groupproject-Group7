import pytest
from app import create_app
from flask import Flask

pytestmark = pytest.mark.integration

# Import MockTimeService from the tests conftest module
# This mock service is defined in tests/conftest.py for predictable testing

@pytest.fixture
def app(mock_time_service) -> Flask:
    """
    Use MockTimeService for integration testing.

    This avoids hitting the real external API and allows predictable test results.
    """
    app = create_app()
    app.time_service = mock_time_service  # Inject mock
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Test client that uses the app with mocked time service."""
    return app.test_client()

def test_get_time_route_returns_mocked_value(client):
    """
    ✅ TC-US031-003: Integration test for GET /api/time route using MockTimeService

    Description:
    Uses mock data to test the /api/time route without making an actual HTTP request.

    Expected Result:
    - Status code: 200
    - Response contains the predictable mocked UTC time with [MOCK DATA] indicator
    - Response contains source indicating it's from MockTimeService
    """
    response = client.get("/api/time")
    assert response.status_code == 200

    data = response.get_json()
    assert data["utc_datetime"] == "2025-08-06T17:40:00.000Z [MOCK DATA]"
    assert data["source"] == "MockTimeService (Development Testing)"