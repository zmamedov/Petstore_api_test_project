import json
import allure

from petstore_api_test_project.api.api_requests import post_request


def create_new_pet(url, pet_name):
    payload = json.dumps({
        "name": pet_name
    })
    headers = {
        'Content-Type': 'application/json'
    }
    endpoint = '/v2/pet'

    url = url + endpoint

    with allure.step('Отправить запрос для добавления питомца в магазин.'):
        new_pet = post_request(url, headers, payload)

    with allure.step('Проверка, что API возвращает код статуса 200.'):
        assert new_pet.status_code == 200

    with allure.step(f'Проверить, что имя питомца - "{pet_name}".'):
        assert new_pet.json()['name'] == pet_name

    return new_pet
