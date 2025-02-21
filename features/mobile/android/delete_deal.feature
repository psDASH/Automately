Feature: Add Stamp Reward to the app
  As a user
  I want to add a stamp reward
  So that I can create a new reward for my customers


  Background:
    Given the app is launched
    When the user clicks "Skip" on the onboarding screen
    And the user enters phone number "9583590112" and selects country "India" with code "+91"
    And the user clicks "Send OTP"
    And the user enters "4321" as the OTP
    Then the user clicks "Login"
    
Scenario: User delete a deal after login
    Given the app is launched
    When the user clicks on deal
    And the user clicks "Delete Deal" button
    Then the user confirm 