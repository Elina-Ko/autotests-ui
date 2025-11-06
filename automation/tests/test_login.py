import pytest
import allure
from playwright.sync_api import expect
from automation.pages.login_page import LoginPage
from automation.data.users import VALID_USER, INVALID_USER


@allure.feature("Авторизация")
@allure.story("Успешный вход в систему")
@pytest.mark.authorization
def test_login_success(ui_page, save_login_state):
    login_page = LoginPage(ui_page)

    with allure.step("Открываем страницу логина"):
        login_page.open()

    with allure.step("Вводим корректные данные и входим"):
        login_page.login(VALID_USER["email"], VALID_USER["password"])

    # 👇 Добавляем отладочную паузу
    ui_page.pause()  # Откроется Playwright Inspector

    with allure.step("Проверяем, что панель управления открылась"):
        expect(ui_page.locator(login_page.dashboard_title)).to_be_visible()

    with allure.step("Сохраняем состояние браузера после успешного входа"):
        save_login_state(ui_page)


@allure.feature("Авторизация")
@allure.story("Ошибка при неверных данных")
@pytest.mark.authorization
def test_login_wrong_credentials(ui_page):
    login_page = LoginPage(ui_page)

    with allure.step("Открываем страницу логина"):
        login_page.open()

    with allure.step("Пробуем войти с неверными данными"):
        login_page.login(INVALID_USER["email"], INVALID_USER["password"])

    with allure.step("Проверяем, что появилось сообщение об ошибке"):
        expect(ui_page.locator(login_page.wrong_alert)).to_be_visible()
        expect(ui_page.locator(login_page.wrong_alert)).to_have_text("Wrong email or password")
