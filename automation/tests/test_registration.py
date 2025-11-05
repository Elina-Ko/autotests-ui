import os
import time
from automation.pages.registration_page import RegistrationPage

STATE_FILE = "browser-state.json"


def test_successful_registration(page):
    reg = RegistrationPage(page)

    # Если сессия уже есть — просто проверяем, что dashboard доступен
    if os.path.exists(STATE_FILE):
        reg.open_dashboard()
        assert reg.registration_success(), "Session state invalid, not logged in"
        return

    # Иначе — регистрируем нового пользователя
    email = f"qa_{int(time.time())}@gmail.com"

    reg.open()
    reg.register(
        email=email,
        username="username",
        password="password"
    )

    assert reg.registration_success(), "User was not redirected to dashboard"
