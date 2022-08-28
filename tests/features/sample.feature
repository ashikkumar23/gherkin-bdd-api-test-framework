Feature: Test CRUD methods in Sample REST API Testing Framework
    As a user, I test CRUD methods
    to ensure POST, GET, UPDATE, DELETE HTTP methods are working as expected

Background:
    Given I set sample "rest_api_base_url"
    And I set header param request content type as "application/json"

@automated
Scenario Outline: POST example
    Given I set POST endpoint to "/posts" for creating posts
    When I send a POST HTTP request with <payload>
    Then I expect HTTP response code of "POST" to be "201"
    And I expect response body of "POST" to be non-empty
    Examples:
        |   payload                                         |
        |   {"title": "foo", "body": "bar", "userId": 1}    |
        |   {"title": "bar", "body": "foo", "userId": 2}    |

@automated
Scenario: GET example
    Given I set GET endpoint to "/posts" for fetching posts
    When I send a GET HTTP request
    Then I expect HTTP response code of "GET" to be "200"
    And I expect response body of "GET" to be non-empty

@manual  # This scenario will be skipped during test execution
Scenario Outline: UPDATE example
    Given I set UPDATE endpoint to "/posts/1" for updating posts
    When I send a PUT HTTP request with <payload>
    Then I expect HTTP response code of "PUT" to be "200"
    And I expect response body of "PUT" to be non-empty
    Examples:
        |   payload                                                         |
        |   {"id": 1, "title": "abc", "body": "xyz", "userId": 1}           |
        |   {"id": 1, "title": "testing", "body": "testing", "userId": 1}   |

@automated
Scenario: DELETE example
    Given I set DELETE endpoint to "/posts/1" for deleting posts
    When I send a DELETE HTTP request
    Then I expect HTTP response code of "DELETE" to be "200"
    And I expect response body of "DELETE" to be empty
