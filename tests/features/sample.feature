Feature: Test CRUD methods in Sample REST API Testing Framework
    As a user, I test CRUD methods
    to ensure POST, GET, UPDATE, DELETE HTTP methods are working as expected

Background:
    Given I set sample REST API URL
    And I set header param request content type as "application/json"

@automated
Scenario Outline: POST example
    Given I set "POST" posts api endpoint
#    When I set header param request content type as "application/json"  # Commented and added this to Background step
    When I send "POST" HTTP request with <payload>
    Then I receive valid HTTP response code "201" for "POST"
    And I expect response body "POST" is non-empty
    Examples:
        |   payload                                         |
        |   {"title": "foo", "body": "bar", "userId": 1}    |
        |   {"title": "bar", "body": "foo", "userId": 2}    |

@automated
Scenario: GET example
    Given I set "GET" posts api endpoint
#    When I set header param request content type as "application/json"  # Commented and added this to Background step
    When I send "GET" HTTP request
    Then I receive valid HTTP response code "200" for "GET"
	And I expect response body "GET" is non-empty

@manual  # This scenario will be skipped during test execution
Scenario Outline: UPDATE example
    Given I set "PUT" posts api endpoint for "1"
#    When I set header param request content type as "application/json"  # Commented and added this to Background step
	When I send "PUT" HTTP request with <payload>
    Then I receive valid HTTP response code "200" for "PUT"
	And I expect response body "PUT" is non-empty
    Examples:
        |   payload                                                         |
        |   {"id": 1, "title": "abc", "body": "xyz", "userId": 1}           |
        |   {"id": 1, "title": "testing", "body": "testing", "userId": 1}   |

@automated
Scenario Outline: DELETE example
    Given I set "DELETE" posts api endpoint for "1"
#    When I set header param request content type as "application/json"  # Commented and added this to Background step
    When I send "DELETE" HTTP request with <payload>
    Then I receive valid HTTP response code "200" for "DELETE"
	And I expect response body "DELETE" is empty
    Examples:
        |   payload                                         |
        |   {"title": "foo", "body": "bar", "userId": 1}    |
        |   {"title": "abc", "body": "xyz", "userId": 1}    |
