from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://bootswatch.com/default/")
    input_elements = page.locator("//input[@placeholder='Search']")
    element = input_elements.element_handles()
    for ele in element:
        ele.fill("Hello")
