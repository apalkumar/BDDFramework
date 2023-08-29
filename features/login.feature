Feature: Login Functionality
  @Login
  Scenario Outline: Login with valid credential
    Given I navigated to Login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
    |email                |password     |
    |abcd1234#@gmail.com  |123456       |
    |abcd1234$@gmail.com  |123456       |
    |abcd1234*@gmail.com  |123456789    |

 @Login
  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email address and valid password into the fields
    And I click on Login button
    Then I should get a proper warning message
    |expected_warning_message                               |
    |Warning: No match for E-Mail Address and/or Password.  |

 @Login
  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email address and invalid password into the fields
    |email_id             |invalid_password |
    |abcd1234#@gmail.com  |2135             |
    And I click on Login button
    Then I should get a proper warning message
    |expected_warning_message                               |
    |Warning: No match for E-Mail Address and/or Password.  |

 @Login
Scenario: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email address and invalid password into the fields
    And I click on Login button
    Then I should get a proper warning message
    |expected_warning_message                               |
    |Warning: No match for E-Mail Address and/or Password.  |

@Login
Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I dont enter anything into email and password the fields
    And I click on Login button
    Then I should get a proper warning message
    |expected_warning_message                               |
    |Warning: No match for E-Mail Address and/or Password.  |