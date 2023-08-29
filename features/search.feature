Feature: Search Functionality

  @Search
  Scenario: Search For a Valid Product
    Given I got navigate to Home page
    When I entered valid product "HP" into the search box field
    And I click on Search button
    Then Valid product should get displayed in Search results

@Search
  Scenario: Search for an invalid product
    Given I got navigate to Home page
    When I entered Invalid product "honda" into the search box field
    And I click on Search button
    Then Proper message should be displayed in Search Results
    |warning_message                                        |
    |There is no product that matches the search criteria.  |

@Search
  Scenario: Search without entering any product
    Given I got navigate to Home page
    When I dont enter anything into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search Results
    |warning_message                                        |
    |There is no product that matches the search criteria.  |