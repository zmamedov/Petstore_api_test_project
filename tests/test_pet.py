import allure
from allure_commons.types import Severity

from petstore_api_test_project.api.create_new_pet import create_new_pet
from petstore_api_test_project.api.delete_pet import delete_pet
from petstore_api_test_project.api.find_pet import get_pet_by_id, get_nonexisting_pet_by_id, get_pet_by_status
from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


@allure.epic('Pet API')
@allure.feature('Tests about pets')
@allure.link('https://petstore.swagger.io/', name='Swagger Petstore')
class TestPet:
    @allure.title('Add new pet to the store')
    @allure.story('Create pet')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_add_new_pet_to_store(self, api_url):
        new_pet = create_new_pet(api_url, pet_name='Spike')

        validate_response_to_json_schema(json_schema='post_pet.json', response=new_pet)

    @allure.title('Find pet by ID')
    @allure.story('Return pet')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_find_pet_by_id(self, api_url):
        new_pet = create_new_pet(api_url, pet_name='Miky')

        get_pet_by_id(api_url, new_pet)

    @allure.title('Search of non-existent pet')
    @allure.story('Return pet')
    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'zmamedov')
    def test_dont_find_pet_by_id(self, api_url):
        get_nonexisting_pet_by_id(api_url, pet_id=111222)

    @allure.title('Find all pets with status "pending"')
    @allure.story('Return pet')
    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'zmamedov')
    def test_find_all_pets_with_pending_status(self, api_url):
        get_pet_by_status(api_url, status='pending')

    @allure.title('Delete pet in the store')
    @allure.story('Delete pet')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_delete_pet_from_store(self, api_url):
        new_pet = create_new_pet(api_url, pet_name='Lily')

        delete_pet(api_url, new_pet)
