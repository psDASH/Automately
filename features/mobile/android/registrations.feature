Feature: Register in the app
  As a user
  I want to register in the app
  So that I can access its features

  Scenario: User registers with a valid phone number and OTP
    Given the app is launched
    When the user clicks "Next"
    And the user clicks "Register"
    And the user enter phone number "9583590111" and selects country "India" with code "+91"
    And the user clicks "Send OTP"
    And the user enters "4321" as the OTP
    