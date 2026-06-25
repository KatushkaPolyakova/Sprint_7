import requests
import random
import string
import allure 
from helper import register_new_courier_and_return_login_password
from url import URL, CREATE_COURIER


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self):
        login = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        password = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        first_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        payload = {'login': login, 'password': password, 'firstName': first_name}
        response = requests.post(URL+CREATE_COURIER, json=payload)
        assert 201 == response.status_code 
        assert {"ok":True} == response.json()


    @allure.title("Повторное создание курьера")
    def test_create_courier_same_login_409error(self):
        courier = register_new_courier_and_return_login_password()
        payload = {'login': courier[0], 'password': courier[1], 'firstName': courier[2]}
        response = requests.post(URL+CREATE_COURIER, json=payload)
        assert 409 == response.status_code
        assert response.json()['message'] == "Этот логин уже используется" 


    @allure.title("Создание курьера без логина")
    def test_create_couirier_not_login_400(self):
        payload = {'password': '220077', 'firstName': 'dzhekky'}
        response = requests.post(URL+CREATE_COURIER, json=payload)
        assert 400 == response.status_code 
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи" 
        

    @allure.title("Создание курьера без пароля")
    def test_create_couirier_not_password(self):
        payload = {'login':'gzekkyyy', 'firstName': 'dzhekky'}
        response = requests.post(URL+CREATE_COURIER, json=payload)
        assert 400 == response.status_code 
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи" 
     
