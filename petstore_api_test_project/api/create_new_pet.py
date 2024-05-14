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

    return new_pet
