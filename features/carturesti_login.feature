Feature: tests for login page
  @CarturestiLogin
  Scenario: negative scenario with incorrect username and password
    Given CARTURESTI I am on the login page
    When CARTURESTI I click on "COOKIES_BUTTON"
    When CARTURESTI I click on the login button
    When CARTURESTI I click on UTILIZATOR EXISTENT
    When CARTURESTI I insert an username "bogdan12@gmail.com"
    When CARTURESTI I insert a password "parolaITF"
#    When CARTURESTI I click on the login button
#    Then CARTURESTI The message is displayed
#    Then CARTURESTI The message is "Adresă de email sau parolă incorectă."


