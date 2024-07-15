import requests
import allure

class Api():


    def __init__(self, url: str,  ) -> None:
        self.url = url
        self.headers = {"X-API-KEY": self.get_token}

    @allure.step("Api. Получить токен авторизации")
    def get_token(self):
        token = str("Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D")
        return token

    @allure.step("Api. Поиск фильмов, сериалов по жанру {genre}")
    def search_films_by_genres(self, genre):
        res = requests.get(self.url + "/v1.4/movie?year=2023&genres"
                           + str(genre), headers=self.headers)
        return res.json()

    @allure.step("Api. Поиск фильмов, сериалов по названию {name}")
    def search_films_by_name(self, name):
        res = requests.get(self.url + "/v1.4/movie/search?page=1&limit\
        =1&query=" + str(name), headers=self.headers
        )
        return res.json()

    @allure.step("Api. Поиск фильмов, сериалов по возрастному\
                  ограничению {ageRating}")
    def search_films_by_ageRating(self, ageRating):
        res = requests.get(self.url + "/v1.4/movie?page=1&limit=10&ageRating="
                           + str(ageRating), headers=self.headers
                           )
        return res.json()

    @allure.step("Api. Поиск топ 10 фильмов и сериалов за месяц {top}")
    def search_top_10_films(self, top):
        res = requests.get(self.url + "/v1.4/movie?page=1&notNullFields="
                           + str(top), headers=self.headers
                           )
        return res.json()

    @allure.step("Api. Поиск фильмов и сериалов по рейтингу {rating_kp}")
    def search_films_by_rated(self, rating_kp):
        res = requests.get(self.url + "/v1.4/movie?page=1&limit\
                           =10&selectFields=name&rating.kp="
                           + str(rating_kp), headers=self.headers
                           )
        return res.json()

    @allure.step("Api. Поиск фильмов и сериалов по годам {year}")
    def search_films_by_years(self, year):
        res = requests.get(self.url + "/v1.4/movie?page=1&limit=10&year="
                           + str(year), headers=self.headers
                           )
        return res.json()

    @allure.step("Api. Поиск фильмов и сериалов по годам\
                  большим допустимого значения {year}")
    def search_films_by_big_years_nigativ(self, year):
        res = requests.get(self.url + "/v1.4/movie?page=1&limit=10&year="
                           + str(year), headers=self.headers
                           )
        return res.json()

    @allure.step("Api. Поиск фильмов и сериалов по\
                 отрицательному рейтингу {rating_kp}")
    def search_films_by_rated_nigative(self, rating_kp):
        res = requests.get(self.url + "/v1.4/movie?page=1&limit=10&rating.kp="
                           + str(rating_kp), headers=self.headers
                           )
        return res.json()

    @allure.step("Api. Поиск фильмов, сериалов по некорректному\
                  возрастному ограничению {ageRating}")
    def search_films_by_ageRating_nigative(self, ageRating):
        res = requests.get(self.url + "/v1.4/movie?page=1&limit=10&ageRating="
                           + str(ageRating), headers=self.headers
                           )
        return res.json()

    @allure.step("Api. Поиск фильмов и сериалов по годам\
                  меньшим допустимого значения {year}")
    def search_films_by_min_years_nigativ(self, year):
        res = requests.get(self.url + "/v1.4/movie?page=1&limit=10&year="
                           + str(year), headers=self.headers
                           )
        return res.json()
    