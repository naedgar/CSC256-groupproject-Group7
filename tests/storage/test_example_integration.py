import pytest

@pytest.mark.integration
def test_example_integration():
    # simple integration-style test (no real DB calls, just demonstration)
    assert isinstance({"id":1}.get("id"), int)