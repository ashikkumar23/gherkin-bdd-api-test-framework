@automated
Feature: Test CRUD HTTP methods
  As a user
  I will send POST, GET, UPDATE, and DELETE requests
  I want to be able to see the expected response

  Background:
    Given I set sample rest_api_base_url
    And I set the header param request content type as "application/json"

  @smoke
  Scenario Outline: POST route
    Given I set the POST endpoint to "/posts" for creating posts
    When I send a POST HTTP request with <payload>
    Then I expect the HTTP response code of "POST" to be "201"
    And I expect the response body of "POST" to be non-empty
    Examples:
      | payload             |
      | post_payload_1.json |
      | post_payload_2.json |

  @smoke
  Scenario: GET route
    Given I set the GET endpoint to "/posts" for fetching posts
    When I send a GET HTTP request
    Then I expect the HTTP response code of "GET" to be "200"
    And I expect the response body of "GET" to be non-empty

  @smoke
  Scenario Outline: UPDATE route
    Given I set the UPDATE endpoint to "/posts/1" for updating posts
    When I send a PUT HTTP request with <payload>
    Then I expect the HTTP response code of "PUT" to be "200"
    And I expect the response body of "PUT" to be non-empty
    Examples:
      | payload            |
      | put_payload_1.json |
      | put_payload_2.json |

  @smoke
  Scenario: DELETE route
    Given I set the DELETE endpoint to "/posts/1" for deleting posts
    When I send a DELETE HTTP request
    Then I expect the HTTP response code of "DELETE" to be "200"
    And I expect the response body of "DELETE" to be empty
