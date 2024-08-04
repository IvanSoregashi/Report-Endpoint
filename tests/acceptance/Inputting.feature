Feature: Inputting transaction via form

  Scenario: Can input an expense transaction
    Given I am on 'input' page
    And I wait for 'container' to load
    When I input 'type' as 'Expense'
    And I input 'account' as 'Forte'
    And I input 'currency' as 'KZT'
    And I input 'amount' as '100'
    And I input 'category' as 'Transport'
    And I click 'submit'
    Then I am on 'home' page

