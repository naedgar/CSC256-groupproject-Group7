"""pytest-bdd fixtures using the industry standard pytest-playwright plugin.

This file uses pytest-playwright's built-in fixtures which provide:
- Automatic browser management and cleanup
- Built-in video recording on test failure
- Screenshot capture capabilities
- Parallel execution support
- Zero-configuration headless/headed mode switching

The pytest-playwright plugin is the industry standard and recommended approach.
"""
from __future__ import annotations

import pytest
import logging

logger = logging.getLogger(__name__)


# pytest-playwright provides these fixtures automatically:
# - browser_type (chromium, firefox, webkit)
# - browser (browser instance)
# - context (browser context)
# - page (page instance)

# No need to define custom browser/page fixtures - pytest-playwright handles this!

# Database reset fixture for clean test isolation
from test_helpers.db_reset_helper import reset_database_state

@pytest.fixture(autouse=True)
def reset_tasks():
    """Reset tasks via the test helper before each test for clean isolation."""
    try:
        reset_database_state()
    except Exception as exc:  # pragma: no cover - defensive logging
        logger.exception("reset_database_state failed: %s", exc)
        raise
    yield
    logger.debug("test_helpers.db_reset_helper not available; skipping autouse reset fixture")