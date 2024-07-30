from playwright.sync_api import sync_playwright


def test_testScreenshot():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://playwright.dev/python")
        page.screenshot(path="Screenshots//playwright.jpg", full_page=True)
        page.get_by_role("link", name="Get Started").screenshot(path="Screenshots//playwrightElement.jpg")
        page.get_by_role("link", name="Get started").click()
        page.screenshot(path="Screenshots//playwrightDoc.jpg", full_page=True)
