@wip
Feature: Login and Logout functionality

  @positive1
  Scenario: a user logins
    Given user is not logged in
    When user click "My Account" and "Login" on upper panel
    When user enters email and password
    And user clicks Login button
    Then user's profile page is launched

  @positive2
  Scenario: a user logouts
    Given user is logged in
    When user click "My Account" and "Logout" on upper panel
    Then "Account logout" info pops up

  @positive3
  Scenario: a user logins then logouts
    When user logins and then logouts
