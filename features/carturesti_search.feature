#cream pagina de search pentru Site-ul Carturesti

Feature: this feature will contain only tests related to search
  @carturesti @search @positive_scenario
  Scenario: I am on the main page and search for a specific book
    Given I am on the main page
    When I click on the search button
    When I enter this ISBN code "9781449340377"
    When I click the magnifier
    Then The book with the title "Python Cookbook" should be visible

    @carturesti2 @search
Scenario: I can navigate directly to page 109 for a specific key-word
    Given I am on the main page with "vinyl" keyword and page parameter "109"