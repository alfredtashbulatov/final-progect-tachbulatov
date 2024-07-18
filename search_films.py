from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from time import sleep
import allure
import json


class Search_films_and_TV_series:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.kinopoisk.ru/")

    def add_cookie(self):
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                self.browser.add_cookie(cookie)
            self.browser.refresh()

    @allure.step("Поиск фильмов и сериалов")
    def search_content(self, films):
        with allure.step("Загружаем куки для повторного входа"):
            self.add_cookie()

        with allure.step("Ввести в поле поиска название фильма"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[role="combobox"]')\
            .send_keys(films)

        with allure.step("Нажать кнопку 'Поиск'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'button[data-tid="f49ca51f"]')\
                    .send_keys(keys.Keys.ENTER)

        with allure.step("Кликнуть по нужному фильму"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'a[href="/film/5388902/sr/1/"]').click()

        with allure.step("Нажать кнопку 'Смотреть'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'a[data-test-id="Watch"]').click()

        sleep(5)

    @allure.step("Поиск с пустым полем ввода названия")
    def search_content_zero_data(self, films):
        with allure.step("Загружаем куки для повторного входа"):
            self.add_cookie()

        with allure.step("Оставить поле ввода пустым"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[role="combobox"]').send_keys(films)

        with allure.step("Нажать кнопку 'Поиск'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'button[data-tid="f49ca51f"]')\
                    .send_keys(keys.Keys.ENTER)

        with allure.step("Нажать кнопку 'Случайный фильм'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[id="search"]')\
                    .send_keys(keys.Keys.ENTER)

    @allure.step("Ввод в поле поиска только цифр")
    def input_only_numbers(self, films):
        with allure.step("Загружаем куки для повторного входа"):
            self.add_cookie()

        with allure.step("Ввести только цифры"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[role="combobox"]')\
                    .send_keys(films)

        with allure.step("Нажать кнопку 'Поиск'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'button[data-tid="f49ca51f"]')\
                    .send_keys(keys.Keys.ENTER)

    def search_content_by_min_years(self, year):
        with allure.step("Загружаем куки для повторного входа"):
            self.add_cookie()

        with allure.step("Перейти к фильтрам"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]')\
                    .send_keys(keys.Keys.ENTER)

        with allure.step("Заполнить поле ввода поиска по годам"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[id="year"]').send_keys(year)

        with allure.step("Нажать кнопку 'Поиск'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[class="el_18 submit nice_button"]')\
                    .click()

    def search_content_by_max_years(self, year):
        with allure.step("Загружаем куки для повторного входа"):
            self.add_cookie()

        with allure.step("Перейти к фильтрам"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]')\
                    .send_keys(keys.Keys.ENTER)

        with allure.step("Заполнить поле ввода поиска по годам"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[id="year"]').send_keys(year)

        with allure.step("Нажать кнопку 'Поиск'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[class="el_18 submit nice_button"]')\
                    .click()

    def input_incorrect_year(self, year):
        with allure.step("Загружаем куки для повторного входа"):
            self.add_cookie()

        with allure.step("Перейти к фильтрам"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]')\
                    .send_keys(keys.Keys.ENTER)

        with allure.step("Заполнить поле ввода поиска по годам"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[id="year"]').send_keys(year)

        with allure.step("Нажать кнопку 'Поиск'"):
            self.browser.find_element(
                By.CSS_SELECTOR, 'input[class="el_18 submit nice_button"]')\
                    .click()
