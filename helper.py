import requests
import random
import string
from url import URL, CREATE_COURIER


def register_new_courier_and_return_login_password():
   
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []   
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(URL+CREATE_COURIER, json=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def generate_courier_payload():
    return {        
        'login': ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
        'password':''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
        'firstName': ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
        }
