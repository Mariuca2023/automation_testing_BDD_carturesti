Feature: tests for login page
  @CarturestiLogin
  Scenario: negative scenario with incorrect username and password
    Given CARTURESTI I am on the login page
    When CARTURESTI I click on the login button
    When CARTURESTI I click on UTILIZATOR EXISTENT
    When CARTURESTI I insert an username "aprio2018@yahoo.com"
    When CARTURESTI I insert a password "homehome"
    When CARTURESTI I click on the AUTENTIFICARE button
    Then CARTURESTI I am redirected to "https://carturesti.ro/site/login"

  @CarturestiLoginPositive
  Scenario: positive scenario with correct username and password
    Given CARTURESTI I am on the login page
    When CARTURESTI I click on the login button
    When CARTURESTI I click on UTILIZATOR EXISTENT
    When CARTURESTI I insert an username "aprio2019@yahoo.com"
    When CARTURESTI I insert a password "lg.talion"
    When CARTURESTI I click on the AUTENTIFICARE button
    Then CARTURESTI I am redirected to "https://carturesti.ro/site/login"



