Feature: Registration and Add Deal Flow
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

  Scenario: User edit a deal after login
    Given the app is launched
    When the user clicks "Edit Button"
    And the user clicks "+" icon to add image
    And the user select from gallery
    And the user select image
    And the user clicks add button
    And the user clicks update image button
    And the user change "Exclusive Deal" as deal name
    And the user change "90" as deal value
    And the user change "Jaldi Le Le offer khatam ho jayega" as deal short description
    And the user change "Dekh bhai yeah offer sabko nehi milta hai tu lucky customer hai toh tereko mil raha hai baad mai paschatap hoga nehi lene ka" as deal details
    Then the user clicks the Update Deal button
    