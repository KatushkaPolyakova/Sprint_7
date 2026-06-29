import requests
import allure 
from helper import generate_courier_payload
from url import URL, CREATE_COURIER


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, delete_courier):
        payload = generate_courier_payload()
        
        with allure.step("Отправить запрос на создание курьера"):
            response = requests.post(URL + CREATE_COURIER, json=payload)
        
        delete_courier.append(payload)

        with allure.step("Проверить ответ сервера"):
            assert 201 == response.status_code 
            assert {"ok":True} == response.json()


    @allure.title("Повторное создание курьера")
    def test_create_courier_same_login_409error(self, courier):
        
        payload = {'login': courier['login'], 'password': courier['password'], 'firstName': courier['first_name']}

        with allure.step("Отправить запрос на повторное создание курьера"):
            response = requests.post(URL+CREATE_COURIER, json=payload)
        
        with allure.step("Проверить ответ сервера"):
            assert 409 == response.status_code
            assert response.json()['message'] == "Этот логин уже используется" 


    @allure.title("Создание курьера без логина")
    def test_create_couirier_not_login_400(self):
        payload = generate_courier_payload()
        del payload['login']

        with allure.step("Отправить запрос на создание курьера"):
            response = requests.post(URL+CREATE_COURIER, json=payload)
        
        with allure.step("Проверить ответ сервера"):
            assert 400 == response.status_code 
            assert response.json()['message'] == "Недостаточно данных для создания учетной записи" 
        

    @allure.title("Создание курьера без пароля")
    def test_create_couirier_not_password(self):
        payload = generate_courier_payload()
        del payload['password']

        with allure.step("Отправить запрос на создание курьера"):
            response = requests.post(URL+CREATE_COURIER, json=payload)
        
        with allure.step("Проверить ответ сервера"):
            assert 400 == response.status_code 
            assert response.json()['message'] == "Недостаточно данных для создания учетной записи" 
     
