import pytest
from playwright.async_api import Playwright
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email_input = page.get_by_test_id("registration-form-email-input").locator('//div//input')
        registration_email_input.fill('qwe@gmail.com')

        registration_username_input = page.get_by_test_id("registration-form-username-input").locator('//div//input')
        registration_username_input.fill('qwe')

        registration_password_input = page.get_by_test_id("registration-form-password-input").locator('//div//input')
        registration_password_input.fill('password')

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        context.storage_state(path='browser-state.json')
        browser.close()


@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()
