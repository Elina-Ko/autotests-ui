from automation.pages.base_page import BasePage


class RegistrationPage(BasePage):
    URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

    email_input = "[data-testid='registration-form-email-input'] input"
    username_input = "[data-testid='registration-form-username-input'] input"
    password_input = "[data-testid='registration-form-password-input'] input"
    register_button = "[data-testid='registration-page-registration-button']"
    dashboard_title = "[data-testid='dashboard-toolbar-title-text']"

    def open(self):
        self.page.goto(self.URL)

    def register(self, email, username, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.register_button)

    def registration_success(self):
        self.page.wait_for_selector(self.dashboard_title, timeout=5000)
        return self.page.locator(self.dashboard_title).is_visible()

    def open_dashboard(self):
        self.page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
