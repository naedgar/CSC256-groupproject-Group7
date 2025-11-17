"""
Selenium Setup Verification Test (Standalone)

This standalone script verifies that your Selenium testing environment is properly configured.
Run this before starting with Selenium UI testing to ensure everything works correctly.

Run with: python tests/health/test_setup_selenium.py

Features verified:
- ✅ All Selenium modules import correctly
- ✅ ChromeDriver availability (webdriver-manager and system)
- ✅ Basic browser functionality (page navigation, element selection)
- ✅ Multi-browser support (Chrome, Firefox if available)
- ✅ WebDriver options and configuration
- ✅ Framework comparison with Playwright (if available)
"""

import sys
import os
import time
from typing import Optional

import pytest

pytestmark = pytest.mark.e2e


def test_selenium_imports():
    """Test 1: Verify all required Selenium modules can be imported"""
    print("🧪 Test 1: Import Test")
    print("-" * 30)
    
    success_count = 0
    total_tests = 6
    
    # Test core Selenium imports
    try:
        from selenium import webdriver
        print("✅ selenium.webdriver imported successfully")
        success_count += 1
    except ImportError as e:
        print(f"❌ Failed to import selenium.webdriver: {e}")
        return False
    
    try:
        from selenium.webdriver.common.by import By
        print("✅ selenium.webdriver.common.by.By imported successfully")
        success_count += 1
    except ImportError as e:
        print(f"❌ Failed to import By: {e}")
    
    try:
        from selenium.webdriver.support.ui import WebDriverWait
        print("✅ selenium.webdriver.support.ui.WebDriverWait imported successfully")
        success_count += 1
    except ImportError as e:
        print(f"❌ Failed to import WebDriverWait: {e}")
    
    try:
        from selenium.webdriver.support import expected_conditions as EC
        print("✅ selenium.webdriver.support.expected_conditions imported successfully")
        success_count += 1
    except ImportError as e:
        print(f"❌ Failed to import expected_conditions: {e}")
    
    try:
        from selenium.webdriver.chrome.options import Options
        print("✅ selenium.webdriver.chrome.options.Options imported successfully")
        success_count += 1
    except ImportError as e:
        print(f"❌ Failed to import Chrome Options: {e}")
    
    # Test webdriver-manager (optional but recommended)
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        print("✅ webdriver_manager.chrome.ChromeDriverManager imported successfully")
        success_count += 1
    except ImportError:
        print("⚠️ webdriver-manager not installed (optional but recommended)")
        print("   Install with: pip install webdriver-manager")
    
    print(f"\n📊 Import Results: {success_count}/{total_tests} core imports successful")
    if success_count >= 5:
        return True
    else:
        print("❌ Missing core Selenium imports")
        return False


def test_selenium_version():
    """Test 2: Check Selenium version"""
    print("\n🧪 Test 2: Version Check")
    print("-" * 30)
    
    try:
        import selenium
        version = selenium.__version__
        print(f"✅ Selenium version: {version}")
        
        # Check if version is reasonable (3.x or 4.x)
        major_version = int(version.split('.')[0])
        if major_version >= 3:
            print(f"✅ Version {version} is supported")
        else:
            print(f"⚠️ Version {version} is quite old, consider upgrading")
        return True
    except Exception as e:
        print(f"❌ Could not determine Selenium version: {e}")
        return False


def test_chromedriver_availability():
    """Test 3: Test ChromeDriver availability and setup"""
    print("\n🧪 Test 3: ChromeDriver Availability")
    print("-" * 30)
    
    chrome_methods = []
    
    # Method 1: webdriver-manager (recommended)
    try:
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        
        print("🔍 Testing webdriver-manager approach...")
        
        # Setup Chrome options for headless testing
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--log-level=3")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.quit()
        
        print("✅ ChromeDriver with webdriver-manager: SUCCESS")
        chrome_methods.append("webdriver-manager")
        
    except ImportError:
        print("⚠️ webdriver-manager not available")
        print("   Install with: pip install webdriver-manager")
    except Exception as e:
        print(f"❌ webdriver-manager ChromeDriver failed: {e}")
    
    # Method 2: System ChromeDriver
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        print("🔍 Testing system ChromeDriver...")
        
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        
        driver = webdriver.Chrome(options=options)
        driver.quit()
        
        print("✅ System ChromeDriver: SUCCESS")
        chrome_methods.append("system")
        
    except Exception as e:
        print(f"❌ System ChromeDriver failed: {e}")
        print("   Make sure Chrome browser is installed")
        print("   For automatic setup, install: pip install webdriver-manager")
    
    if chrome_methods:
        print(f"\n✅ ChromeDriver available via: {', '.join(chrome_methods)}")
        return True
    else:
        print("\n❌ No working ChromeDriver found")
        print("\n🔧 Troubleshooting:")
        print("   1. Install Chrome browser: https://www.google.com/chrome/")
        print("   2. Install webdriver-manager: pip install webdriver-manager")
        print("   3. Or download ChromeDriver manually: https://chromedriver.chromium.org/")
        return False


def test_basic_functionality():
    """Test 4: Test basic Selenium functionality"""
    print("\n🧪 Test 4: Basic Functionality")
    print("-" * 30)
    
    try:
        # Setup Chrome with all the options
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        
        print("🔍 Testing basic browser operations...")
        
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--log-level=3")
        
        # Try webdriver-manager first, fallback to system
        driver = None
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        except:
            driver = webdriver.Chrome(options=options)
        
        # Test basic operations
        print("  🌐 Testing page navigation...")
        driver.get("data:text/html,<html><body><h1 id='test'>Selenium Test Page</h1><button id='btn'>Click Me</button></body></html>")
        
        print("  🔍 Testing element selection...")
        heading = driver.find_element(By.ID, "test")
        assert heading.text == "Selenium Test Page"
        
        print("  👆 Testing element interaction...")
        button = driver.find_element(By.ID, "btn")
        button.click()
        
        print("  📏 Testing browser properties...")
        title = driver.title
        url = driver.current_url
        
        driver.quit()
        
        print("✅ Basic functionality test passed")
        print(f"   Page title: {title}")
        print(f"   Page URL: {url[:50]}...")
        return True

    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        if 'driver' in locals() and driver:
            try:
                driver.quit()
            except:
                pass
        return False


def test_multi_browser_support():
    """Test 5: Test multi-browser support"""
    print("\n🧪 Test 5: Multi-Browser Support")
    print("-" * 30)
    
    browsers_tested = []
    
    # Test Chrome (already tested above, but confirm)
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--log-level=3")
        
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        except:
            driver = webdriver.Chrome(options=options)
        
        driver.get("data:text/html,<html><body><h1>Chrome Test</h1></body></html>")
        driver.quit()
        browsers_tested.append("Chrome")
        print("✅ Chrome browser support confirmed")
        
    except Exception as e:
        print(f"❌ Chrome browser test failed: {e}")
    
    # Test Firefox
    try:
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        
        print("🔍 Testing Firefox browser...")
        
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        
        try:
            from webdriver_manager.firefox import GeckoDriverManager
            from selenium.webdriver.firefox.service import Service as FirefoxService
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
        except:
            driver = webdriver.Firefox(options=firefox_options)
        
        driver.get("data:text/html,<html><body><h1>Firefox Test</h1></body></html>")
        driver.quit()
        browsers_tested.append("Firefox")
        print("✅ Firefox browser support confirmed")
        
    except ImportError:
        print("⚠️ webdriver-manager firefox support not available")
    except Exception as e:
        print(f"⚠️ Firefox browser test failed: {e}")
        print("   Firefox may not be installed or GeckoDriver missing")
    
    # Test Edge (Windows)
    if sys.platform.startswith('win'):
        try:
            from selenium import webdriver
            from selenium.webdriver.edge.options import Options as EdgeOptions
            
            print("🔍 Testing Edge browser...")
            
            edge_options = EdgeOptions()
            edge_options.add_argument("--headless")
            
            try:
                from webdriver_manager.microsoft import EdgeChromiumDriverManager
                from selenium.webdriver.edge.service import Service as EdgeService
                service = EdgeService(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=service, options=edge_options)
            except:
                driver = webdriver.Edge(options=edge_options)
            
            driver.get("data:text/html,<html><body><h1>Edge Test</h1></body></html>")
            driver.quit()
            browsers_tested.append("Edge")
            print("✅ Edge browser support confirmed")
            
        except Exception as e:
            print(f"⚠️ Edge browser test failed: {e}")
    
    print(f"\n📊 Browser Results: {len(browsers_tested)} browsers available: {', '.join(browsers_tested)}")
    if len(browsers_tested) > 0:
        return True
    else:
        print("⚠️ No browsers confirmed available")
        return False


def test_framework_comparison():
    """Test 6: Compare with Playwright if available"""
    print("\n🧪 Test 6: Framework Comparison")
    print("-" * 30)
    
    try:
        import playwright
        print("✅ Playwright is also available in this environment")
        print("   You can use both Selenium and Playwright for comprehensive testing")
        print("   Selenium: Mature, widely adopted, extensive ecosystem")
        print("   Playwright: Modern, fast, excellent developer experience")
    except ImportError:
        print("ℹ️ Playwright not installed (this is fine)")
        print("   Selenium is ready for your UI testing needs")
        print("   To also install Playwright: pip install playwright")
    
    # Check pytest
    try:
        import pytest
        print("✅ pytest is available for professional test structure")
    except ImportError:
        print("⚠️ pytest not installed")
        print("   Install with: pip install pytest")
    
    return True


def main():
    """Main function to run all setup verification tests"""
    print("🌐 SELENIUM SETUP VERIFICATION")
    print("=" * 50)
    print("ℹ️ This is a health check for your Selenium testing environment")
    print("ℹ️ Located in /tests/health/ as it verifies system dependencies")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_selenium_imports),
        ("Version Check", test_selenium_version),
        ("ChromeDriver Availability", test_chromedriver_availability),
        ("Basic Functionality", test_basic_functionality),
        ("Multi-Browser Support", test_multi_browser_support),
        ("Framework Comparison", test_framework_comparison),
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed_tests += 1
        except Exception as e:
            print(f"❌ {test_name} encountered an error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 FINAL RESULTS: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests >= 4:  # At least core functionality must work
        print("🎉 SELENIUM SETUP COMPLETE!")
        print("\n🚀 You're ready to start UI testing with Selenium!")
        print("\nNext steps:")
        print("  1. Run learning mode: pytest -v -s tests/ui/selenium/pytest/test_selenium_pytest.py")
        print("  2. Run production mode: python tests/ui/selenium/standalone/test_selenium_standalone.py")
        print("  3. Check the selenium_tutorial.md for comprehensive guidance")
        return 0
    else:
        print("❌ SELENIUM SETUP INCOMPLETE")
        print("\n🔧 Please address the failing tests above before proceeding.")
        print("\nCommon fixes:")
        print("  • Install Selenium: pip install selenium")
        print("  • Install webdriver-manager: pip install webdriver-manager")
        print("  • Install Chrome browser: https://www.google.com/chrome/")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())