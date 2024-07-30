from playwright.sync_api import sync_playwright


def test_trace():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False,slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(name="trace_MyPlaywright",
                              screenshots=True,
                              snapshots=True,
                              sources=True
                              )
        page.goto("https://playwright.dev/python")
        page.locator("//a[text()='Get started']").click()
        # page.wait_for_load_state()
        # page.get_by_role("link", name="Add Example Test").click()
        page.locator("//a[text()='Add Example Test']").click()
        context.tracing.stop(path="Traces//trace.zip")
#TO WATCH THE TRACE, YOU WOULD NEED TO OPEN THE TRACE.ZIP FROM THE COMMAND LINE USING -
# playwright show-trace Traces/trace.zip
