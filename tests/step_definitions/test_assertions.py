from assertpy import assert_that
from pytest_bdd import then, parsers


@then(
    parsers.parse(
        'I expect HTTP response code of "{request_type}" to be "{status_code}"'
    )
)
def validate_status_code(context, request_type, status_code):
    if request_type == "POST":
        assert_that(context["post_status_code"]).is_equal_to(int(status_code))
    elif request_type == "GET":
        assert_that(context["get_status_code"]).is_equal_to(int(status_code))
    elif request_type == "PUT":
        assert_that(context["put_status_code"]).is_equal_to(int(status_code))
    elif request_type == "DELETE":
        assert_that(context["delete_status_code"]).is_equal_to(int(status_code))


@then(parsers.parse('I expect response body of "{request_type}" to be empty'))
@then(parsers.parse('I expect response body of "{request_type}" to be non-empty'))
def validate_response_body(context, request_type):
    if request_type == "POST":
        assert_that(context["post_response"]).is_not_equal_to(None)
    elif request_type == "GET":
        assert_that(context["get_response"]).is_not_equal_to(None)
    elif request_type == "PUT":
        assert_that(context["put_response"]).is_not_equal_to(None)
    elif request_type == "DELETE":
        assert_that(context["delete_response"]).is_empty()
