import requests

from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


def get_pet_by_id(pet):
    pet_id = pet.json()['id']

    response = requests.get(
        url=f'https://petstore.swagger.io/v2/pet/{pet_id}'
    )

    assert response.status_code == 200
    assert response.json()['name'] == pet.json()['name']
    validate_response_to_json_schema(json_schema='get_pet.json', response=response)


def get_nonexisting_pet_by_id(pet_id):
    response = requests.get(
        url=f'https://petstore.swagger.io/v2/pet/{pet_id}'
    )

    assert response.status_code == 404


def get_pet_by_status(status):
    response = requests.get(
        url=f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}'
    )
    assert response.status_code == 200
    assert response.json()[0]['status'] == status
