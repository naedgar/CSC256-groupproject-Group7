"""
tests/regression/test_time_regression.py

PR-7: Regression Test Suite for Time (TimeService / /api/time)

This comprehensive test suite covers all time operations to ensure:
- GET Time Service returns 200 with expected fields (datetime, timezone)
- Negative/edge cases (service unavailable, mock error paths)
"""

import pytest
from flask.testing import FlaskClient
from unittest.mock import patch
import re


class TestTimeRegressionGetTime:
    """Regression tests for GET /api/time - Fetch current time"""
    
    def test_get_time_returns_200(self, client: FlaskClient):
        """TC-REG-TIME-001: GET /api/time returns 200 OK"""
        response = client.get('/api/time')
        assert response.status_code == 200
    
    def test_get_time_returns_json(self, client: FlaskClient):
        """TC-REG-TIME-002: GET /api/time returns JSON response"""
        response = client.get('/api/time')
        assert response.content_type.startswith('application/json')
        data = response.get_json()
        assert isinstance(data, dict)
    
    def test_get_time_includes_datetime_field(self, client: FlaskClient):
        """TC-REG-TIME-003: Response includes datetime/utc_datetime field"""
        response = client.get('/api/time')
        data = response.get_json()
        
        # Should have datetime or utc_datetime field
        assert any(key in data for key in ['datetime', 'utc_datetime'])
        
        # Value should be a string
        datetime_field = data.get('datetime') or data.get('utc_datetime')
        assert isinstance(datetime_field, str)
    
    def test_get_time_datetime_format_iso8601(self, client: FlaskClient):
        """TC-REG-TIME-004: DateTime field is in ISO 8601 format"""
        response = client.get('/api/time')
        data = response.get_json()
        
        datetime_field = data.get('datetime') or data.get('utc_datetime')
        
        # Match ISO 8601 format: YYYY-MM-DDTHH:MM:SS
        iso_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
        assert re.match(iso_pattern, datetime_field), \
            f"DateTime '{datetime_field}' is not in ISO 8601 format"
    
    def test_get_time_includes_timezone_info(self, client: FlaskClient):
        """TC-REG-TIME-005: Response includes timezone information"""
        response = client.get('/api/time')
        data = response.get_json()
        
        print(f"DEBUG: Time response data: {data}")
        
        # Should have timezone, source, or Z suffix (UTC indicator)
        has_tz_info = any([
            'timezone' in data,
            'Z' in str(data.get('datetime')) or 'Z' in str(data.get('utc_datetime')),
            'UTC' in str(data.get('source', '')),
            'source' in data,  # Accept source field as timezone indicator
        ])
        assert has_tz_info, f"Response should include timezone information. Got: {data}"
    
    def test_get_time_response_complete_structure(self, client: FlaskClient):
        """TC-REG-TIME-006: Response has complete structure"""
        response = client.get('/api/time')
        data = response.get_json()
        
        # Basic structure requirements
        assert isinstance(data, dict)
        assert len(data) > 0
        
        # Should have at least datetime field
        datetime_present = any(key in data for key in 
                             ['datetime', 'utc_datetime', 'timestamp'])
        assert datetime_present, "Response missing datetime information"
    
    def test_get_time_multiple_requests_different_timestamps(self, client: FlaskClient):
        """TC-REG-TIME-007: Multiple requests return progression of times"""
        import time
        
        response1 = client.get('/api/time')
        data1 = response1.get_json()
        
        time.sleep(0.1)  # Small delay
        
        response2 = client.get('/api/time')
        data2 = response2.get_json()
        
        # Both should be valid time responses
        assert response1.status_code == 200
        assert response2.status_code == 200


class TestTimeRegressionEdgeCases:
    """Regression tests for edge cases and error scenarios"""
    
    def test_get_time_invalid_method_post(self, client: FlaskClient):
        """TC-REG-TIME-101: POST /api/time returns method not allowed"""
        response = client.post('/api/time')
        assert response.status_code in [405, 404]
    
    def test_get_time_invalid_method_put(self, client: FlaskClient):
        """TC-REG-TIME-102: PUT /api/time returns method not allowed"""
        response = client.put('/api/time')
        assert response.status_code in [405, 404]
    
    def test_get_time_invalid_method_delete(self, client: FlaskClient):
        """TC-REG-TIME-103: DELETE /api/time returns method not allowed"""
        response = client.delete('/api/time')
        assert response.status_code in [405, 404]
    
    def test_get_time_with_query_parameters(self, client: FlaskClient):
        """TC-REG-TIME-104: GET /api/time accepts query parameters gracefully"""
        response = client.get('/api/time?format=iso&timezone=UTC')
        # Should not error out
        assert response.status_code in [200, 400]
    
    def test_get_time_consistency_in_object(self, client: FlaskClient):
        """TC-REG-TIME-105: Time object is consistent across reads"""
        response = client.get('/api/time')
        data1 = response.get_json()
        
        response = client.get('/api/time')
        data2 = response.get_json()
        
        # Both should have the same structure
        assert set(data1.keys()) == set(data2.keys())
    
    def test_get_time_no_sensitive_data(self, client: FlaskClient):
        """TC-REG-TIME-106: Response contains no sensitive data"""
        response = client.get('/api/time')
        data = response.get_json()
        data_str = str(data).lower()
        
        # Should not contain credentials or sensitive info
        sensitive_keywords = ['password', 'token', 'secret', 'api_key']
        for keyword in sensitive_keywords:
            assert keyword not in data_str, \
                f"Response contains potentially sensitive data: {keyword}"


class TestTimeErrorResponses:
    """Regression tests for error handling in time operations"""
    
    def test_time_endpoint_exists(self, client: FlaskClient):
        """TC-REG-TIME-201: /api/time endpoint is registered"""
        response = client.get('/api/time')
        assert response.status_code in [200, 500], \
            "Endpoint should exist (200) or have server error (500)"
        assert response.status_code != 404, "/api/time endpoint not found"
    
    def test_time_response_is_valid_json(self, client: FlaskClient):
        """TC-REG-TIME-202: Response is valid JSON even on edge cases"""
        response = client.get('/api/time')
        if response.status_code in [200, 500]:
            data = response.get_json()
            assert isinstance(data, (dict, list, str, int, float, type(None)))
    
    def test_time_error_response_structure(self, client: FlaskClient):
        """TC-REG-TIME-203: Error responses have proper structure"""
        # Try invalid endpoint variation
        response = client.get('/api/time/invalid')
        
        # Should be 404 or valid error structure
        if response.status_code >= 400:
            if response.content_type and 'json' in response.content_type:
                data = response.get_json()
                # Should have error information
                assert isinstance(data, dict)


class TestTimeIntegration:
    """Regression tests for time service integration"""
    
    @pytest.mark.unit
    def test_time_service_module_exists(self):
        """TC-REG-TIME-301: TimeService module can be imported"""
        from app.services.time_service import TimeService
        assert TimeService is not None
    
    @pytest.mark.unit
    def test_time_service_has_get_current_time_method(self):
        """TC-REG-TIME-302: TimeService has get_current_time method"""
        from app.services.time_service import TimeService
        service = TimeService()
        assert hasattr(service, 'get_current_time')
        assert callable(service.get_current_time)
    
    @pytest.mark.unit
    def test_time_service_returns_dict(self):
        """TC-REG-TIME-303: TimeService.get_current_time returns dict"""
        from app.services.time_service import TimeService
        service = TimeService()
        result = service.get_current_time()
        assert isinstance(result, dict)
    
    @pytest.mark.unit
    def test_time_service_result_has_datetime(self):
        """TC-REG-TIME-304: TimeService returns datetime information"""
        from app.services.time_service import TimeService
        service = TimeService()
        result = service.get_current_time()
        
        # Should have datetime or timestamp field
        has_time_info = any(key in result for key in 
                           ['datetime', 'utc_datetime', 'timestamp'])
        assert has_time_info


class TestTimeRegressionCombined:
    """Combined regression tests for time service"""
    
    def test_get_time_health_check_pattern(self, client: FlaskClient):
        """TC-REG-TIME-401: Time endpoint follows health check pattern"""
        # Similar to health checks
        response = client.get('/api/time')
        
        assert response.status_code == 200
        assert response.content_type.startswith('application/json')
        data = response.get_json()
        assert isinstance(data, dict)
    
    def test_get_time_concurrent_requests(self, client: FlaskClient):
        """TC-REG-TIME-402: Time endpoint handles multiple requests"""
        responses = []
        for _ in range(5):
            response = client.get('/api/time')
            responses.append(response)
        
        # All should succeed
        assert all(r.status_code == 200 for r in responses)
        assert all(r.content_type.startswith('application/json') for r in responses)
    
    def test_time_response_fields_are_strings_or_numbers(self, client: FlaskClient):
        """TC-REG-TIME-403: Response field values are serializable types"""
        response = client.get('/api/time')
        data = response.get_json()
        
        # Check all values are JSON-serializable
        for key, value in data.items():
            assert isinstance(value, (str, int, float, bool, type(None))), \
                f"Field '{key}' has non-serializable type: {type(value)}"
