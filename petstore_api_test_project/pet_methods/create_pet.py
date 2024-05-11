import json
import requests


def create_pet(pet_name):
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

    return new_pet
