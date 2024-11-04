Feature: PoetryDB API

  Scenario: Fetch a random poem
    Given the PoetryDB API is available
    When I request a random poem
    Then I should receive a poem with a title and author

  Scenario Outline: Fetch poems by author
    Given the PoetryDB API is available
    When I request poems by the author "<author>"
    Then I should get a 200 status code
    And the request result should match the "<expected>" results file

    Examples:
      | author         | expected                     |
      | Amy Levy       | aly_levy_expected.json       |
      | George Herbert | george_herbert_expected.json |
      | Robinson       | robinson_expected.json       |

  Scenario: Fetch list of authors
    Given the PoetryDB API is available
    When I request the list of authors
    Then I should get a 200 status code
    And the request result should match the "authors_list_expected.json" results file

  Scenario Outline: Fetch list of titles by author
    Given the PoetryDB API is available
    When I request the list of titles from the "<author>"
    Then I should get a 200 status code
    And the request result should match the "<expected>" results file

    Examples:
      | author   | expected                      |
      | Amy Levy | aly_levy_titles_expected.json |
      | Robinson | robinson_titles_expected.json |