import pytest
from playwright.sync_api import sync_playwright
import os
import allure

STATE_FILE = "browser-state.json"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser, request):
    if os.path.exists(STATE_FILE):
        context = browser.new_context(storage_state=STATE_FILE)
    else:
        context = browser.new_context()

    page = context.new_page()

    yield page

    # ✅ Сохраняем session state только один раз
    if not os.path.exists(STATE_FILE):
        context.storage_state(path=STATE_FILE)

    # ✅ Скриншот до закрытия браузера
    if request.node.rep_call.failed:
        screenshot = page.screenshot()
        allure.attach(
            screenshot,
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
