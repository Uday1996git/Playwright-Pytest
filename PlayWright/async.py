import asyncio
from playwright.async_api import async_playwright



async def async_method():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://bootswatch.com/default/")
        print(await page.title())
        await browser.close()


asyncio.run(async_method())