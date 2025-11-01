from playwright.sync_api import sync_playwright, expect


def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Находим поле с помощью get_by_test_id

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        # Находим элемент с помощью locator XPath

        password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill("password")

        # Находим поле с помощью get_by_test_id

        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')

        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
