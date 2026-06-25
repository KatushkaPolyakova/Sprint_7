import requests
import allure 
from url import URL, GET_ORDERS_BY_NUMBER


class TestGetOrdersByTrack:

    @allure.title('Получить заказ по корректному номеру')
    def test_get_order_by_track_success(self, order):
        response = requests.get(URL+GET_ORDERS_BY_NUMBER+ f'?t={order}')
        assert 200 == response.status_code
        assert 'order' in response.json() 


    @allure.title('Запрос без номера')
    def test_get_order_without_track(self):
        response = requests.get(URL+GET_ORDERS_BY_NUMBER)
        assert 400 == response.status_code
        assert response.json()['message'] == 'Недостаточно данных для поиска' 


    @allure.title('Запрос с несуществующим номером')
    def test_get_order_track_invalid(self):
        response = requests.get(URL+GET_ORDERS_BY_NUMBER+ f'?t=9999999999')
        assert 404 == response.status_code
        assert response.json()['message'] == 'Заказ не найден'

