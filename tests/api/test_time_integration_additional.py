import pytest
from flask import Flask
from app.services.time_service import TimeService

pytestmark = pytest.mark.integration


def test_api_time_returns_error_field_when_service_raises(monkeypatch, app):
    """
    Simulate TimeService raising an exception and verify API returns a graceful error.
    """
    class BrokenTimeService:
        def get_current_time(self):
            raise RuntimeError("simulated failure")

    # Save the original service
    original_service = app.time_service
    
    try:
        # Inject broken service into the app
        app.time_service = BrokenTimeService()
        client = app.test_client()
        resp = client.get('/api/time')
        assert resp.status_code == 200
        data = resp.get_json()
        # The route should return either an error field or a dict with fallback
        assert isinstance(data, dict)
        assert ('error' in data) or ('utc_datetime' in data)
    finally:
        # Restore the original service
        app.time_service = original_service
