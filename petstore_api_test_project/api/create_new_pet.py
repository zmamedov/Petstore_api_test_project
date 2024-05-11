import json
import requests


def create_new_pet(pet_name):
    payload = json.dumps({
        "name": pet_name
    })
    headers = {
        'Content-Type': 'application/json'
    }
    new_pet = requests.post(
        url='https://petstore.swagger.io/v2/pet',
        headers=headers,
        data=payload
    )

    assert new_pet.status_code == 200
    assert new_pet.json()['name'] == pet_name

    return new_pet
