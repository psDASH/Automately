Feature: Login and Add Deal Flow
  As a user
  I want to login and add a deal1
  So that I can publish it on the app

  Background:
    Given the app is launched
    When the user clicks "Skip" on the onboarding screen
    And the user enters phone number "9583590112" and selects country "India" with code "+91"
    And the user clicks "Send OTP"
    And the user enters "4321" as the OTP
    Then the user clicks "Login"

  Scenario: User adds a new deal after registration
    Given the user is on the home screen
    When the user clicks "Add Deals"
    And the user selects the deal "Get, $5 off, $5 OFF on min. purchase of $30"
    And the user enters "70" as the minimum purchase amount
    And the user enters "799" as the discount amount
    And the user clicks "Next"
    And the user opens the date picker
    And the user sets the end date to "27"
    And the user clicks "SAVE"
    Then the user clicks "Publish"