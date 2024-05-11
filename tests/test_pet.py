from petstore_api_test_project.api.create_new_pet import create_new_pet
from petstore_api_test_project.api.delete_pet import delete_pet
from petstore_api_test_project.api.find_pet import get_pet_by_id, get_nonexisting_pet_by_id, get_pet_by_status
from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


class TestPet:
    def test_add_new_pet_to_store(self):
        new_pet = create_new_pet(pet_name='Spike')

        validate_response_to_json_schema(json_schema='post_pet.json', response=new_pet)

    def test_find_pet_by_id(self):
        new_pet = create_new_pet(pet_name='Miky')

        get_pet_by_id(new_pet)

    def test_dont_find_pet_by_id(self):
        get_nonexisting_pet_by_id(pet_id=111222)

    def test_delete_pet_from_store(self):
        new_pet = create_new_pet(pet_name='Lily')

        delete_pet(new_pet)

    def test_find_all_pets_with_pending_status(self):
        get_pet_by_status(status='pending')
