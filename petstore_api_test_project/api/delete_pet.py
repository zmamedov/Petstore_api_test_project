import allure

from petstore_api_test_project.api.api_requests import delete_request


def delete_pet(url, pet):
    endpoint = '/v2/pet/'
    pet_id = pet.json()['id']

    url = url + endpoint + f'{pet_id}'

    with allure.step('Отправить запрос для удаления питомца в магазине.'):
        response = delete_request(url)

    return response, pet_id
