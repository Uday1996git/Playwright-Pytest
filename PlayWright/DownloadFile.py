from playwright.sync_api import sync_playwright

def on_download(download):
    download.save_as("event.jpg")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page(no_viewport=True)
    page.goto("https://unsplash.com/")
    img = page.get_by_alt_text("The sun is setting on a rocky beach")
    img.click()

    page.on("download", on_download)
    with page.expect_download() as download_file:
        download_image = page.get_by_role("link", name = "Download free")
        download_image.click()
    # download = download_file.value
    # download.save_as("HatPhone.jpg")
    browser.close()
