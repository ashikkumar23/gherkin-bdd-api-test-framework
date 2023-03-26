import pytest
from pytest_bdd import given, parsers


@pytest.fixture
@given("I set sample rest_api_base_url")
def set_rest_api_base_url(base_url):
    return base_url


@pytest.fixture
@given(
    parsers.parse(
        'I set the header param request content type as "{header_content_type}"'
    )
)
def set_headers(header_content_type):
    return {"Content-type": f"{header_content_type}; charset=UTF-8"}


@pytest.fixture
@given(
    parsers.parse('I set the DELETE endpoint to "{endpoint_url}" for deleting posts')
)
@given(
    parsers.parse('I set the UPDATE endpoint to "{endpoint_url}" for updating posts')
)
@given(parsers.parse('I set the GET endpoint to "{endpoint_url}" for fetching posts'))
@given(parsers.parse('I set the POST endpoint to "{endpoint_url}" for creating posts'))
def set_api_endpoint(set_rest_api_base_url, endpoint_url):
    api_endpoint = set_rest_api_base_url + endpoint_url
    return api_endpoint
