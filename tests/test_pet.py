import allure
from allure_commons.types import Severity

from petstore_api_test_project.api.create_new_pet import create_new_pet
from petstore_api_test_project.api.delete_pet import delete_pet
from petstore_api_test_project.api.find_pet import get_pet_by_id, get_nonexistent_pet_by_id, get_pet_by_status
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

        with allure.step('Проверка, что API возвращает код статуса 200.'):
            assert new_pet.status_code == 200
        with allure.step('Проверка, что имя питомца - "Spike".'):
            assert new_pet.json()['name'] == 'Spike'
        validate_response_to_json_schema(json_schema='post_pet.json', response=new_pet)

    @allure.title('Find pet by ID')
    @allure.story('Return pet')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_find_pet_by_id(self, api_url):
        new_pet = create_new_pet(api_url, pet_name='Miky')

        response = get_pet_by_id(api_url, new_pet)

        with allure.step('Проверка, что API возвращает код статуса 200.'):
            assert response.status_code == 200
        with allure.step('Проверка, что у найденного питомца имя - "Miky".'):
            assert response.json()['name'] == 'Miky'
        validate_response_to_json_schema(json_schema='get_pet.json', response=response)

    @allure.title('Search of non-existent pet')
    @allure.story('Return pet')
    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'zmamedov')
    def test_dont_find_pet_by_id(self, api_url):
        response = get_nonexistent_pet_by_id(api_url, pet_id=111222)

        with allure.step('Проверка, что API возвращает код статуса 404.'):
            assert response.status_code == 404
        with allure.step('Проверка, что в ответе содержится сообщение "Pet not found".'):
            assert response.json()['message'] == 'Pet not found'
        validate_response_to_json_schema(json_schema='get_nonexistent_pet.json', response=response)

    @allure.title('Find all pets with status "pending"')
    @allure.story('Return pet')
    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'zmamedov')
    def test_find_all_pets_with_pending_status(self, api_url):
        response = get_pet_by_status(api_url, status='pending')

        with allure.step('Проверка, что API возвращает код статуса 200.'):
            assert response.status_code == 200
        with allure.step('Проверка, что статус первого питомца в ответе - "pending".'):
            assert response.json()[0]['status'] == 'pending'

    @allure.title('Delete pet in the store')
    @allure.story('Delete pet')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_delete_pet_from_store(self, api_url):
        new_pet = create_new_pet(api_url, pet_name='Lily')

        response, delete_pet_id = delete_pet(api_url, new_pet)

        with allure.step('Проверка, что API возвращает код статуса 200.'):
            assert response.status_code == 200
        with allure.step('Проверка, поле "message" в ответе содержит id удаленного питомца.'):
            assert response.json()['message'] == str(delete_pet_id)
        validate_response_to_json_schema(json_schema='delete_pet.json', response=response)
