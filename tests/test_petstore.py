import json
import requests
from jsonschema import validate

from petstore_api_test_project.pet_methods.create_pet import create_pet
from petstore_api_test_project.utils.path import abs_path_from_project


def test_add_new_pet_to_store():
    new_pet = create_pet(pet_name='Spike')

    assert new_pet.status_code == 200
    assert new_pet.json()['name'] == 'Spike'
    json_file = abs_path_from_project('petstore_api_test_project\\json_schemas\\post_pet.json')
    with open(json_file) as file:
        f = file.read()
        validate(new_pet.json(), schema=json.loads(f))


def test_load_pet_image():
    pass


def test_change_pet_name():
    pass


def test_find_pet_by_id():
    pass


def test_delete_pet():
    pass
