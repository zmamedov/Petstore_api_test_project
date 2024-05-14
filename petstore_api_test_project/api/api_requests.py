import json

import allure
import requests
import logging

from allure_commons.types import AttachmentType
from requests import Response


def get_request(url, params=None):
    response = requests.get(
        url=url,
        params=params
    )
    response_logging(response)
    response_attaching(response)

    return response


def post_request(url, headers, data):
    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )
    response_logging(response)
    response_attaching(response)

    return response


def delete_request(url):
    response = requests.delete(
        url=url
    )
    response_logging(response)
    response_attaching(response)

    return response


def response_logging(response: Response):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
