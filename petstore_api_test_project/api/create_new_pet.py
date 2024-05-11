import json
import allure
import requests


def create_new_pet(pet_name):
    payload = json.dumps({
        "name": pet_name
    })
    headers = {
        'Content-Type': 'application/json'
    }
    with allure.step('Отправить запрос для добавления питомца в магазин.'):
        new_pet = requests.post(
            url='https://petstore.swagger.io/v2/pet',
            headers=headers,
            data=payload
        )

    with allure.step('Проверка, что API возвращает код статуса 200.'):
        assert new_pet.status_code == 200

    with allure.step(f'Проверить, что имя питомца - "{pet_name}".'):
        assert new_pet.json()['name'] == pet_name

    return new_pet
