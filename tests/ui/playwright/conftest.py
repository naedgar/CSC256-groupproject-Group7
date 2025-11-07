"""
Playwright Test Configuration and Fixtures

This file provides shared Playwright fixtures for all Playwright tests.
Follows pytest best practices for fixture organization.

Features:
- Session-scoped Playwright instance
- Multi-browser support (Chrome, Firefox, Safari)
- Configurable headless/visual modes
- Automatic cleanup
- CI/CD friendly configurations
- Learning mode for development

STUDENT NOTE:
This is the recommended place for Playwright-specific fixtures and shared config (like BASE_URL, LEARNING_MODE).
All Playwright UI tests should use fixtures from this file for browser setup and configuration.
This keeps your browser automation isolated from global test setup in tests/conftest.py.

HOW TO RUN FROM ROOT DIRECTORY:
    .\\.venv\\Scripts\\python.exe -m pytest tests/ui/playwright/ -v
    .\\.venv\\Scripts\\python.exe -m pytest tests/ui/playwright/pytest/ -v
    .\\.venv\\Scripts\\python.exe -m pytest tests/ui/playwright/standalone/ -v
"""

import pytest
import os

# Playwright is an optional dependency for running UI tests. If it's not
# installed in the environment (for example a minimal CI/test environment
# or when the developer doesn't want browser tests), skip the entire
# Playwright test collection instead of causing an import error.
try:
    from playwright.sync_api import sync_playwright
except ModuleNotFoundError:
    # Skip this module at collection time when Playwright is not available
    pytest.skip("Playwright not installed - skipping Playwright UI tests", allow_module_level=True)

@pytest.fixture(scope="session")
def learning_mode():
    return LEARNING_MODE

# Configuration
# LEARNING_MODE controls whether Playwright runs in visual (browser) mode or headless mode.
# Set the environment variable LEARNING_MODE=true for visual mode (browser opens).
# Set LEARNING_MODE=false (or leave unset) for headless mode (no browser window).
LEARNING_MODE = os.environ.get('LEARNING_MODE', 'false').lower() == 'true'
BASE_URL = "http://localhost:5000"
IS_CI = os.environ.get('GITHUB_ACTIONS') == 'true' or os.environ.get('CI') == 'true'


@pytest.fixture(scope="session")
def playwright_instance():
    """
    Session-scoped fixture to manage Playwright instance.
    
    This ensures Playwright is properly initialized and cleaned up
    across all Playwright tests in the session.
    """
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser_launch_options():
    """
    Centralized browser launch configuration.
    
    This makes it easy to adjust settings across all browsers.
    """
    if LEARNING_MODE and not IS_CI:
        # Visual mode - perfect for development and debugging
        return {
            "headless": False,
            "slow_mo": 500,  # Slow down actions for learning
            "devtools": False,  # Set to True for debugging
        }
    else:
        # CI or headless mode - production ready
        return {
            "headless": True,
            "args": [
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-extensions",
                "--disable-web-security",  # Useful for CORS testing
            ]
        }


@pytest.fixture
def chrome_page(playwright_instance, browser_launch_options):
    """
    Chrome browser page fixture for Playwright tests.
    
    Automatically handles browser lifecycle and cleanup.
    """
    print(f"\\n🌐 Chrome Browser - {'Visual' if not browser_launch_options['headless'] else 'Headless'} Mode")
    
    browser = playwright_instance.chromium.launch(**browser_launch_options)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        # Add any additional context options here
        record_video_dir="test-results/videos/" if LEARNING_MODE else None,
        record_video_size={"width": 1280, "height": 720} if LEARNING_MODE else None,
    )
    page = context.new_page()
    
    yield page
    
    # Cleanup
    context.close()
    browser.close()
    print("✅ Chrome browser cleanup completed")


@pytest.fixture
def firefox_page(playwright_instance, browser_launch_options):
    """
    Firefox browser page fixture for Playwright tests.
    """
    print(f"\\n🦊 Firefox Browser - {'Visual' if not browser_launch_options['headless'] else 'Headless'} Mode")
    
    # Firefox-specific launch options
    firefox_options = browser_launch_options.copy()
    # Remove Chrome-specific args for Firefox
    if 'args' in firefox_options:
        firefox_options['args'] = [arg for arg in firefox_options['args'] 
                                if arg not in ['--no-sandbox', '--disable-dev-shm-usage']]
    
    browser = playwright_instance.firefox.launch(**firefox_options)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir="test-results/videos/" if LEARNING_MODE else None,
        record_video_size={"width": 1280, "height": 720} if LEARNING_MODE else None,
    )
    page = context.new_page()
    
    yield page
    
    # Cleanup
    context.close()
    browser.close()
    print("✅ Firefox browser cleanup completed")


@pytest.fixture
def webkit_page(playwright_instance, browser_launch_options):
    """
    WebKit (Safari) browser page fixture for Playwright tests.
    
    Note: WebKit requires additional setup on some systems.
    """
    print(f"\\n🧭 WebKit Browser - {'Visual' if not browser_launch_options['headless'] else 'Headless'} Mode")
    
    # WebKit-specific launch options
    webkit_options = browser_launch_options.copy()
    # Remove Chrome-specific args for WebKit
    if 'args' in webkit_options:
        webkit_options.pop('args', None)
    
    try:
        browser = playwright_instance.webkit.launch(**webkit_options)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir="test-results/videos/" if LEARNING_MODE else None,
            record_video_size={"width": 1280, "height": 720} if LEARNING_MODE else None,
        )
        page = context.new_page()
        
        yield page
        
        # Cleanup
        context.close()
        browser.close()
        print("✅ WebKit browser cleanup completed")
        
    except Exception as e:
        pytest.skip(f"WebKit browser not available: {e}")


@pytest.fixture(params=['chrome', 'firefox'])
def multi_browser_page(request, chrome_page, firefox_page):
    """
    Parametrized fixture that runs tests on multiple browsers.
    
    Usage:
    def test_something(multi_browser_page):
        # This test will run on both Chrome and Firefox
        multi_browser_page.goto("/tasks")
    """
    if request.param == 'chrome':
        return chrome_page
    elif request.param == 'firefox':
        return firefox_page


@pytest.fixture(autouse=True)
def setup_playwright_test_environment():
    """
    Automatically sets up and tears down Playwright test environment.
    
    This runs before every Playwright test to ensure clean state.
    """
    # Pre-test setup
    print("🔄 Setting up Playwright test environment...")
    
    # Create test results directory
    os.makedirs("test-results/videos", exist_ok=True)
    os.makedirs("test-results/screenshots", exist_ok=True)
    
    yield  # Run the test
    
    # Post-test cleanup
    print("🧹 Playwright test environment cleanup completed")


@pytest.fixture(scope="session")
def app_base_url():
    """
    Provides the base URL for the application under test.
    
    This can be overridden via environment variable for different environments.
    Note: Named app_base_url to avoid conflict with pytest-base-url plugin.
    """
    return os.environ.get('BASE_URL', BASE_URL)


# Server health check (similar to API tests)
@pytest.fixture(autouse=True, scope="session")
def verify_playwright_server():
    """
    Verify the server is running before Playwright tests.
    
    This prevents Playwright tests from failing due to server issues.
    """
    try:
        import requests
        response = requests.get(f"{BASE_URL}/api/health", timeout=5)
        if response.status_code != 200:
            pytest.skip(f"Server health check failed: {response.status_code}")
    except Exception as e:
        pytest.skip(f"Server not available for Playwright tests: {e}")