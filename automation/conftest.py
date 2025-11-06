import pytest
from playwright.sync_api import sync_playwright
import os
import allure

STATE_FILE = "browser-state.json"


@pytest.fixture(scope="session")
def browser():
    """Создаёт браузер Chromium"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=400)
        yield browser
        browser.close()


@pytest.fixture()
def ui_page(browser, request):
    """Создаёт новую страницу. Если есть сохранённое состояние — подгружает"""
    # Загружаем сохранённый state (если есть)
    if os.path.exists(STATE_FILE):
        context = browser.new_context(storage_state=STATE_FILE)
    else:
        context = browser.new_context()

    page = context.new_page()

    yield page  # ← возвращаем страницу в тест

    # === 📸 Скриншот при падении ===
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot = page.screenshot()
        allure.attach(
            screenshot,
            name=f"{request.node.name}_failure",
            attachment_type=allure.attachment_type.PNG
        )

    context.close()


@pytest.fixture()
def save_login_state(browser):
    """
    Вспомогательная фикстура — вручную вызвать в тесте,
    если вход прошёл успешно.
    """

    def _save(page):
        page.context.storage_state(path=STATE_FILE)
        print(f"💾 Состояние сохранено в {STATE_FILE}")

    return _save


# === 📊 Сохраняем статус выполнения теста ===
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Позволяет определить, упал ли тест"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
