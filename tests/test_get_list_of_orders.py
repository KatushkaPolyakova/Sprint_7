import requests
import allure
from url import URL, GET_ORDERS


class TestGetOrders:
    
    @allure.title("Получение списка заказов")
    def test_get_orders_success(self):

        with allure.step("Отправить запрос на получение списка заказов"):
            response = requests.get(URL+GET_ORDERS)
        
        with allure.step("Проверить ответ сервера"):
            assert 200 == response.status_code
            assert 'orders' in response.json()

