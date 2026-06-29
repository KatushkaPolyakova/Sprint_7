import requests
import allure 
from url import URL, GET_ORDERS_BY_NUMBER


class TestGetOrdersByTrack:

    @allure.title('Получить заказ по корректному номеру')
    def test_get_order_by_track_success(self, order):

        with allure.step("Отправить запрос на получение заказа"):
            response = requests.get(URL+GET_ORDERS_BY_NUMBER+ f'?t={order}')

        with allure.step("Проверить ответ сервера"): 
            assert 200 == response.status_code
            assert 'order' in response.json() 


    @allure.title('Запрос без номера')
    def test_get_order_without_track(self):

        with allure.step("Отправить запрос на получение заказа"):
            response = requests.get(URL+GET_ORDERS_BY_NUMBER)
        
        with allure.step("Проверить ответ сервера"):
            assert 400 == response.status_code
            assert response.json()['message'] == 'Недостаточно данных для поиска' 


    @allure.title('Запрос с несуществующим номером')
    def test_get_order_track_invalid(self):

        with allure.step("Отправить запрос на получение заказа"):
            response = requests.get(URL+GET_ORDERS_BY_NUMBER+ f'?t=9999999999')
        
        with allure.step("Проверить ответ сервера"):
            assert 404 == response.status_code
            assert response.json()['message'] == 'Заказ не найден'

