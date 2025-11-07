"""
Pytest-Playwright Built-in Fixtures Demo

This file demonstrates the advanced features of pytest-playwright:
- Built-in fixtures (no custom fixture definitions needed)
- Automatic video recording on test failure
- Screenshot capture capabilities
- Professional reporting integration
- Zero-configuration browser management

These are the "industry standard" features mentioned in the labs.

HOW TO RUN:
    .\\.venv\\Scripts\\python.exe -m pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v

HOW TO RUN WITH VIDEO RECORDING:
    .\\.venv\\Scripts\\python.exe -m pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v --video=on

HOW TO RUN WITH HEADED MODE (visible browser):
    .\\.venv\\Scripts\\python.exe -m pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v --headed

HOW TO RUN WITH HTML REPORT:
    .\\.venv\\Scripts\\python.exe -m pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v --html=test-results/report.html --self-contained-html
"""

import pytest
import time
import os

# Configuration
BASE_URL = "http://localhost:5000"
LEARNING_MODE = os.environ.get('LEARNING_MODE', 'false').lower() == 'true'


def test_add_task_with_builtin_fixtures(page):
    """
    RF014-US003-UI: Add task using pytest-playwright built-in fixtures.
    
    This test uses the built-in 'page' fixture provided by pytest-playwright.
    No custom fixture definitions needed!
    
    Built-in features:
    - Automatic browser/page management
    - Video recording on failure (with --video=on)
    - Screenshot capture on failure
    - Professional reporting integration
    """
    print("\n🧪 Testing with pytest-playwright built-in fixtures")
    
    # Step 1: Navigate to add task page
    print("🌐 Step 1: Navigating to add task page...")
    page.goto(f"{BASE_URL}/tasks/new")
    
    if LEARNING_MODE:
        time.sleep(1)
    
    # Step 2: Fill in the form
    print("📝 Step 2: Filling in task details...")
    page.fill('input[name="title"]', "Built-in Fixtures Task")
    page.fill('input[name="description"]', "Created using pytest-playwright built-in fixtures")
    
    if LEARNING_MODE:
        print("   ✏️ Filled title: 'Built-in Fixtures Task'")
        print("   ✏️ Filled description: 'Created using pytest-playwright built-in fixtures'")
        time.sleep(1)
    
    # Step 3: Submit the form
    print("🚀 Step 3: Submitting the form...")
    page.click('button[type="submit"]')
    
    # Step 4: Wait for redirection
    print("⏳ Step 4: Waiting for redirection...")
    page.wait_for_url(lambda url: url.endswith("/tasks") or "/tasks?" in url, timeout=10000)
    
    if LEARNING_MODE:
        print(f"   🔗 Redirected to: {page.url}")
        time.sleep(1)
    
    # Step 5: Verify task appears in list
    print("🔍 Step 5: Verifying task appears in list...")
    page_content = page.content()
    
    assert "Built-in Fixtures Task" in page_content, "Task title should be visible in task list"
    assert "Created using pytest-playwright built-in fixtures" in page_content, "Task description should be visible"
    
    if LEARNING_MODE:
        print("   ✅ Task title found in page")
        print("   ✅ Task description found in page")
        time.sleep(2)
    
    print("✅ Built-in fixtures test PASSED!")


def test_screenshot_on_success(page):
    """
    RF014-US003-UI: Demonstrate screenshot capture capability.
    
    This test shows how to manually take screenshots using built-in features.
    """
    print("\n🧪 Testing screenshot capabilities")
    
    # Navigate to tasks page
    page.goto(f"{BASE_URL}/tasks")
    
    # Take a screenshot (saved to test-results/ directory)
    page.screenshot(path="test-results/manual-screenshot.png")
    print("📸 Screenshot saved to test-results/manual-screenshot.png")
    
    # Verify we're on the right page
    assert "Task Tracker" in page.content()
    print("✅ Screenshot test PASSED!")


def test_browser_context_features(page, context):
    """
    RF014-US003-UI: Demonstrate browser context features.
    
    This test shows access to browser context for advanced features.
    """
    print("\n🧪 Testing browser context features")
    
    # Access browser context for advanced features
    print(f"🌐 Browser context: {context}")
    print(f"📱 Page: {page}")
    
    # Navigate and verify
    page.goto(f"{BASE_URL}/api/health")
    
    # Verify health endpoint
    page_content = page.content()
    assert "healthy" in page_content.lower() or "ok" in page_content.lower()
    print("✅ Browser context test PASSED!")


def test_multiple_pages_same_context(context):
    """
    RF014-US003-UI: Demonstrate multiple pages in same context.
    
    This test shows how to create multiple pages within the same browser context.
    """
    print("\n🧪 Testing multiple pages in same context")
    
    # Create first page
    page1 = context.new_page()
    page1.goto(f"{BASE_URL}/tasks")
    
    # Create second page
    page2 = context.new_page()
    page2.goto(f"{BASE_URL}/api/health")
    
    # Verify both pages
    assert "Task Tracker" in page1.content()
    assert "healthy" in page2.content().lower() or "ok" in page2.content().lower()
    
    print("✅ Multiple pages test PASSED!")


def test_cross_browser_with_builtin(page):
    """
    RF014-US003-UI: Cross-browser testing with built-in fixtures.
    
    This test uses pytest-playwright's built-in fixtures.
    Run with different browsers using: --browser chromium --browser firefox
    """
    print(f"\\n🧪 Testing with pytest-playwright built-in fixtures")
    
    # Navigate to add task page
    page.goto(f"{BASE_URL}/tasks/new")
    
    # Fill and submit form
    page.fill('input[name="title"]', f"Cross-browser Task")
    page.fill('input[name="description"]', f"Created with pytest-playwright")
    page.click('button[type="submit"]')
    
    # Verify redirection
    page.wait_for_url(lambda url: url.endswith("/tasks") or "/tasks?" in url, timeout=10000)
    
    # Verify task appears
    page_content = page.content()
    assert f"Cross-browser Task" in page_content
    
    print(f"✅ Cross-browser test PASSED!")


def test_deliberately_failing_test(page):
    """
    RF014-US999-DEMO: This test is designed to fail to demonstrate video recording.
    
    When run with --video=on, this will create a video showing the failure.
    
    Run with: pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py::test_deliberately_failing_test -v --video=on
    """
    print("\n🧪 Testing video recording on failure (this test will fail intentionally)")
    
    # Navigate to tasks page
    page.goto(f"{BASE_URL}/tasks")
    
    # Take a screenshot before failure
    page.screenshot(path="test-results/before-failure.png")
    
    # This will fail intentionally to demonstrate video recording
    assert "This text definitely does not exist on the page" in page.content(), "Intentional failure to demo video recording"


if __name__ == "__main__":
    print("💡 To run these tests with built-in pytest-playwright features:")
    print("   # Basic run:")
    print("   pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v")
    print("")
    print("   # With video recording on failure:")
    print("   pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v --video=on")
    print("")
    print("   # With visible browser (headed mode):")
    print("   pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v --headed")
    print("")
    print("   # With HTML report:")
    print("   pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v --html=test-results/report.html --self-contained-html")
    print("")
    print("   # Cross-browser testing:")
    print("   pytest tests/acceptance/bdd_playwright/test_playwright_builtin_fixtures.py -v --browser chromium --browser firefox")
    print("")
    print("🎯 These demonstrate the 'industry standard' features mentioned in the labs!")
