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
    
  Scenario: User adds a new stamp reward
    Given the user is on the reward creation screen
    When the user clicks "Click here to Add, Stamp reward"
    And the user enters "Indri" as the reward name
    And the user enters "50" as the reward value
    And the user clicks "Choose Stamps"
    And the user clicks "Choose Stamps"
    And the user selects the stamp
    And the user enters "10" as the number of days
    And the user enters "Limited offer!!!" as the reward description
    And the user clicks "Save Button"
    Then the reward is created successfully