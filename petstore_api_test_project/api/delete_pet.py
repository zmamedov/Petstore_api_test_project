import allure
import requests

from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


def delete_pet(pet):
    pet_id = pet.json()['id']

    with allure.step('Отправить запрос для удаления питомца в магазине.'):
        response = requests.delete(
            url=f'https://petstore.swagger.io/v2/pet/{pet_id}'
        )

    with allure.step('Проверка, что API возвращает код статуса 200.'):
        assert response.status_code == 200

    with allure.step(f'Проверить поле "message" в ответе.'):
        assert response.json()['message'] == str(pet_id)

    validate_response_to_json_schema(json_schema='delete_pet.json', response=response)
