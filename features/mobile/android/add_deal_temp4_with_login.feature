Feature: Registration and Add Deal Flow
  As a user
  I want to login and add a deal4
  So that I can publish it on the app

  Background:
    Given the app is launched
    When the user clicks "Skip" on the onboarding screen
    And the user enters phone number "9583590112" and selects country "India" with code "+91"
    And the user clicks "Send OTP"
    And the user enters "4321" as the OTP
    Then the user clicks "Login"

 Scenario: User adds a new deal with valid details
    Given the app is launched
    When the user clicks "Add Deals"
    And the user selects the deal "Get, BOGO, Buy 1 item Get 1 Item for Free"
    And the user enters "JD" as a Item
    And the user enters "beer" as a Item
    And the user clicks "Next"
    And the user opens the date picker
    And the user sets the end date to "27"
    And the user clicks "SAVE"
    Then the user clicks "Publish"