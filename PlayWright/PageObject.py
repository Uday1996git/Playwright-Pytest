from playwright.sync_api import Page
from locatorsEnums import HomaPageLocators
from StartUp import start


class Homepage:
    URL = "https://playwright.dev/python"
    browser = "chrome"

    def __init__(self, page:Page):
        self.page = page
        self.locators = HomaPageLocators
        self.launch = start()

    def before_fixture(self):
        self.launch.Start_up(Homepage.browser)
        # start.Start_up(Homepage.browser)

    def navigate_toURL(self):
        self.page.goto(Homepage.URL)

    def return_Docs_Button(self):
        return self.page.locator(self.locators.Docs_Button.value)

    def return_Search_box(self):
        return self.page.locator(self.locators.Search_bar.value)

    def return_search_box_popup(self):
        return self.page.get_by_placeholder(self.locators.Search_Pop_Placeholders.value)

    def click_DocsButton(self):
        Homepage.return_Docs_Button(self).click()

