import requests
import logging

from requests import Response


def get_request(url):
    response = requests.get(
        url=url
    )
    response_logging(response)

    return response


def post_request(url, headers, data):
    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )
    response_logging(response)

    return response


def delete_request(url):
    response = requests.delete(
        url=url
    )
    response_logging(response)

    return response


def response_logging(response: Response):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)
