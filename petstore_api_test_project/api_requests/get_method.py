import requests


def return_pet(new_pet_id):
    response = requests.get(
        url=f'https://petstore.swagger.io/v2/pet/{new_pet_id}'
    )

    return response
