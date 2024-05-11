import requests

from petstore_api_test_project.pet_methods.create_pet import create_pet
from petstore_api_test_project.pet_methods.create_user import create_user
from petstore_api_test_project.pet_methods.delete_pet import delete_pet
from petstore_api_test_project.pet_methods.get_pet import return_pet
from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


def test_add_new_pet_to_store():
    new_pet = create_pet(pet_name='Spike')

    assert new_pet.status_code == 200
    assert new_pet.json()['name'] == 'Spike'
    validate_response_to_json_schema(json_schema='post_pet.json', response=new_pet)


def test_load_pet_image():
    pass


def test_create_user():
    new_user = create_user(username='Kate')
    assert new_user.status_code == 200
    validate_response_to_json_schema(json_schema='post_user.json', response=new_user)


def test_find_pet_by_id():
    new_pet = create_pet(pet_name='Miky')
    new_pet_id = new_pet.json()['id']

    response = return_pet(new_pet_id)

    assert response.status_code == 200
    assert response.json()['name'] == 'Miky'
    validate_response_to_json_schema(json_schema='get_pet.json', response=response)


def test_delete_pet():
    new_pet = create_pet(pet_name='Miky')
    new_pet_id = new_pet.json()['id']

    response = delete_pet(new_pet_id)
    assert response.status_code == 200
    assert response.json()['message'] == str(new_pet_id)
    validate_response_to_json_schema(json_schema='delete_pet.json', response=response)
