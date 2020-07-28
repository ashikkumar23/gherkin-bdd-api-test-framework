import ast
import pytest
import requests
from pytest_bdd import given, when, then, parsers, scenarios
import json

scenarios('sample.feature', strict_gherkin=False)


@given('I set sample REST API URL')
def set_rest_api_url():
    pytest.globalDict['api_url'] = 'http://jsonplaceholder.typicode.com'


@given(parsers.parse('I set "{request_type}" posts api endpoint'))
def set_post_and_get_api_endpoint(request_type):
    if request_type == "POST":
        pytest.globalDict['post_api_endpoint'] = pytest.globalDict['api_url']+'/posts'
        print('POST ENDPOINT URL: {}'.format(pytest.globalDict['post_api_endpoint']))
    elif request_type == "GET":
        pytest.globalDict['get_api_endpoint'] = pytest.globalDict['api_url']+'/posts/'
        print('GET ENDPOINT URL: {}'.format(pytest.globalDict['get_api_endpoint']))


@given(parsers.parse('I set header param request content type as "{header_content_type}"'))
def set_header_without_request_body(header_content_type):
    pytest.globalDict['Content-Type'] = header_content_type


@given(parsers.parse('I set "{request_type}" posts api endpoint for "{id}"'))
def set_put_and_delete_api_endpoint(request_type, id):
    if request_type == "PUT":
        pytest.globalDict['put_api_endpoint'] = pytest.globalDict['api_url']+'/posts/'+id
        print('PUT ENDPOINT URL: {}'.format(pytest.globalDict['put_api_endpoint']))
    elif request_type == "DELETE":
        pytest.globalDict['delete_api_endpoint'] = pytest.globalDict['api_url']+'/posts/'+id
        print('DELETE ENDPOINT URL: {}'.format(pytest.globalDict['delete_api_endpoint']))


@when(parsers.parse('I send "{request_type}" HTTP request'))
def send_get_request(request_type):
    if request_type == "GET":
        response = requests.get(url=pytest.globalDict['get_api_endpoint'],
                                headers={"content-type": pytest.globalDict['Content-Type'], "charset": "UTF-8"})
        pytest.globalDict['get_response'] = response.json()
        print("get_response: {}".format(pytest.globalDict['get_response']))
        pytest.globalDict['get_status_code'] = response.status_code


@when(parsers.parse('I send "{request_type}" HTTP request with <payload>'))
def send_post_request(request_type, payload):
    if request_type == "POST":
        response = requests.post(url=pytest.globalDict['post_api_endpoint'],
                                 data=json.dumps(ast.literal_eval(payload)),
                                 headers={"content-type": pytest.globalDict['Content-Type'], "charset": "UTF-8"})
        pytest.globalDict['post_response'] = response.json()
        print("post_response: {}".format(pytest.globalDict['post_response']))
        print("id: {}".format(pytest.globalDict['post_response']['id']))
        pytest.globalDict['post_status_code'] = response.status_code
    if request_type == "PUT":
        response = requests.put(url=pytest.globalDict['put_api_endpoint'],
                                 data=json.dumps(ast.literal_eval(payload)),
                                 headers={"content-type": pytest.globalDict['Content-Type'], "charset": "UTF-8"})
        pytest.globalDict['put_response'] = response.json()
        print("put_response: {}".format(pytest.globalDict['put_response']))
        pytest.globalDict['put_status_code'] = response.status_code
    elif request_type == "DELETE":
        response = requests.delete(url=pytest.globalDict['delete_api_endpoint'],
                                   data=payload,
                                   headers={"content-type": pytest.globalDict['Content-Type'], "charset": "UTF-8"})
        pytest.globalDict['delete_response'] = response.json()
        print("delete_response: {}".format(pytest.globalDict['delete_response']))
        pytest.globalDict['delete_status_code'] = response.status_code


@then(parsers.parse('I receive valid HTTP response code "{status_code}" for "{request_type}"'))
def validate_request(status_code, request_type):
    if request_type == "POST":
        # print(pytest.globalDict['post_status_code'])  # For Debugging
        assert pytest.globalDict['post_status_code'] == int(status_code)
    elif request_type == "GET":
        # print(pytest.globalDict['get_status_code'])  # For Debugging
        assert pytest.globalDict['get_status_code'] == int(status_code)
    elif request_type == "PUT":
        # print(pytest.globalDict['put_status_code'])  # For Debugging
        assert pytest.globalDict['put_status_code'] == int(status_code)
    elif request_type == "DELETE":
        # print(pytest.globalDict['delete_status_code'])  # For Debugging
        assert pytest.globalDict['delete_status_code'] == int(status_code)


@then(parsers.parse('I expect response body "{request_type}" is non-empty'))
def validate_response_body(request_type):
    if request_type == "POST":
        assert pytest.globalDict['post_response'] is not None
    elif request_type == "GET":
        assert pytest.globalDict['get_response'] is not None
    elif request_type == "PUT":
        assert pytest.globalDict['put_response'] is not None
    elif request_type == "DELETE":
        assert pytest.globalDict['delete_response'] == {}


@then(parsers.parse('I expect response body "{request_type}" is empty'))
def validate_delete_response_body(request_type):
    if request_type == "DELETE":
        assert pytest.globalDict['delete_response'] == {}
