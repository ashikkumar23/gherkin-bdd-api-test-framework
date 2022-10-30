@automated
Feature: Test CRUD methods in Sample REST API Testing Framework
    As a user, I test CRUD methods
    to ensure POST, GET, UPDATE, DELETE HTTP methods are working as expected

    Background:
        Given I set sample "rest_api_base_url"
        And I set header param request content type as "application/json"

    @smoke
    Scenario Outline: POST example
        Given I set POST endpoint to "/posts" for creating posts
        When I send a POST HTTP request with <payload>
        Then I expect HTTP response code of "POST" to be "201"
        And I expect response body of "POST" to be non-empty
        Examples:
            |   payload             |
            |   post_payload_1.json |
            |   post_payload_2.json |

    @smoke
    Scenario: GET example
        Given I set GET endpoint to "/posts" for fetching posts
        When I send a GET HTTP request
        Then I expect HTTP response code of "GET" to be "200"
        And I expect response body of "GET" to be non-empty

    @smoke
    Scenario Outline: UPDATE example
        Given I set UPDATE endpoint to "/posts/1" for updating posts
        When I send a PUT HTTP request with <payload>
        Then I expect HTTP response code of "PUT" to be "200"
        And I expect response body of "PUT" to be non-empty
        Examples:
            |   payload             |
            |   put_payload_1.json  |
            |   put_payload_2.json  |

    @smoke
    Scenario: DELETE example
        Given I set DELETE endpoint to "/posts/1" for deleting posts
        When I send a DELETE HTTP request
        Then I expect HTTP response code of "DELETE" to be "200"
        And I expect response body of "DELETE" to be empty
