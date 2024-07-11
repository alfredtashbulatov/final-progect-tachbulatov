# final-progect-tachbulatov
from selenium import webdriver
import json

# Сохраняем куки
driver = webdriver.Chrome()
driver.get('https://example.com/login')
# Здесь происходит вход в систему
cookies = driver.get_cookies()
with open('cookies.json', 'w') as file:
    json.dump(cookies, file)

# Загружаем куки для повторного входа
driver = webdriver.Chrome()
driver.get('https://example.com')
with open('cookies.json', 'r') as file:
    cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
driver.refresh()
