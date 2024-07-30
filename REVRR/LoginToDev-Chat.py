from EmailAutomation import simpleFetchEmail
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rs-dev-chat.revrr.ai/login", wait_until='load')

    page.get_by_label("Email").fill("uday@revrr.digital")
    page.get_by_role("button", name='Sign in').click()
    page.wait_for_timeout(timeout=15000)
    OTP = simpleFetchEmail.fetch_latest_email_by_subject("Your One-Time Password (OTP) for Verification")
    otp_array = simpleFetchEmail.OTP_array(OTP)
    otp = page.locator("//input")
    otp_inputs = otp.element_handles()
    count = 1
    if len(otp_inputs) == len(otp_array):
        for ele in otp_inputs:
            ele.fill(str(otp_array[count]))
            count += 1

    page.get_by_role("button", name="Verify OTP").click()
    page.wait_for_timeout(timeout=5000)
    page.locator("//div[@type='button']//div").click()
    page.locator("//div[text()='Google']").click()
    prompt_textarea = page.locator("//textarea[@id='prompt-textarea']")
    prompt_placeholder = prompt_textarea.get_attribute('placeholder')
    print(prompt_placeholder)
    assert prompt_placeholder == "Message Gemini…"
    prompt_textarea.fill("My Date of birth is june 10 1996")
    page.keyboard.press("Enter")


