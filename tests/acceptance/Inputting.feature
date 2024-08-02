Feature: Inputting transaction via form

  Scenario: Can input an expense transaction
    Given I am on input page
    When I input 'Type' as 'Expense'
    And I input 'Account' as 'Forte'
    And I input 'Currency' as 'KZT'
    And I input 'Amount' as '100'
    And I input 'Category' as 'Transport'
    And I click 'Submit'
    Then I am directed to the 'All transactions' page

