from petstore_api_test_project.pet_methods.create_pet import create_pet
from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


def test_add_new_pet_to_store():
    new_pet = create_pet(pet_name='Spike')

    assert new_pet.status_code == 200
    assert new_pet.json()['name'] == 'Spike'
    validate_response_to_json_schema(json_schema='post_pet.json', response=new_pet)


def test_load_pet_image():
    pass


def test_change_pet_name():
    pass


def test_find_pet_by_id():
    pass


def test_delete_pet():
    pass
