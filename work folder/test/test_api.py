import requests
import allure
from user_api import Api


@allure.title("Поиск фильмов и сериалов по жанру")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по\
                     жанру с параметрами genre = криминал")
@allure.feature("SEARCH BY GENRES")
@allure.severity(allure.severity_level.BLOCKER)
def test_api_search_by_genres(api: Api):
    with allure.step("Задать значение параметру 'genre'"):
        genre = "криминал"

    with allure.step("Вызвать Api метод для поиска по жанрам"):
        body = api.search_films_by_genres(genre)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и серилов по названию")
@allure.description("Тест вызывает Api метод для поиска\
                    фильмов и сериалов по названию\
                    с параметрами name = холоп")
@allure.feature("SEARCH BY NAME")
@allure.severity(allure.severity_level.BLOCKER)
def test_api_search_by_name(api: Api):
    with allure.step("Задать значение параметру 'name'"):
        name = "холоп"

    with allure.step("Вызвать Api метод для поиска по названию"):
        body = api.search_films_by_name(name)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и сериалов по возростному ограничению")
@allure.description("Тест вызывает Api метод для поиска\
                    фильмов и сериалов по возростному ограничению\
                    с параметром ageRating = 0")
@allure.feature("SEARCH BY AGE-RATING")
@allure.severity(allure.severity_level.BLOCKER)
def test_search_films_by_ageRating(api: Api):
    with allure.step("Задать значение параметру 'ageRating'"):
        ageRating = "0"

    with allure.step("Вызвать Api метод для поиска\
                     по возростному ограничению"):
        body = api.search_films_by_ageRating(ageRating)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск топ 10 фильмов и сериалов")
@allure.description("Тест вызывает Api метод для поиска ТОП-10\
                    фильмов и сериалов с параметром top = top10")
@allure.feature("SEARCH BY TOP-10")
@allure.severity(allure.severity_level.BLOCKER)
def test_search_top_10_films(api: Api):
    with allure.step("Задать значение параметру 'top'"):
        top = "top10"

    with allure.step("Вызвать Api метод для поиска ТОП-10 фильмов и сериалов"):
        body = api.search_top_10_films(top)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и сериалов по рейтингу")
@allure.description("Тест вызывает Api метод для\
                    поиска фильмов и сериалов по ")
@allure.feature("SEARCH BY RATED")
@allure.severity(allure.severity_level.BLOCKER)
def test_search_films_by_rated(api: Api):
    with allure.step("Задать значение параметру 'rating_kp'"):
        rating_kp = "7.2-10"

    with allure.step("Вызвать Api метод для поиска\
                     фильмов и сериалов по рейтингу"):
        body = api.search_films_by_rated(rating_kp)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и сериалов по году")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов\
                    о годам с параметрами 'year=2000'")
@allure.feature("SEARCH BY YEAR")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_films_by_years(api: Api):
    with allure.step("Задать значение параметру 'rating_kp'"):
        year = "2000"

    with allure.step("Вызвать Api метод для\
                     поиска фильмов и сериалов по годам"):
        body = api.search_films_by_years(year)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и сериалов по году большим допустимого значения")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов\
                    по годам большим допустимого значения с\
                    параметрами 'year=2100'")
@allure.feature("SEARCH BY YEAR")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_big_years_nigative(api: Api):
    with allure.step("Задать значение парметру 'year'"):
        year = "2100"

    with allure.step("Вызвать Api метод для поиска фильмов и\
                     сериалов по годам большим допустимого значения"):
        body = api.search_films_by_big_years_nigativ(year)

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message'\
                         из списка 'body' равна 'Значение поля year\
                         должно быть в диапазоне от 1874 до 2050!'"):
            assert body['message'] == [
                                       'Значение поля year должно быть в диапазоне от 1874 до 2050!'
                                      ]


@allure.title("Поиск фильмов и сериалов по году большим допустимого значения")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов\
                    по годам меньшим допустимого значения с параметрами\
                    'year=1870'")
@allure.feature("SEARCH BY YEAR")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_min_years_nigative(api: Api):
    with allure.step("Задать значение парметру 'year'"):
        year = "1870"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов\
                     по годам большим допустимого значения"):
        body = api.search_films_by_min_years_nigativ(year)

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message'\
                         из списка 'body' равна'Значение поля year\
                         должно быть в диапазоне от 1874 до 2050!'"
                         ):
            assert body['message'] == [
                                       'Значение поля year должно быть в диапазоне от 1874 до 2050!'
                                      ]


@allure.title("Поиск фильмов и сериалов по отрицательному рейтингу")
@allure.description("Тест вызывает Api метод для поиска фильмов и\
                    сериалов по отрицательному рейтингу\
                    с параметром rating_kp= -7")
@allure.feature("SEARCH BY RATED")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_rated_nigative(api: Api):
    with allure.step("Задать значение парметру 'rating_kp'"):
        rating_kp = "-7"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов\
                     по отрицательному рейтингу"):
        body = api.search_films_by_rated_nigative(rating_kp)

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в 'body'\
                         больше чем '0'"):
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message'\
                          из списка 'body' равна \
                         'Поле rating.kp должно быть\
                         числом или массивом чисел!',\
                         'Значение поля rating.kp должно быть в\
                         диапазоне от 0 до 10!'"):
            assert body['message'] == [
                                       'Поле rating.kp должно быть числом или массивом чисел!',
                                       'Значение поля rating.kp должно быть в диапазоне от 0 до 10!'
                                      ]


@allure.title("Поиск фильмов и сериалов по неккоректному\
              возростному ограничению")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов\
                    по неккоректному возростному ограничению\
                    с параметрами ageRating=55")
@allure.feature("SEARCH BY AGE-RATING")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_ageRating_nigative(api: Api):
    with allure.step("Задать значение парметру 'ageRating'"):
        ageRating = "55"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов\
                     по неккоректному возростному ограничению"):
        body = api.search_films_by_ageRating_nigative(ageRating)

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в\
                         'body' больше чем '0'"):
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message'\
                         из списка 'body' равна\
                         'Значение поля ageRating должно\
                         быть в диапазоне от 0 до 18!'"):
            assert body['message'] == [
                                       'Значение поля ageRating должно быть в диапазоне от 0 до 18!'
                                      ]
