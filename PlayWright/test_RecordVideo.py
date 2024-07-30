from playwright.sync_api import sync_playwright



def test_RecordVideo():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(record_video_dir="")

        page = context.new_page()

        page.goto("https://playwright.dev/python")
        page.get_by_role("link", name="Get Started").click()
        page.wait_for_load_state()
        # page.get_by_role("link", name="Add Example Test").click()
        page.locator("//a[text()='Add Example Test']").click()
        page.wait_for_timeout(timeout=3000)

        context.close()


