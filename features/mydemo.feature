Feature: Orange Hrm logo
  Scenario: Checking LOgo present on  Orange Hrm home page
    Given Launch chrome browser
    When open Orange hrm home page
    Then verify logo present on home page
    And close browser
