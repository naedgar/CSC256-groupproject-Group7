"""
Development server with MockTimeService for testing with curl.

This server runs your Flask app but replaces the real TimeService with MockTimeService,
allowing you to test API endpoints with predictable mock data.

Usage:
    python test_helpers/dev_api_mock_server.py
    
Then test with curl:
    curl http://localhost:5000/api/time
    curl http://localhost:5000/time
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

# Import MockTimeService from conftest.py (reuse existing mock)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tests'))

class MockTimeService:
    """
    Mock implementation of TimeService that returns predictable time data.
    Used for unit and integration tests involving /api/time.
    """
    def get_current_time(self):
        return {
            "utc_datetime": "2025-08-06T17:40:00.000Z [MOCK DATA]",
            "source": "MockTimeService (Development Testing)"
        }

def create_mock_app():
    """Create Flask app with MockTimeService for development testing."""
    app = create_app()
    
    # Replace real TimeService with MockTimeService
    app.time_service = MockTimeService()
    
    print("🚀 Development server started with MockTimeService")
    print("⚠️  WARNING: Using MOCK data, not real external API!")
    print("📋 Test endpoints:")
    print("   • curl http://localhost:5000/api/time")
    print("   • curl http://localhost:5000/time") 
    print("   • Open http://localhost:5000/time in browser")
    print("🎯 Expected response: Fixed mock time (2025-08-06T17:40:00.000Z [MOCK DATA])")
    print("📝 Source will show: 'MockTimeService (Development Testing)'")
    print()
    print("💡 To use REAL external API, run: python -m flask run")
    
    return app

if __name__ == "__main__":
    app = create_mock_app()
    app.run(debug=True, port=5000)