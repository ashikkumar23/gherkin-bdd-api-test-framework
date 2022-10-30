import json
from os import path, listdir
from pathlib import Path

import pytest
import requests

from utils.custom_exceptions import InvalidFileFormatException, FileNotFoundException


def read_file(file_name):
    file_path = get_file_path(file_name)
    with open(file_path, encoding="utf-8") as fl:
        extension = path.splitext(file_path)[1]
        if extension == ".json":
            return json.load(fl)
        raise InvalidFileFormatException(
            f"File format {'.' + file_name.split('.')[-1]} is invalid"
        )


def get_file_path(file_name):
    tests_abs_path = path.abspath(".")
    file_path = "".join(
        f"{tests_abs_path}/{d}" for d in listdir(tests_abs_path) if "data" in d
    )
    path_object = Path(f"{file_path}/{file_name}")
    if not path_object.exists():
        raise FileNotFoundException(f"File {file_name} is missing in {file_path}")
    return path_object.resolve()


def get_request(headers):
    get_url = pytest.globalDict["api_endpoint"]
    response = requests.get(url=f"{get_url}", headers=headers)
    print(
        f"Request Method: GET \n"
        f"Request URI: {get_url} \n"
        f"Request Header: {headers} \n"
        f"Response Status Code: {response.status_code} \n"
        f"Response Header Fields: {response.headers} \n"
        f"Response Body: {response.json()} \n"
    )
    return response


def post_request(payload, headers):
    post_url = pytest.globalDict["api_endpoint"]
    response = requests.post(
        url=f"{post_url}", data=json.dumps(payload), headers=headers
    )
    print(
        f"Request Method: POST \n"
        f"Request URI: {post_url} \n"
        f"Request Header: {headers} \n"
        f"Request Body: {payload} \n"
        f"Response Status Code: {response.status_code} \n"
        f"Response Header Fields: {response.headers} \n"
        f"Response Body: {response.json()} \n"
    )
    return response


def put_request(payload, headers):
    put_url = pytest.globalDict["api_endpoint"]
    response = requests.put(url=f"{put_url}", data=json.dumps(payload), headers=headers)
    print(
        f"Request Method: PUT \n"
        f"Request URI: {put_url} \n"
        f"Request Header: {headers} \n"
        f"Request Body: {payload} \n"
        f"Response Status Code: {response.status_code} \n"
        f"Response Header Fields: {response.headers} \n"
        f"Response Body: {response.json()} \n"
    )
    return response


def delete_request(headers):
    delete_url = pytest.globalDict["api_endpoint"]
    response = requests.delete(url=f"{delete_url}", headers=headers)
    print(
        f"Request Method: DELETE \n"
        f"Request URI: {delete_url} \n"
        f"Request Header: {headers} \n"
        f"Response Status Code: {response.status_code} \n"
        f"Response Header Fields: {response.headers} \n"
        f"Response Body: {response.json()} \n"
    )
    return response
