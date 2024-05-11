import requests


def delete_pet(new_pet_id):
    response = requests.delete(
        url=f'https://petstore.swagger.io/v2/pet/{new_pet_id}'
    )

    return response
