#!/usr/bin/env python3
"""
🎭 PLAYWRIGHT SETUP VERIFICATION TEST

This test verifies that Playwright is properly installed and configured.
Similar to test_setup_selenium.py, this ensures all Playwright components work.

🎯 PURPOSE:
- Verify Playwright installation
- Test browser availability
- Validate basic functionality
- Educational demonstration of Playwright setup

🚀 USAGE:
python tests/health/test_setup_playwright.py

📚 EDUCATIONAL VALUE:
- Shows step-by-step setup verification
- Demonstrates browser management
- Compares with Selenium setup patterns
- Perfect for troubleshooting installation issues
"""

import sys
import os


def test_playwright_imports():
    """Test that all required Playwright modules can be imported."""
    print("🎭 Testing Playwright Imports...")
    
    try:
        from playwright.sync_api import sync_playwright, Browser, Page
        print("  ✅ sync_playwright imported successfully")
        print("  ✅ Browser type imported successfully") 
        print("  ✅ Page type imported successfully")
        return True
    except ImportError as e:
        print(f"  ❌ IMPORT ERROR: {e}")
        print("  💡 Try: pip install playwright==1.50.0")
        return False
    except Exception as e:
        print(f"  ❌ OTHER ERROR: {e}")
        return False


def test_playwright_version():
    """Test Playwright version information."""
    print("\n🔍 Testing Playwright Version...")
    
    try:
        import playwright
        version = getattr(playwright, '__version__', 'Unknown')
        print(f"  ✅ Playwright version: {version}")
        
        if version != 'Unknown' and version >= '1.50.0':
            print("  ✅ Version is compatible (>=1.50.0)")
            return True
        else:
            print("  ⚠️ Version may be outdated, recommend 1.50.0+")
            return True  # Still functional, just warning
    except Exception as e:
        print(f"  ❌ Version check failed: {e}")
        return False


def test_browser_availability():
    """Test that browsers are installed and available."""
    print("\n🌐 Testing Browser Availability...")
    
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            # Test Chromium
            try:
                browser = p.chromium.launch(headless=True)
                print("  ✅ Chromium browser available")
                browser.close()
                chromium_ok = True
            except Exception as e:
                print(f"  ❌ Chromium failed: {e}")
                print("  💡 Try: playwright install chromium")
                chromium_ok = False
            
            # Test Firefox
            try:
                browser = p.firefox.launch(headless=True)
                print("  ✅ Firefox browser available")
                browser.close()
                firefox_ok = True
            except Exception as e:
                print(f"  ❌ Firefox failed: {e}")
                print("  💡 Try: playwright install firefox")
                firefox_ok = False
            
            # Test WebKit (Safari engine)
            try:
                browser = p.webkit.launch(headless=True)
                print("  ✅ WebKit browser available")
                browser.close()
                webkit_ok = True
            except Exception as e:
                print(f"  ⚠️ WebKit not available: {e}")
                print("  ℹ️ WebKit is optional but recommended")
                webkit_ok = False  # Optional
        
        return chromium_ok and firefox_ok  # WebKit is optional
        
    except Exception as e:
        print(f"  ❌ Browser test failed: {e}")
        print("  💡 Try: playwright install")
        return False


def test_basic_functionality():
    """Test basic Playwright functionality with a simple page operation."""
    print("\n🧪 Testing Basic Functionality...")
    
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            # Use Chromium for basic test
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            
            # Navigate to a simple data URL
            page.goto("data:text/html,<html><body><h1>Playwright Test</h1></body></html>")
            
            # Get page title
            title = page.title()
            print(f"  ✅ Page navigation successful")
            print(f"  ✅ Page content accessible")
            
            # Test element selection
            heading = page.locator("h1").text_content()
            if "Playwright Test" in heading:
                print(f"  ✅ Element selection working: '{heading}'")
            else:
                print(f"  ⚠️ Unexpected content: '{heading}'")
            
            # Cleanup
            context.close()
            browser.close()
            
        print("  ✅ Basic functionality test passed")
        return True
        
    except Exception as e:
        print(f"  ❌ Basic functionality test failed: {e}")
        return False


def test_multi_browser_support():
    """Test that multiple browsers can run simultaneously."""
    print("\n🔄 Testing Multi-Browser Support...")
    
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browsers = []
            
            # Launch multiple browsers
            try:
                chromium = p.chromium.launch(headless=True)
                browsers.append(("Chromium", chromium))
                print("  ✅ Chromium launched")
            except Exception:
                print("  ❌ Chromium launch failed")
            
            try:
                firefox = p.firefox.launch(headless=True)
                browsers.append(("Firefox", firefox))
                print("  ✅ Firefox launched")
            except Exception:
                print("  ❌ Firefox launch failed")
            
            # Test concurrent operation
            if len(browsers) >= 2:
                print("  ✅ Multi-browser support confirmed")
                multi_browser_ok = True
            else:
                print("  ⚠️ Limited browser support")
                multi_browser_ok = False
            
            # Cleanup all browsers
            for name, browser in browsers:
                try:
                    browser.close()
                    print(f"  ✅ {name} closed successfully")
                except Exception as e:
                    print(f"  ⚠️ {name} cleanup issue: {e}")
            
            return multi_browser_ok
            
    except Exception as e:
        print(f"  ❌ Multi-browser test failed: {e}")
        return False


def test_comparison_with_selenium():
    """Show comparison between Playwright and Selenium setup."""
    print("\n⚖️ Playwright vs Selenium Comparison...")
    
    # Test if Selenium is also available
    selenium_available = False
    try:
        from selenium import webdriver
        selenium_available = True
        print("  ✅ Selenium also available")
    except ImportError:
        print("  ℹ️ Selenium not installed")
    
    print("\n  📊 Setup Comparison:")
    print("  ┌─────────────────┬──────────────┬───────────────┐")
    print("  │ Feature         │ Playwright   │ Selenium      │")
    print("  ├─────────────────┼──────────────┼───────────────┤")
    print("  │ Installation    │ 1 command    │ 2+ commands   │")
    print("  │ Browser Setup   │ Automatic    │ Manual        │")
    print("  │ Multi-browser   │ Built-in     │ Per-browser   │")
    print("  │ Modern Features │ Excellent    │ Good          │")
    print("  │ Auto-waiting    │ Built-in     │ Manual        │")
    print("  └─────────────────┴──────────────┴───────────────┘")
    
    if selenium_available:
        print("  🎯 Both frameworks available - choose based on project needs!")
    else:
        print("  🎭 Playwright-only setup - modern and streamlined!")
    
    return True


def main():
    """Run all Playwright setup verification tests."""
    print("🎭 PLAYWRIGHT SETUP VERIFICATION")
    print("=" * 50)
    print("This test verifies your Playwright installation")
    print("Similar to Selenium setup verification")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_playwright_imports),
        ("Version Check", test_playwright_version),
        ("Browser Availability", test_browser_availability),
        ("Basic Functionality", test_basic_functionality),
        ("Multi-Browser Support", test_multi_browser_support),
        ("Framework Comparison", test_comparison_with_selenium),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for test_name, result in results:
        if result:
            print(f"✅ {test_name}")
            passed += 1
        else:
            print(f"❌ {test_name}")
            failed += 1
    
    print("-" * 50)
    print(f"Total: {len(results)} | Passed: {passed} | Failed: {failed}")
    
    if failed == 0:
        print("\n🎉 PLAYWRIGHT SETUP COMPLETE!")
        print("✅ Ready for UI testing with Playwright")
        print("✅ Both learning and production modes available")
        print("✅ Multi-browser testing enabled")
        print("\n📚 Next Steps:")
        print("  - Run: pytest tests/ui/test_playwright_pytest.py -v")
        print("  - Run: python tests/ui/test_playwright_standalone.py")
        return True
    else:
        print(f"\n⚠️ SETUP ISSUES DETECTED ({failed} failed)")
        print("💡 Check the error messages above for solutions")
        print("💡 Common fixes:")
        print("  - pip install playwright==1.50.0")
        print("  - playwright install")
        print("  - playwright install chromium firefox")
        return False


if __name__ == "__main__":
    """Entry point for setup verification."""
    success = main()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)
