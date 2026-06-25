import requests
import allure 
from url import URL, DELETE_COURIER


class TestDeleteCourier:

    @allure.title ('Успешное удаление курьера')
    def test_delete_courier_success(self, courier_not_delete):
        
        response = requests.delete(URL + DELETE_COURIER + f"/{courier_not_delete['id']}")
        assert response.status_code == 200
        assert response.json() == {"ok": True}


    @allure.title('Запрос на удаление курьера без id')
    def test_delete_courier_no_id(self):
        delete_response = requests.delete(URL+DELETE_COURIER)
        assert 400 == delete_response.status_code
        assert delete_response.json()['message'] == 'Недостаточно данных для удаления курьера'

    
    @allure.title('Запрос на удаление курьера с несуществующим id')
    def test_delete_courier_invalid_id(self):
        delete_response = requests.delete(URL+DELETE_COURIER + '/9999999999')
        assert 404 == delete_response.status_code
        assert delete_response.json()['message'] == 'Курьера с таким id нет'

        