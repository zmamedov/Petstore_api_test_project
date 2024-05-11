import json

import allure
from jsonschema import validate

from petstore_api_test_project.utils.path import abs_path_from_project


def validate_response_to_json_schema(json_schema, response):
    json_file = abs_path_from_project(f'petstore_api_test_project/json_schemas/{json_schema}')

    with open(json_file) as file:
        with allure.step('Валидация типов данных.'):
            validate(response.json(), schema=json.loads(file.read()))
