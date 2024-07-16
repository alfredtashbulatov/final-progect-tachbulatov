import pytest
from selenium import webdriver

from search_films import Search_films_and_TV_series
from user_api import Api


@pytest.fixture
def driver():
    browser = webdriver.Chrome()

    yield browser

    browser.quit()

@pytest.fixture(scope="session")
def api():
    return Api("https://api.kinopoisk.dev")

