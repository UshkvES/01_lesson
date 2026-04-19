# Проект автоматизации тестирования с Allure

## Описание

Проект содержит автотесты для:
1. **Калькулятора** (https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
2. **Интернет-магазина SauceDemo** (https://www.saucedemo.com/)

Тесты реализованы с использованием паттерна **Page Object Model (POM)** и собраны в отчеты с помощью **Allure**.

В проекте используется Allure для:

1. Декораторов тестов: @allure.epic, @allure.feature, @allure.story, @allure.title, @allure.description, @allure.severity, @allure.id

2. Шагов: @allure.step для методов Page Object и with allure.step() для блоков в тестах

3. Вложений: allure.attach() для сохранения результатов вычислений

## Требования

- Python 3.9+
- Установленный браузер **Chrome** (для `test_calculator.py`)
- Установленный браузер **Firefox** (для `test_shop.py`)
- Утилита **Allure Report**

## Запуск тестов и формирование отчета

Чтобы запустить тесты и сохранить результаты для отчета, выполните из папки `lesson_10`:

```bash
pytest --alluredir=allure-results 
```

## Просмотр сформированного отчета

Из папки `lesson_10` выполните команду:

```bash
allure serve allure-results
```