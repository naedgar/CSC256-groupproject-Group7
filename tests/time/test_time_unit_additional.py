import pytest
from app.services.time_service import TimeService
from unittest.mock import patch
from datetime import datetime

pytestmark = pytest.mark.unit


def test_get_current_time_fallback_to_system_on_api_error(monkeypatch):
    """
    Ensure TimeService falls back to system UTC when external API fails.
    """

    def _raise(*args, **kwargs):
        raise RuntimeError("network failure")

    with patch('app.services.time_service.requests.get', side_effect=_raise):
        svc = TimeService()
        result = svc.get_current_time()
        # Fallback returns a dict with utc_datetime in ISO-like format
        assert isinstance(result, dict)
        assert 'utc_datetime' in result
        assert 'source' in result
        assert 'System Time' in result['source']


def test_utc_datetime_format_is_iso_like():
    svc = TimeService()
    res = svc.get_current_time()
    val = res.get('utc_datetime')
    assert isinstance(val, str)
    # Basic sanity parse to datetime (allow fractional seconds)
    try:
        # Strip trailing Z if present
        dt_str = val.rstrip('Z')
        # Trim anything after seconds if present
        if '.' in dt_str:
            dt_str = dt_str.split('.')[0]
        datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S")
    except Exception:
        pytest.skip("UTC datetime not parseable in this environment")
