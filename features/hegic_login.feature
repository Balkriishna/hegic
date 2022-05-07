Feature: Hegic Login

  Scenario: Login to Hegic application with valid credentials
    Given I launch chrome browser
    When I open hegic Homepage
    And Enter valid username "jatin@gmail.com" and password "password"
    And Click on login button
    Then User must successfully login to the homepage
