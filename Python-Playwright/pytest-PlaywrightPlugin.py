import pytest
from playwright.sync_api import Page

val = False


@pytest.fixture(autouse=True)
def skip_if_failed():
    global val
    if val:
        pytest.skip("Skipping subsequent tests due to failure in the before test")


@pytest.fixture(autouse=True)
def test_TestPlaywrightPytestPlugin(page: Page):
    global val
    try:
        page.goto("https://playwright.dev/python", wait_until="load")
        yield page
    except ConnectionError:
        val = True
        print("Failed to create a Page Object")
        raise


def test_get_started_button(test_TestPlaywrightPytestPlugin):
    global val
    try:
        print(val)
        page = test_TestPlaywrightPytestPlugin
        get_started_btn = page.get_by_role("link", name="Get started")
        assert get_started_btn.is_visible()
        assert get_started_btn.is_enabled()
        get_started_btn.click()
        title = page.locator(".theme-doc-markdown h1").inner_text()
        assert title == "Installation"
    except AssertionError:
        val = True
        print("Failed to test the get started button")
        raise


def test_failure_Scenario():
    print("Second Test")
