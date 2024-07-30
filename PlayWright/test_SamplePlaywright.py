import re
from playwright.sync_api import sync_playwright
import pytest
from playwright.sync_api import Page
from PageObject import Homepage


#sync api and async api(uses await and async keywords)
#Intially the test run on headless mode, to run test on headed mode you need to mention headless to false in the step "browser = playwright.chromium.launch(headless=false)"

# playwright = sync_playwright().start()
#
# browser = playwright.chromium.launch(headless=False, slow_mo= 10page = browser.new_page()
# page.goto("https://playwright.dev/python")
# browser.close()

# class TestClass:

    # def __init__(self, page: Page):
    #     self.home = Homepage(page)
    # obj = Homepage(Page)



@pytest.fixture(scope='module')
def fixture_code():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page



def test_PlayWrightWebsite(fixture_code):
    page = fixture_code
    homePage = Homepage(page)
    homePage.navigate_toURL()
    print(page.title())
    homePage.return_Docs_Button().click()
    homePage.return_Search_box().click()
    homePage.return_search_box_popup().fill("tests")

    # page.locator("//a[text()='Docs']").click()
    # page.get_by_role("link", name="Docs").click()
    # browser.close()
