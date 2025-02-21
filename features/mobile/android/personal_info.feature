Feature: Login and Share Deal Flow
  As a user
  I want to login and share a deal


Background:
    Given the app is launched
    When the user clicks "Skip" on the onboarding screen
    And the user enters phone number "9583590112" and selects country "India" with code "+91"
    And the user clicks "Send OTP"
    And the user enters "4321" as the OTP
    Then the user clicks "Login"

Scenario: User logout
    Given the app is launched
    When the user clicks on settings icon
    And the user clicks on personal info
    And the user edit "Ankit" as the owner name
    
    
    