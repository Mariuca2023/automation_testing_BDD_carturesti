#This is the file that store all the login tests for the page: URL
Feature: tests for login functionality
  @smoke @skip
  Scenario: negative scenario with incorrect username and password
    Given I am on the login page
    When I insert an username "bogdan12@gmail.com"
    When I insert a password "parolaITF"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your username is invalid!"

  @smoke @high @skip @login @positive
  Scenario: positive scenario
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The banner is displayed
    Then The message is "You logged into a secure area!"

