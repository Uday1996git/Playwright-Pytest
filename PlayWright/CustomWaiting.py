from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")
    page.locator("//a[@id='2015']").click()
    text = page.locator("//tbody[@id='table-body']//tr[1]//td[1]").inner_text()
    print(text)
