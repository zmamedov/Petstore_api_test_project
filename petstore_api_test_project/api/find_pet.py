import allure
import requests

from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


def get_pet_by_id(pet):
    pet_id = pet.json()['id']

    with allure.step('Отправить запрос для получения питомца по ID.'):
        response = requests.get(
            url=f'https://petstore.swagger.io/v2/pet/{pet_id}'
        )

    with allure.step('Проверка, что API возвращает код статуса 200.'):
        assert response.status_code == 200

    with allure.step(f'Проверка, что у найденного питомца имя - "{response.json()['name']}".'):
        assert response.json()['name'] == pet.json()['name']

    validate_response_to_json_schema(json_schema='get_pet.json', response=response)


def get_nonexisting_pet_by_id(pet_id):
    with allure.step('Отправить запрос для получения питомца по несуществующему ID.'):
        response = requests.get(
            url=f'https://petstore.swagger.io/v2/pet/{pet_id}'
        )

    with allure.step('Проверка, что API возвращает код статуса 404.'):
        assert response.status_code == 404


def get_pet_by_status(status):
    with allure.step(f'Отправить запрос для поиска всех питомцев со статусом "{status}".'):
        response = requests.get(
            url=f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}'
        )

    with allure.step('Проверка, что API возвращает код статуса 200.'):
        assert response.status_code == 200

    with allure.step(f'Проверка, что статус первого питомца в ответе - "{status}".'):
        assert response.json()[0]['status'] == status
