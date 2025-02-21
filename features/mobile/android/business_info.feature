Feature: Registration and Add Deal Flow
  As a user
  I want to login and add a deal5
  So that I can publish it on the app

  Background:
    Given the app is launched
    When the user clicks "Skip" on the onboarding screen
    And the user enters phone number "9583590112" and selects country "India" with code "+91"
    And the user clicks "Send OTP"
    And the user enters "4321" as the OTP
    Then the user clicks "Login"


  Scenario: User wants to edit the business information
    Given the app is launched
    When the user clicks "Add Deals"