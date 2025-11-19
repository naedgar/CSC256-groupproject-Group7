# db_reset_helper.py - Helper for database reset

"""
🎭 db_reset_helper.py provides shared test environment setup and database reset logic for all test types,
including BDD (pytest-bdd), standalone UI tests (Selenium, Playwright), and other scripts that do not use pytest's configuration.

Key Features:
- Centralized database reset for test isolation across BDD, standalone, and UI tests
- Flask app integration and health check for live server testing
- Support for both Selenium and Playwright test suites
- Environment variable configuration for CI and local development
- Fallback mechanisms for direct file/database cleanup if API reset is unavailable

Environment Variables:
- CI=true: Enables headless mode for browser tests
- TESTING=true: Enables test mode for Flask app
"""

import os
import sys
import json
import requests
import time
from pathlib import Path

# Add app to Python path for imports
sys.path.insert(0, os.path.abspath('.'))

# Configuration
BASE_URL = "http://localhost:5000"
TASKS_FILE = os.path.join("app", "data", "tasks.json")

# Cross-platform database file path
import tempfile
DATABASE_FILE = os.path.join(tempfile.gettempdir(), "tasks.db") if os.getenv("TESTING") == "true" else "tasks.db"

def reset_database_state():
    """
    Reset the database state for BDD test isolation.
    This function is called before each scenario to ensure clean state.
    """
    try:
        # First, try to reset via API endpoint (preferred)
        response = requests.post(f"{BASE_URL}/api/tasks/reset", timeout=5)
        if response.status_code == 200:
            print("✅ Database reset via API successful")
            return True
        else:
            print(f"⚠️ API reset failed with status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ API reset failed: {e}")
    
    # Fallback to direct file cleanup
    print("🔄 Falling back to direct file cleanup...")
    return direct_database_cleanup()

def direct_database_cleanup():
    """
    Direct database cleanup as fallback when API is not available.
    Cleans both JSON file storage and SQLite database.
    """
    try:
        # Clean JSON file storage
        os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
        print("✅ JSON file reset successful")
        
        # Clean SQLite database
        if os.path.exists(DATABASE_FILE):
            try:
                os.remove(DATABASE_FILE)
                print("✅ SQLite database file removed")
            except PermissionError:
                # Windows file handle delay
                time.sleep(0.1)
                try:
                    os.remove(DATABASE_FILE)
                    print("✅ SQLite database file removed (retry)")
                except PermissionError:
                    print("⚠️ Could not remove database file (still in use)")
                    pass
        
        return True
    except Exception as e:
        print(f"❌ Direct cleanup failed: {e}")
        return False

def verify_flask_app():
    """
    Verify that the Flask application is running and accessible.
    This is called before the test suite starts.
    """
    max_retries = 10
    for attempt in range(max_retries):
        try:
            response = requests.get(f"{BASE_URL}/api/health", timeout=5)
            if response.status_code == 200:
                print("✅ Flask application is accessible")
                return True
        except requests.exceptions.RequestException:
            if attempt < max_retries - 1:
                print(f"⏳ Waiting for Flask app... (attempt {attempt + 1}/{max_retries})")
                time.sleep(2)
            else:
                print("❌ Flask application is not accessible!")
                print("💡 Make sure to start the Flask app: python -m app.main")
                return False
    return False

# Environment setup for CI vs local development
def setup_test_environment():
    """
    Configure test environment based on CI/local settings.
    """
    # Set testing environment variables
    os.environ.setdefault('TESTING', 'true')
    os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')
    
    # CI-specific configuration
    if os.environ.get('CI', 'false').lower() == 'true':
        print("🚀 Running in CI environment (headless mode)")
        os.environ['HEADLESS'] = 'true'
    else:
        print("🖥️ Running in local development environment")
    
    print(f"🔧 Test environment configured:")
    print(f"   - TESTING: {os.environ.get('TESTING')}")
    print(f"   - CI: {os.environ.get('CI', 'false')}")
    print(f"   - HEADLESS: {os.environ.get('HEADLESS', 'false')}")

# Main setup function called by pytest-bdd
if __name__ == "__main__":
    setup_test_environment()
    if verify_flask_app():
        print("🎭 BDD test environment ready!")
    else:
        sys.exit(1)