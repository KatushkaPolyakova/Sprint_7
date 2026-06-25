import requests
import allure 
from url import URL, PUT_ORDERS


class TestPutOrders:

    @allure.title('Успешное принятие заказа')
    def test_put_order_success(self, courier, order):
        response = requests.put(URL+PUT_ORDERS+f"/{order}?courierId={courier['id']}")
        assert 200 == response.status_code
        assert response.json()== {'ok': True}


    @allure.title('Передача заказа без courierId')
    def test_put_order_no_courierId(self, order):
        response = requests.put(URL+PUT_ORDERS+f'/{order}')
        assert 400 == response.status_code
        assert response.json()['message']== 'Недостаточно данных для поиска'


    @allure.title('Передача заказа с неверный courierId')
    def test_put_order_invalid_courierId(self, order):
        response = requests.put(URL+PUT_ORDERS+f'/{order}?courierId=9999999999')
        assert 404 == response.status_code
        assert response.json()['message']== 'Курьера с таким id не существует'


    @allure.title('Передача заказа без id заказа')
    def test_put_order_without_order_id(self, courier):
        response = requests.put(URL+PUT_ORDERS+f"/?courierId={courier['id']}")
        assert 400 == response.status_code
        assert response.json()['message']== 'Недостаточно данных для поиска'


    @allure.title('Передача заказа неверный id заказа')
    def test_put_order_invalid_order_id(self,courier):
        response = requests.put(URL+PUT_ORDERS+f"/9999999999?courierId={courier['id']}")
        assert 404 == response.status_code
        assert response.json()['message']== 'Заказа с таким id не существует'
    
 