import requests
import pytest
import allure 
from url import URL, CREATE_ORDER
from data.order_data import order_payload, COLORS


class TestCreateOrder:
    
    @pytest.mark.parametrize('color', COLORS)
    
    @allure.title("Успешное создание заказа с разными цветами")
    def test_create_order_success(self, color):
        payload = order_payload.copy()
        payload['color'] = color

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(URL+CREATE_ORDER, json=payload)
        
        with allure.step("Проверить ответ сервера"):
            assert 201 == response.status_code
            assert 'track' in response.json()

        
    @allure.title("Успешное создание заказа без цвета")
    def test_create_order_without_color_success(self):
        payload = order_payload.copy()

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(URL + CREATE_ORDER, json=payload)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 201
            assert "track" in response.json()

