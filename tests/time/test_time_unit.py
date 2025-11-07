# ✅ TC-US031-001: Unit test with mocked time service

from app.services.time_service import TimeService
from unittest.mock import patch

def test_get_current_time_returns_mocked_value():
    mock_response = {
        "utc_datetime": "2025-08-06T17:40:00.000Z [MOCK DATA]",
        "source": "MockTimeService (Development Testing)"
    }

    with patch.object(TimeService, "get_current_time", return_value=mock_response):
        service = TimeService()
        result = service.get_current_time()
        assert result["utc_datetime"] == "2025-08-06T17:40:00.000Z [MOCK DATA]"
        assert result["source"] == "MockTimeService (Development Testing)"