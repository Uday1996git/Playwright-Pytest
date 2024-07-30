from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    start = perf_counter()
    # page.goto("https://playwright.dev/python", wait_until='load')
    # page.goto("https://playwright.dev/python", wait_until='domcontentloaded')
    # page.goto("https://playwright.dev/python", wait_until='commit')
    page.goto("https://playwright.dev/python", wait_until='networkidle')
    end = perf_counter()-start
    print(f"time taken to load the page is {round(end, 2)}s")
