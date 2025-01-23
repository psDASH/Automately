from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from libraries.Locators import LOCATORS

@given("the app is launched")
def step_given_app_is_launched(context):
    # Wait for the skip button to be visible, indicating the app is launched
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Skip']"))  # Replace with your skip button locator
    )
    print("App launched and skip button is visible.")

@when('the user clicks "Skip" on the onboarding screen')
def step_when_user_clicks_skip(context):
    skip_button = context.driver.find_element(*LOCATORS["skip_button"])
    skip_button.click()
    print("Skip button clicked, navigating to login screen.")

@when('the user enters phone number "{phone_number}" and selects country "{country_name}" with code "{country_code}"')
def step_user_enters_phone_and_otp(context, phone_number, country_name, country_code):
    country_picker = context.driver.find_element(*LOCATORS["country_code_picker"])
    country_picker.click()

    country_search = context.driver.find_element(*LOCATORS["country_search_input"])
    country_search.click()
    country_search.send_keys(country_name)
    print(f"Country name '{country_name}' entered.")

    country_code_element = context.driver.find_element(*LOCATORS["country_code"](country_code))
    country_code_element.click()
    print(f"Country code '{country_code}' selected.")

    phone_field = context.driver.find_element(*LOCATORS["phone_number_field"])
    phone_field.click()
    phone_field.send_keys(phone_number)
    print(f"Phone number '{phone_number}' entered.")

@when('the user clicks "Send OTP"')
def step_when_user_clicks_send_otp(context):
    send_otp_button = context.driver.find_element(*LOCATORS["send_otp_button"])
    send_otp_button.click()
    print("Send OTP button clicked.")

@when('the user enters "{otp}" as the OTP')
def step_enter_otp(context, otp):
    for index, digit in enumerate(otp):
        otp_field = context.driver.find_element(*LOCATORS["otp_input"](index))
        otp_field.send_keys(digit)
    print("OTP entered successfully.")

@when('the user clicks "Login"')
def step_when_user_clicks_login(context):
    login_button = context.driver.find_element(*LOCATORS["login_button"])
    login_button.click()
    print("Login button clicked, navigating to home screen.")

@then("the user should be navigated to the home screen")
def step_then_navigate_to_home(context):
    print("Validation successful: Home screen loaded.")
    context.driver.quit()
