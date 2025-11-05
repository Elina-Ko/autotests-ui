![UI Tests](https://github.com/Elina-Ko/autotests-ui/actions/workflows/tests.yml/badge.svg)

# UI Automation Testing Project (Python + Playwright)

Учебный проект по автоматизации веб-тестирования.
Цель: переход к работе QA Automation Engineer с упором на UI и API тестирование.

# Стек

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Git / GitHub

# Планируется:

- ✅ Allure Reports
- ✅ API тесты (requests + Playwright fixtures)
- ✅ CI/CD (GitHub Actions)
- ✅ Docker

# 📂 Структура проекта

```bash
autotests-ui/
├── automation/
│   ├── pages/
│   │   ├── base_page.py
│   │   └── registration_page.py
│   ├── tests/
│   │   └── test_registration.py
│   ├── utils/
│   └── conftest.py
│
├── .github/workflows/tests.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

# ✅ Реализовано

- Автотесты для UI
- POM-архитектура
- Фикстуры Pytest
- Логирование шагов

# ▶️ Как запустить

- 1️⃣ Установить зависимости

```bash
pip install -r requirements.txt
```

- 2️⃣ Запустить тесты

```bash
pytest -s -v
```

- 3️⃣ Установить Playwright браузеры (один раз)

```bash
playwright install
```

# Планы развития

- Задача Статус
- UI тесты ✅
- API тесты 🚧 in progress
- Allure отчёты 🚧 in progress
  -CI/CD GitHub Actions 🚧 in progress
- Docker контейнер 🚧 in progress

# Автор

Элина Кондратьева
Junior QA Automation Engineer
📫 tg: @ElinaKon

# ❗Важно

Это учебный проект, который развивается и расширяется в процессе изучения автоматизации тестирования.
