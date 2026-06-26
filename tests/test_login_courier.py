import requests
import allure
from url import URL, LOGIN_COURIER
from helper import generate_courier_payload


class TestLoginCourier:

    @allure.title("Успешный вход курьера")
    def test_login_courier_success(self, courier):
        payload = {'login': courier['login'], 'password': courier['password']}

        with allure.step("Отправить запрос на вход курьера"):
            response = requests.post(URL+LOGIN_COURIER, json=payload)
        
        with allure.step("Проверить ответ сервера"):
            assert 200 == response.status_code
            assert 'id' in response.json()


    @allure.title("Вход курьера без логина")
    def test_login_courier_no_login(self):
        payload = generate_courier_payload()
        del payload['login']

        with allure.step("Отправить запрос на вход курьера"):
            response = requests.post(URL+LOGIN_COURIER, json=payload)
        
        with allure.step("Проверить ответ сервера"):
            assert 400 == response.status_code
            assert response.json()['message'] == "Недостаточно данных для входа"


    @allure.title("Вход курьера без пароля")
    def test_login_courier_no_password(self):
        payload = generate_courier_payload()
        del payload['password']

        with allure.step("Отправить запрос на вход курьера"):
            response = requests.post(URL+LOGIN_COURIER, json=payload)
        
        with allure.step("Проверить ответ сервера"):
            assert 400 == response.status_code
            assert response.json()['message'] == "Недостаточно данных для входа"


    @allure.title("Вход курьера, который не зарегистирован")
    def test_login_courier_no_exist(self):
       payload = generate_courier_payload()
       
       with allure.step("Отправить запрос на вход курьера"):
           response = requests.post(URL+LOGIN_COURIER, json=payload)
       
       with allure.step("Проверить ответ сервера"):
           assert 404 == response.status_code
           assert response.json()['message'] == "Учетная запись не найдена"


    @allure.title("Вход курьера, с неверным паролем")
    def test_login_courier_wrong_password(self, courier):
       payload = {'login': courier['login'], 'password': 'wrong_password'}
       
       with allure.step("Отправить запрос на вход курьера"):
           response = requests.post(URL+LOGIN_COURIER, json=payload)
       
       with allure.step("Проверить ответ сервера"):
           assert 404 == response.status_code
           assert response.json()['message'] == "Учетная запись не найдена"
