import allure
import pytest
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

from search_films import Search_films_and_TV_series as SF

@pytest.mark.ui_test
@allure.title("Просмотр фильмов исериалов")
@allure.description("Тест проверяет поиск фильма(сериала)")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH")
def test_search_films(driver: WebDriver):
    with allure.step("Передать браузер в конструктор класса\
                     Search_films_and_TV_series"):
        search = SF(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content(films="на автомате")

@pytest.mark.ui_test
@allure.title("Поиск с пустым полем ввода")
@allure.description("Тест проверяет поиск фильма(сериала)\
                    при тустом поле ввода")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH ZERO DATA")
def test_search_zero_data(driver: WebDriver):
    with allure.step("Передать браузер в конструктор\
                     класса Search_films_and_TV_series"):
        search = SF(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content_zero_data(films="")
        sleep(5)

@pytest.mark.ui_test
@allure.title("Ввод в поле поиска только цифр")
@allure.description("Тест проверяет поиск фильма(сериала),\
                    при вводе в поле поиска только цифр")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH ONLY NUMBERS")
def test_only_numbers(driver: WebDriver):
    with allure.step("Передать браузер в конструктор\
                     класса Search_films_and_TV_series"):
        search = SF(driver)

    with allure.step("Вызвать метод для поиска"):
        search.input_only_numbers(films="547368769")
        sleep(5)

@pytest.mark.ui_test
@allure.title("Поиск фильмов(сериалов) по минимальной дате")
@allure.description("Тест проверяет поиск фильма\
                    (сериала) по мимнимальной дате")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH MIN YEAR")
def test_search_min_year(driver: WebDriver):
    with allure.step("Передать браузер в конструктор\
                     класса Search_films_and_TV_series"):
        search = SF(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content_by_min_years(year="1874")
        sleep(5)

@pytest.mark.ui_test
@allure.title("Поиск фильмов(сериалов) по максимальной дате")
@allure.description("Тест проверяет поиск фильма\
                    (сериала) по мимнимальной дате")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH MAX YEAR")
def test_search_max_year(driver: WebDriver):
    with allure.step("Передать браузер в конструктор\
                     класса Searchfilms_and_TV_series"):
        search = SF(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content_by_max_years(year="2050")
        sleep(5)

@pytest.mark.ui_test
@allure.title("Поиск фильмов(сериалов)\
              по некорректной дате дате")
@allure.description("Тест проверяет поиск фильма\
                    (сериала) по некорректной дате")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH INCORRECT YEAR")
def test_search_incorrect_year(driver: WebDriver):
    with allure.step("Передать браузер в конструктор\
                     класса Search_films_and_TV_series"):
        search = SF(driver)

    with allure.step("Вызвать метод для поиска"):
        search.input_incorrect_year(year="205")
        sleep(5)
