from playwright.sync_api import sync_playwright, Page


def on_filechooser(file_chooser):
    print("File opened")
    file_chooser.set_files("pytest.ini")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")
    page.on("filechooser", on_filechooser)
    page.get_by_label("Default file input example").click(delay=2000)
