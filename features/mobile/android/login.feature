Feature: Login to the app
  As a user
  I want to log in to the app
  So that I can access the home screen

  Scenario: User logs in with a valid phone number and OTP
    Given the app is launched
    When the user clicks "Skip" on the onboarding screen
    And the user enters phone number "9583590112" and selects country "India" with code "+91"
    And the user clicks "Send OTP"
    And the user enters "4321" as the OTP
    Then the user clicks "Login"