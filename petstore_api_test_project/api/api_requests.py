import requests


def get_request(url):
    response = requests.get(
        url=url
    )

    return response


def post_request(url, headers, data):
    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )

    return response


def delete_request(url):
    response = requests.delete(
        url=url
    )

    return response
