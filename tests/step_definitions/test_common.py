import os

import pytest
from pytest_bdd import given, parsers

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


@given(parsers.parse('I set sample "{rest_api_base_url}"'))
def set_rest_api_url():
    pytest.globalDict['rest_api_base_url'] = os.environ.get("BASE_URL")


@pytest.fixture
@given(parsers.parse('I set header param request content type as "{header_content_type}"'))
def set_headers(header_content_type):
    return {'Content-type': f'{header_content_type}; charset=UTF-8'}


@given(parsers.parse('I set DELETE endpoint to "{endpoint_url}" for deleting posts'))
@given(parsers.parse('I set UPDATE endpoint to "{endpoint_url}" for updating posts'))
@given(parsers.parse('I set GET endpoint to "{endpoint_url}" for fetching posts'))
@given(parsers.parse('I set POST endpoint to "{endpoint_url}" for creating posts'))
def set_api_endpoint(endpoint_url):
    pytest.globalDict['api_endpoint'] = pytest.globalDict['rest_api_base_url'] + endpoint_url
