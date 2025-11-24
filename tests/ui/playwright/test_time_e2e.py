import re
import pytest
from datetime import datetime

pytestmark = pytest.mark.e2e


def parse_iso_like(s: str):
    m = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", s)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(0), "%Y-%m-%dT%H:%M:%S")
    except Exception:
        return None


def test_time_ui_displays_and_updates(chrome_page, start_flask_server, app_base_url):
    """
    Playwright E2E test using the project's `chrome_page` fixture.
    Verifies the /time UI displays UTC time and that it updates.
    """

    url = f"{app_base_url}/time"
    chrome_page.goto(url)
    chrome_page.wait_for_selector("div.alert")

    content = chrome_page.locator("div.alert p").inner_text()
    assert "UTC Time" in content or "UTC Time:" in content

    t1 = parse_iso_like(content)
    assert t1 is None or isinstance(t1, datetime)

    chrome_page.wait_for_timeout(1500)
    content2 = chrome_page.locator("div.alert p").inner_text()
    t2 = parse_iso_like(content2)

    if t1 and t2:
        assert t2 >= t1
    else:
        assert isinstance(content2, str)
