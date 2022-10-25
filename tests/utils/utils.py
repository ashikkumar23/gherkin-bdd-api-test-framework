import ast
import json

import pytest
import requests


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
        url=f"{post_url}", data=json.dumps(ast.literal_eval(payload)), headers=headers
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
    response = requests.put(
        url=f"{put_url}", data=json.dumps(ast.literal_eval(payload)), headers=headers
    )
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
