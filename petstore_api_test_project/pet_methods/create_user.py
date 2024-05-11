import json
import requests


def create_user(username):
    payload = json.dumps({
        "id": 0,
        "username": username,
        "firstName": "aaaa",
        "lastName": "xxx",
        "email": "qqqq",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    })
    headers = {
        'Content-Type': 'application/json'
    }
    new_user = requests.post(
        url='https://petstore.swagger.io/v2/user',
        headers=headers,
        data=payload
    )

    return new_user
