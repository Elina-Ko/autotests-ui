![UI Tests](https://github.com/Elina-Ko/autotests-ui/actions/workflows/tests.yml/badge.svg)

# UI Automation Testing Framework (Python + Playwright)

Проект по автоматизации тестирования web-приложений.
Разрабатывается для формирования полного навыка QA Automation Engineer.

---

## 🧰 Tech stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Git / GitHub
- Allure Reports (в процессе)
- GitHub Actions CI

---

## 🚀 Возможности фреймворка

- UI автотесты (Web)
- POM-архитектура
- Контекст сессии (storage state)
- Фикстуры Pytest
- Скриншоты при падении теста
- Генерация отчётов Allure (готовится)
- CI pipeline (GitHub Actions)

---

## 📂 Структура проекта

```bash
autotests-ui/
├── automation/
│   ├── pages/
│   │   ├── base_page.py
│   │   └── registration_page.py
│   ├── tests/
│   │   └── test_registration.py
│   ├── utils/          # helpers (будут добавляться)
│   └── conftest.py
│
├── .github/workflows/tests.yml   # CI pipeline
├── requirements.txt
├── pytest.ini
└── README.md
```

## ▶️ Как запустить тесты локально

1️⃣ Установить зависимости

```bash
pip install -r requirements.txt
```

2️⃣ Установить Playwright браузеры

```bash
playwright install
```

3️⃣ Запуск тестов

```bash
pytest -s -v
```

4️⃣ Allure отчёт (если установлен Allure CLI)

```bash
allure serve allure-results
```

## 🛠 Roadmap

| Функция              | Статус         |
|----------------------|----------------|
| UI тесты             | ✅ Done         |
| API тесты            | 🚧 In progress |
| Allure отчёты        | 🚧 In progress |
| CI/CD GitHub Actions | ✅ Done         |
| Docker support       | 🚧 Planned     |

## 👤 Автор

**Элина Кондратьева**  
QA Automation Engineer

📬 Telegram: @ElinaKon

Проект развивается в рамках подготовки к позиции QA Automation Engineer