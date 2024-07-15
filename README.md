# final-progect-tachbulatov

## Тестирование платформы "Кинопоиск"

«Кинопо́иск» — русскоязычный интернет-сервис с условно свободно редактируемой базой данных и интернет-издание о кинематографе. С 2018 года — онлайн-кинотеатр. С 2020 года совместно с «Плюс Студией», продюсерским центром «Яндекса», производит и распространяет оригинальные фильмы и сериалы.

## ШАГИ
1. Склонировать проект https://github.com/alfredtashbulatov/final-progect-tachbulatov.git

2. Установить зависимости

3. Сохранить куки для тестов 
 - Для сохранения куки необходимо авторизоваться в свою учетную запись кинопоиска.
 ~~~
 from selenium import webdriver
 import json

driver = webdriver.Chrome()
driver.get("https://www.kinopoisk.ru/")
Здесь происходит вход в систему
cookies = driver.get_cookies()
with open('cookies.json', 'w') as file:
    json.dump(cookies, file)
~~~
 - Загружаем куки для повторного входа
 ~~~
Загружаем куки для повторного входа
driver = webdriver.Chrome()
driver.get("https://www.kinopoisk.ru/")
with open('cookies.json', 'r') as file:
    cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
driver.refresh()
 ~~~

4. Запустить тесты с указанием пути к директории результатов тестирования pytest pytest --alluredir allure-result

5. Сформировать отчет allure serve allure-results

### Стек:
- pytest
- selenium
- requests
- allure
- configb
- json

### Структура
- ./test - тесты 
  - test_api.py - Api тесты
  - test_ui.py - Ui тесты
- conftest.py - Файл с фикстурами
- requirements.txt - Файл с используемыми зависимостями
- search_films.py - Методы для Ui тестов
- user_api.py - Методы для Аpi тестов

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Документация для неофициального API кинопоиска (kinopoisk.dev)](https://api.kinopoisk.dev/documentation)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure
- pip install json

### Запуск тестов
- python -m pytest (Запуск тестов)
- python -m pytest --alluredir allure-result (Запустить тесты с указанием пути к каталогу результатов тестирования)
- allure serve allure-results (Запустить Allure и конвертирует результаты теста в отчет)