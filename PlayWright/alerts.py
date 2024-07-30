from playwright.sync_api import sync_playwright


def on_dialog(dialog):
    print("Dialog open " + str(dialog))
    dialog.accept("Playwright Prompt box")
    # dialog.dismiss()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")
    # page.locator("[value='Show alert box']").click()
    page.on("dialog", on_dialog)
    alert_box = page.get_by_text("Show prompt box")
    alert_box.click(delay=2000)
    page.wait_for_timeout(timeout=2000)
