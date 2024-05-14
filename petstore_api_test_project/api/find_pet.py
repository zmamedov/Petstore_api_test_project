import allure

from petstore_api_test_project.api.api_requests import get_request


def get_pet_by_id(url, pet):
    endpoint = '/v2/pet/'
    pet_id = pet.json()['id']

    url = url + endpoint + f'{pet_id}'

    with allure.step('Отправить запрос для получения питомца по ID.'):
        response = get_request(url)

    return response


def get_nonexistent_pet_by_id(url, pet_id):
    endpoint = '/v2/pet/'
    url = url + endpoint + f'{pet_id}'

    with allure.step('Отправить запрос для получения питомца по несуществующему ID.'):
        response = get_request(url)

    return response


def get_pet_by_status(url, status):
    endpoint = '/v2/pet/findByStatus'
    params = {'status': status}

    url = url + endpoint

    with allure.step(f'Отправить запрос для поиска всех питомцев со статусом "{status}".'):
        response = get_request(url, params=params)

    return response
