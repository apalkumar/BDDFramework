Feature: Register Account Functionality
  @Register
  Scenario: Register with mandatory fields
    Given I navigate to Register page
    When I enter below details into mandatory fields
    |first_name | last_name | telephone | password |
    |First Name | Last Name | 2588      | 123456   |
    And I click on Continue button
    Then Account should get created

  @Register
  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter below details into all fields
    |first_name | last_name | telephone | password |
    |First Name | Last Name | 2588      | 123456   |
    And I click on Continue button
    Then Account should get created

  @Register
  Scenario: Register with duplicate email address
    Given I navigate to Register page
    When I enter below details into all fields except email field
    |first_name | last_name | telephone | password |
    |First Name | Last Name | 2588      | 123456   |
    And I enter existing into the email "abcd1234#@gmail.com" field
    And I click on Continue button
    Then Proper warning message information about duplicate account should be displayed

 @Register
  Scenario: Register without providing any details
    Given I navigate to Register page
    When I enter anything into the fields
    And I click on Continue button
    Then Proper warning message for every mandatory fields should be displayed
