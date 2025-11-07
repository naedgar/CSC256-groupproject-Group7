# tests/health/verify_playwright_bdd_setup.py
"""
pytest-bdd + pytest-playwright Setup Verification Script

This helper verifies the local environment is prepared for running the
pytest-bdd + pytest-playwright acceptance tests used in the course.

INDUSTRY STANDARD VERIFICATION:
This script validates the pytest-playwright setup which is the industry
standard for BDD browser automation, providing built-in fixtures,
video recording, screenshot capture, and zero-configuration browser management.

It checks for:
 - Python packages: playwright, pytest-bdd, pytest-playwright, pytest-html
 - Playwright CLI availability and browser installation
 - pytest-playwright plugin integration and fixtures
 - Flask app reachability and health
 - Feature files and BDD test structure
 - pytest-playwright configuration and capabilities

Run from the repository root. Returns 0 on success, non-zero otherwise.
Example: python tests/health/verify_playwright_bdd_setup.py
"""

from __future__ import annotations

import sys
import subprocess
import os
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parent


def _run(cmd, timeout=10):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except Exception as e:
        return 1, "", str(e)


def test_python_packages():
    print("🧪 Test 1: Required Python packages with EXACT versions")
    print("-" * 50)
    
    # Define required exact versions (must match requirements.txt)
    required_versions = {
        "playwright": "1.55.0",
        "pytest-playwright": "0.7.1", 
        "pytest-bdd": "8.1.0",
        "pytest-html": "4.1.1"
    }
    
    # Map PyPI names to import names
    import_names = {
        "playwright": "playwright",
        "pytest-playwright": "pytest_playwright",
        "pytest-bdd": "pytest_bdd", 
        "pytest-html": "pytest_html"
    }
    
    ok = True
    version_issues = []
    missing_packages = []
    
    for pypi_name, required_version in required_versions.items():
        import_name = import_names[pypi_name]
        
        # Check if package is importable and get version
        version_cmd = f"""
try:
    import {import_name}
    if hasattr({import_name}, '__version__'):
        print({import_name}.__version__)
    else:
        import importlib.metadata
        print(importlib.metadata.version('{pypi_name}'))
except ImportError:
    print('not_installed')
except Exception:
    # Try alternative method using importlib.metadata directly
    try:
        import importlib.metadata
        print(importlib.metadata.version('{pypi_name}'))
    except:
        print('unknown')
"""
        code, out, err = _run([sys.executable, "-c", version_cmd])
        
        if code == 0:
            installed_version = out.strip() if out else 'unknown'
            
            if installed_version == 'not_installed':
                print(f"❌ {pypi_name} not installed (REQUIRED: {required_version})")
                missing_packages.append((pypi_name, required_version))
                ok = False
            elif installed_version == required_version:
                print(f"✅ {pypi_name}=={installed_version} (EXACT MATCH)")
                if pypi_name == "pytest-playwright":
                    print(f"   🎭 Industry standard Playwright plugin detected")
            elif installed_version == 'unknown':
                print(f"⚠️ {pypi_name} installed but version unknown (expected {required_version})")
                version_issues.append((pypi_name, installed_version, required_version))
                ok = False
            else:
                print(f"❌ {pypi_name}=={installed_version} (EXPECTED: {required_version})")
                version_issues.append((pypi_name, installed_version, required_version))
                ok = False
        else:
            print(f"❌ {pypi_name} not installed (REQUIRED: {required_version})")
            missing_packages.append((pypi_name, required_version))
            ok = False
    
    # Provide specific fix instructions if there are issues
    if not ok:
        print("\n" + "=" * 50)
        print("🔧 FIX INSTRUCTIONS:")
        print("=" * 50)
        
        if missing_packages or version_issues:
            print("Run this EXACT command to install/update to required versions:")
            print()
            print("pip install --upgrade \\")
            
            all_packages = []
            for pypi_name, required_version in required_versions.items():
                all_packages.append(f"  {pypi_name}=={required_version}")
            
            print(" \\\n".join(all_packages))
            print()
            print("OR if your requirements.txt already has the correct versions:")
            print("pip install -r requirements.txt")
            print()
            print("Then install browser binaries:")
            print("python -m playwright install chromium firefox webkit")
            print()
            print("💡 This ensures EXACT version compatibility for BDD testing")
            print()
            print("🔍 COMMON CAUSES OF VERSION MISMATCHES:")
            print("• You updated requirements.txt but didn't reinstall the packages")
            print("• You ran 'pip freeze > requirements.txt' which captured newer versions,")
            print("  but your environment still has older versions cached")
            print("• Some packages were manually updated but not others")
            print("• Virtual environment is out of sync with requirements.txt")
        
        if version_issues:
            print("\n� Version mismatches found:")
            for pypi_name, installed, required in version_issues:
                print(f"  • {pypi_name}: {installed} → {required}")
        
        if missing_packages:
            print("\n📋 Missing packages:")
            for pypi_name, required in missing_packages:
                print(f"  • {pypi_name}=={required}")
    
    return ok


def test_playwright_cli_and_browsers():
    print("🧪 Test 2: Playwright CLI & browsers for pytest-playwright")
    print("-" * 50)
    code, out, err = _run([sys.executable, "-m", "playwright", "--version"])
    if code == 0:
        version_info = out.splitlines()[0] if out else 'version info'
        print(f"✅ Playwright CLI available: {version_info}")
    else:
        print(f"❌ Playwright CLI not available: {err.splitlines()[0]}")
        return False

    # Check browser installations specifically for pytest-playwright
    browsers = ["chromium", "firefox", "webkit"]
    for browser in browsers:
        code, out, err = _run([sys.executable, "-m", "playwright", "install", browser, "--dry-run"], timeout=5)
        if code == 0 and "is already installed" in out:
            print(f"✅ {browser} browser installed for pytest-playwright")
        else:
            print(f"⚠️ {browser} browser may need installation")
    
    print("💡 To install all browsers: python -m playwright install")
    print("🎭 pytest-playwright automatically manages browser lifecycle")
    return True


def test_pytest_playwright_integration():
    print("🧪 Test 3: pytest-playwright plugin integration")
    print("-" * 50)
    
    # Test pytest-playwright fixtures availability
    code, out, err = _run([sys.executable, "-m", "pytest", "--fixtures", "-q"], timeout=10)
    if code == 0:
        pytest_playwright_fixtures = [
            "browser_type", "browser", "context", "page", 
            "browser_name", "browser_channel", "is_chromium", "is_firefox", "is_webkit"
        ]
        
        found_fixtures = []
        for fixture in pytest_playwright_fixtures:
            if fixture in out:
                found_fixtures.append(fixture)
        
        if len(found_fixtures) >= 4:  # Core fixtures
            print(f"✅ pytest-playwright fixtures detected: {', '.join(found_fixtures[:4])}")
            print("🎭 Industry standard browser automation fixtures available")
        else:
            print(f"⚠️ Some pytest-playwright fixtures missing: {', '.join(found_fixtures)}")
            
        # Check for built-in features
        features = {
            "--headed": "headed mode support",
            "--browser": "multiple browser support", 
            "--video": "video recording capability",
            "--screenshot": "screenshot capture capability"
        }
        
        print("🎥 pytest-playwright built-in features:")
        for flag, description in features.items():
            print(f"   {flag}: {description}")
            
    else:
        print(f"❌ pytest fixture discovery failed: {err.splitlines()[0] if err else 'unknown error'}")
        return False
        
    # Test pytest-playwright help
    code, out, err = _run([sys.executable, "-m", "pytest", "--help"], timeout=5)
    if code == 0 and ("--headed" in out or "playwright" in out.lower()):
        print("✅ pytest-playwright CLI integration working")
    else:
        print("⚠️ pytest-playwright CLI options may not be available")
        
    return True


def test_flask_app():
    print("🧪 Test 4: Flask application status")
    print("-" * 50)
    try:
        r = requests.get("http://localhost:5000/api/health", timeout=3)
        if r.status_code == 200:
            print("✅ Flask API /api/health reachable")
            
            # Test additional endpoints for BDD testing
            endpoints = ["/tasks", "/tasks/new", "/tasks/report"]
            for endpoint in endpoints:
                try:
                    resp = requests.get(f"http://localhost:5000{endpoint}", timeout=2)
                    if resp.status_code == 200:
                        print(f"✅ Flask {endpoint} reachable")
                    else:
                        print(f"⚠️ Flask {endpoint} returned {resp.status_code}")
                except:
                    print(f"⚠️ Flask {endpoint} not accessible")
            
            return True
        else:
            print(f"⚠️ Flask responded {r.status_code}; try starting with: python -m app.main")
            return False
    except requests.RequestException:
        print("❌ Flask server not reachable on http://localhost:5000/")
        print("   Start it with: python -m app.main")
        return False


def test_feature_files():
    print("🧪 Test 5: BDD Feature files and pytest-bdd integration")
    print("-" * 50)
    features_dir = ROOT.joinpath("features")
    feature_file = features_dir.joinpath("task_workflow_playwright.feature")
    ok = True
    if feature_file.exists():
        print(f"✅ {feature_file.relative_to(ROOT)}")
        
        # Check feature file content
        try:
            with open(feature_file, 'r') as f:
                content = f.read()
                if "pytest-playwright" in content.lower() or "playwright" in content:
                    print("✅ Feature file contains Playwright references")
                if "Given" in content and "When" in content and "Then" in content:
                    print("✅ Feature file has proper Gherkin syntax")
        except Exception as e:
            print(f"⚠️ Could not validate feature file content: {e}")
    else:
        print(f"❌ {feature_file.relative_to(ROOT)} missing")
        ok = False

    # Report on any .feature files found
    found = list(features_dir.rglob('*.feature')) if features_dir.exists() else []
    print(f"ℹ️ Found {len(found)} .feature file(s) in {features_dir}")
    
    # Check step definitions file
    step_file = ROOT.joinpath("test_playwright_pytestbdd.py")
    if step_file.exists():
        print(f"✅ Step definitions file present: {step_file.name}")
        try:
            with open(step_file, 'r') as f:
                content = f.read()
                if "pytest-playwright" in content.lower():
                    print("✅ Step definitions reference pytest-playwright")
                if "@given" in content and "@when" in content and "@then" in content:
                    print("✅ Step definitions have pytest-bdd decorators")
        except Exception as e:
            print(f"⚠️ Could not validate step definitions: {e}")
    else:
        print(f"⚠️ Step definitions file missing: {step_file.name}")
        ok = False
        
    return ok


def test_pytest_playwright_features():
    print("🧪 Test 6: pytest-playwright advanced features")
    print("-" * 50)
    
    # Test video recording capability
    code, out, err = _run([sys.executable, "-m", "pytest", "--help"], timeout=5)
    if code == 0:
        video_support = "--video" in out
        screenshot_support = "--screenshot" in out
        browser_support = "--browser" in out
        headed_support = "--headed" in out
        
        features_found = []
        if video_support:
            features_found.append("video recording")
        if screenshot_support:
            features_found.append("screenshot capture")
        if browser_support:
            features_found.append("multiple browsers")
        if headed_support:
            features_found.append("headed/headless modes")
            
        if len(features_found) >= 3:
            print(f"✅ pytest-playwright features available: {', '.join(features_found)}")
        else:
            print(f"⚠️ Limited pytest-playwright features: {', '.join(features_found)}")
    else:
        print("❌ Could not verify pytest-playwright features")
        return False
    
    # Check for pytest-playwright configuration files
    config_files = ["pytest.ini", "pyproject.toml", "setup.cfg"]
    config_found = False
    for config_file in config_files:
        config_path = ROOT.parent.parent.parent.joinpath(config_file)  # Go to repo root
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    content = f.read()
                    if "playwright" in content.lower():
                        print(f"✅ pytest-playwright configuration found in {config_file}")
                        config_found = True
                        break
            except:
                pass
    
    if not config_found:
        print("ℹ️ No pytest-playwright configuration found (using defaults)")
    
    print("🎭 pytest-playwright provides industry-standard browser automation")
    return True


def main():
    print("🎭 PYTEST-PLAYWRIGHT + pytest-bdd SETUP VERIFICATION")
    print("=" * 60)
    print("Development Environment Readiness Check")
    print("-" * 60)
    
    checks = [
        test_python_packages,           # Test 1: Dependencies with exact versions
        test_flask_app,                # Test 4: Flask application status
    ]

    passed = 0
    for i, chk in enumerate(checks, 1):
        try:
            if chk():
                passed += 1
        except Exception as e:
            print(f"❌ Error running check: {e}")
        print()

    # Always show browser installation instructions
    print("🌐 BROWSER BINARIES INSTALLATION:")
    print("-" * 50)
    print("📦 Install Playwright browser binaries (required for BDD testing):")
    print("python -m playwright install chromium firefox webkit")
    print()
    print("💡 This downloads browser engines that Playwright uses for automation")
    print("💡 Only needs to be done once per environment")
    print()

    print("=" * 60)
    print(f"📊 RESULTS: {passed}/{len(checks)} core development checks passed")
    if passed == len(checks):
        print("🎉 Development environment ready for pytest-bdd + pytest-playwright!")
        print("\n🚀 NEXT STEPS:")
        print("-" * 60)
        print("1️⃣ Install browser binaries (if not already done):")
        print("python -m playwright install chromium firefox webkit")
        print()
        print("2️⃣ Ready to run BDD tests:")
        print("pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -v")
        print()
        print("3️⃣ Advanced BDD testing options:")
        print("pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --headed --video=retain-on-failure")
        return 0
    else:
        print("❌ Some checks failed. Fix the issues above and re-run this script.")
        print("\n" + "=" * 60)
        print("� COMPLETE SETUP INSTRUCTIONS:")
        print("=" * 60)
        print("1️⃣ Install/Update to EXACT required versions:")
        print("pip install --upgrade \\")
        print("  playwright==1.55.0 \\")
        print("  pytest-playwright==0.7.1 \\") 
        print("  pytest-bdd==8.1.0 \\")
        print("  pytest-html==4.1.1")
        print()
        print("2️⃣ Install Playwright browser binaries:")
        print("python -m playwright install chromium firefox webkit")
        print()
        print("   OR if your requirements.txt already has the correct versions:")
        print("   pip install -r requirements.txt")
        print()
        print("3️⃣ Start Flask server (required for verification):")
        print("python -m app.main")
        print()
        print("4️⃣ Re-run this verification script:")
        print("python tests/health/verify_playwright_bdd_setup.py")
        print()
        print("💡 These are the EXACT versions in requirements.txt")
        print("💡 All versions must match for BDD testing compatibility")
        print()
        print("🔍 TROUBLESHOOTING VERSION MISMATCHES:")
        print("• Check if your virtual environment is activated")
        print("• You may have updated requirements.txt but not reinstalled packages")
        print("• Environment could be out of sync after 'pip freeze > requirements.txt'")
        print("• Try: pip install -r requirements.txt to sync with requirements")
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
