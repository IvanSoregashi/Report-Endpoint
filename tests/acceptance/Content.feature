Feature: Pages show correct content

  Scenario: Title is shown on the home page
    Given I am on 'home' page
    And I wait for 'container' to load
    Then Title 'All transactions' is shown on the page

  Scenario: Transactions are shown on the home page
    Given I am on 'home' page
    And I wait for 'container' to load
    Then Transactions are shown on the page