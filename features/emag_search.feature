
Feature: this test suit tests search feature on Emag.ro website

  @emag
  Scenario: This scenario will test the search feature for a specific keyword
    Given EMAG I am on the main page
    When EMAG I click on the search button
    When EMAG I enter the keyword "colagen"
    When EMAG I click the magnifier
    Then EMAG "colagen" keyword is in title phrasing element

  @emag @negative
  Scenario: This scenario will test a negative case for a non existing product
    Given EMAG I am on the main page
    When EMAG I click on the search button
    When EMAG I enter the keyword "elefantul cicrooo"
    When EMAG I click the magnifier
    Then EMAG "elefantul cicrooo" keyword is in negative title phrasing element
    Then EMAG "0 rezultate pentru:" is in negative title phrasing number element
