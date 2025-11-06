from automation.pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

    email_input = "[data-testid='login-form-email-input'] input"
    password_input = "[data-testid='login-form-password-input'] input"
    login_button = "[data-testid='login-page-login-button']"
    dashboard_title = "[data-testid='dashboard-toolbar-title-text']"
    wrong_alert = "[data-testid='login-page-wrong-email-or-password-alert']"

    @allure.step("Открываем страницу авторизации")
    def open(self):
        self.page.goto(self.URL)

    @allure.step("Вводим email и пароль: {email}")
    def login(self, email, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    @allure.step("Проверяем, что пользователь успешно вошёл")
    def login_success(self):
        return self.page.locator(self.dashboard_title).is_visible()

    @allure.step("Проверяем сообщение об ошибке авторизации")
    def login_failed(self):
        return self.page.locator(self.wrong_alert).is_visible()
