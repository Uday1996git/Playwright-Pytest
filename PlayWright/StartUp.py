from playwright.sync_api import sync_playwright, Page


class start():
    def __init__(self):
        self.page = Page

    def Start_up(self, browser):
        playwright = sync_playwright().start()
        if str(browser).lower() == "chrome":
            playwright.chromium.launch(headless=False, slow_mo=1000)
            context = browser.new_context(no_viewport=True)
            self.page = context.new_page()
