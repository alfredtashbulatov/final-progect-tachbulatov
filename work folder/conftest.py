import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from user_api import Api
import json
import configparser

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    
    yield browser
  
    browser.quit()

@pytest.fixture(scope="session")
def base_url():
    return "https://www.kinopoisk.ru/"


# @pytest.fixture
# def cookie_us(browser):
#     with open('cookies.json', 'r') as file:
#             cookies = json.load(file)
#             for cookie in cookies:
#                 browser.add_cookie(cookie)

@pytest.fixture(scope="session")
def url():
    return Api("https://api.kinopoisk.dev")


@pytest.fixture(scope="session")
def token():
    return Api("Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D")
