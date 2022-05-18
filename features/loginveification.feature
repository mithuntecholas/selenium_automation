Feature: verify login of orange HRM
  Scenario: LOgin to Orange HRM page with valid parameters
    Given Launch the browser
    When  open the orange hrm website
    And enter username "admin"  and password "admin123"
    And click the login button
    Then User must login to the dashboard page