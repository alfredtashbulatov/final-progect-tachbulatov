from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import allure
import pytest
from search_films import Search_films_and_TV_series
import json
from time import sleep
import configparser

@allure.title("Просмотр фильмов исериалов")
@allure.description("Тест проверяет поиск фильма(сериала)")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH")
def test_search_films(driver):
    # with allure.step("Инициализировать браузер"):
    #     browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса\
                     Search_films_and_TV_series"):
        search = Search_films_and_TV_series(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content(films="на автомате")

@allure.title("Поиск с пустым полем ввода")
@allure.description("Тест проверяет поиск фильма(сериала) при тустом поле ввода")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH ZERO DATA")
def test_search_zero_data(driver):
    # with allure.step("Инициализировать браузер"):
    #     browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор\
                     класса Search_films_and_TV_series"):
        search = Search_films_and_TV_series(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content_zero_data(films="")
        sleep(5)

@allure.title("Ввод в поле поиска только цифр")
@allure.description("Тест проверяет поиск фильма(сериала), при вводе в поле поиска только цифр")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH ONLY NUMBERS")
def test_only_numbers():
    with allure.step("Инициализировать браузер"):
        browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса Search_films_and_TV_series"):
        search = Search_films_and_TV_series(browser)

    with allure.step("Вызвать метод для поиска"):
        search.input_only_numbers(films="547368769")
        sleep(5)

@allure.title("Поиск фильмов(сериалов) по минимальной дате")
@allure.description("Тест проверяет поиск фильма\
                    (сериала) по мимнимальной дате")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH MIN YEAR")
def test_search_min_year(driver):
    # with allure.step("Инициализировать браузер"):
    #     browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор\
                     класса Search_films_and_TV_series"):
        search = Search_films_and_TV_series(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content_by_min_years(year="1874")
        sleep(5)

@allure.title("Поиск фильмов(сериалов) по максимальной дате")
@allure.description("Тест проверяет поиск фильма\
                    (сериала) по мимнимальной дате")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH MAX YEAR")
def test_search_max_year(driver):
    # with allure.step("Инициализировать браузер"):
    #     browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор\
                     класса Searchfilms_and_TV_series"):
        search = Search_films_and_TV_series(driver)

    with allure.step("Вызвать метод для поиска"):
        search.search_content_by_max_years(year="2050")
        sleep(5)

@allure.title("Поиск фильмов(сериалов)\
              по некорректной дате дате")
@allure.description("Тест проверяет поиск фильма\
                    (сериала) по некорректной дате")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SEARCH INCORRECT YEAR")
def test_search_incorrect_year(driver):
    # with allure.step("Инициализировать браузер"):
    #     browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор\
                     класса Search_films_and_TV_series"):
        search = Search_films_and_TV_series(driver)

    with allure.step("Вызвать метод для поиска"):
        search.input_incorrect_year(year="205")
        sleep(5)
