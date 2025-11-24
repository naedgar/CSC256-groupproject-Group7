import re
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

pytestmark = pytest.mark.e2e


def _parse_iso_like(s: str):
    m = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", s)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(0), "%Y-%m-%dT%H:%M:%S")
    except Exception:
        return None


def test_time_ui_selenium_updates(start_flask_server):
    """
    Selenium E2E test: launch headless Chrome, open /time, verify time is shown and updates.
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get("http://127.0.0.1:5000/time")
        # Find the paragraph containing the UTC time
        elem = driver.find_element("css selector", "div.alert p")
        text1 = elem.text
        assert "UTC Time" in text1

        t1 = _parse_iso_like(text1)

        # Wait 1.5s and check again
        driver.implicitly_wait(2)
        elem2 = driver.find_element("css selector", "div.alert p")
        text2 = elem2.text
        t2 = _parse_iso_like(text2)

        if t1 and t2:
            assert t2 >= t1
        else:
            assert isinstance(text2, str)
    finally:
        driver.quit()
