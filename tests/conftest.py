import pytest
import requests
from helper import register_new_courier_and_return_login_password
from url import URL, LOGIN_COURIER, DELETE_COURIER, CREATE_ORDER


# создает и удаляет курьера
@pytest.fixture
def courier():
    courier = register_new_courier_and_return_login_password()
    
    payload = {'login': courier[0], 'password': courier[1]}
    login_response = requests.post(URL+LOGIN_COURIER, json=payload)

    courier_id = login_response.json()['id']

    yield {
        'login': courier[0],
        'password': courier[1],
        'first_name': courier[2],
        'id': courier_id
    }
    delete_response = requests.delete(URL+DELETE_COURIER+f'/{courier_id}')


@pytest.fixture
def order(): 
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2026-07-01",
        "comment": "test",
        "color": ["BLACK"]
    }

    response = requests.post(URL + CREATE_ORDER,json=payload)
    return response.json()["track"]


#Создает курьера без удаления
@pytest.fixture
def courier_not_delete():
    courier = register_new_courier_and_return_login_password()
    payload = {'login': courier[0], 'password': courier[1]}
    login_response = requests.post(URL+LOGIN_COURIER, json=payload)
    return login_response.json()["id"]


#Удаляет курьера
@pytest.fixture
def delete_courier():
    create_courier = []
    yield create_courier
    for courier in create_courier:
        login_response = requests.post(URL+LOGIN_COURIER, json={"login": courier["login"],"password": courier["password"]})
        courier_id = login_response.json().get('id')
        if courier_id:
            requests.delete(f'{URL}{DELETE_COURIER}/{courier_id}')
