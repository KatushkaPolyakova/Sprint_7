import requests
import pytest
import allure 
from url import URL, CREATE_ORDER


class TestCreateOrder:
    
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    
    @allure.title("Успешное создание заказа с разными цветами")
    def test_create_order_success(self, color):
        payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": color
}
        response = requests.post(URL+CREATE_ORDER, json=payload)
        assert 201 == response.status_code
        assert 'track' in response.json()

