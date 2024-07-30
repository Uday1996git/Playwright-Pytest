from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    page.goto("https://gmail.com")
    page.get_by_label("Email or phone").fill("uday.janoos@gmail.com")
    page.get_by_text("Next").click()
    page.get_by_label("Enter your password").fill("Number@1")
    page.get_by_text("Next").click()

    context.storage_state(path="..//GmailSession//auth//session.json")

    context.close()
