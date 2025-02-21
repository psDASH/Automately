from behave import given, when, then
from libraries.Locators import LOCATORS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_element(context, locator, description=""):
    element = context.driver.find_element(*locator)
    element.click()
    print(f"{description} clicked successfully.")

def enter_text(context, locator, text, description=""):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.click()  # Click before entering text
        element.clear()  # Clear field (if needed)
        element.send_keys(text)  # Enter text
        print(f"{description}: '{text}' entered successfully.")
    except Exception as e:
        print(f"Error entering text in {description}: {e}")


@given("the app is launched")
def step_given_app_is_launched(context):
    context.driver.implicitly_wait(10)
    print("App launched successfully.")

### Login Flow
@when('the user clicks "Skip" on the onboarding screen')
def step_user_clicks_skip(context):
    click_element(context, LOCATORS["skip_button"], "Skip Button")

@when('the user enters phone number "{phone_number}" and selects country "{country_name}" with code "{country_code}"')
def step_user_enters_phone_and_country(context, phone_number, country_name, country_code):
    click_element(context, LOCATORS["country_code_picker"], "Country Code Picker (+1)")
    enter_text(context, LOCATORS["country_search"], country_name, "Country Search (India)")
    
    country_code_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(LOCATORS["country_code"](country_code))
    )
    country_code_element.click()
    country_code_element.click()
    
    phone_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(LOCATORS["phone_number_field"])
    )
    phone_field.click()
    phone_field.send_keys(phone_number)

@when('the user clicks "Send OTP"')
def step_user_clicks_send_otp(context):
    click_element(context, LOCATORS["send_otp_button"], "Send OTP Button")
    click_element(context, LOCATORS["send_otp_button"], "Send OTP Button")

@when('the user enters "{otp}" as the OTP')
def step_user_enters_otp(context, otp):
    enter_text(context, LOCATORS["otp_input"], otp, "OTP Input Field")
        
@then('the user clicks "Login"')
def step_user_clicks_login(context):
    click_element(context, LOCATORS["login_button"], "Login Button")
    
### Registration Flow
@when('the user clicks "Next"')
def step_user_clicks_next(context):
    click_element(context, LOCATORS["next_button"], "Next Button")
    

@when('the user clicks "Register"')
def step_user_clicks_register(context):
    click_element(context, LOCATORS["register_button"], "Register")


@when('the user enter phone number "{phone_number}" and selects country "{country_name}" with code "{country_code}"')
def step_user_enters_phone_and_country(context, phone_number, country_name, country_code):
    click_element(context, LOCATORS["country_code_picker"], "Country Code Picker (+1)")
    enter_text(context, LOCATORS["country_search"], country_name, "Country Search (India)")
    country_code_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(LOCATORS["country_code"](country_code))
    )
    country_code_element.click()
    
    
    phone_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(LOCATORS["phone_number"])
    )
    phone_field.click()
    phone_field.send_keys(phone_number)


@when('the user clicks "Submit"')
def step_user_clicks_register(context):
    click_element(context, LOCATORS["submit_button"], "Submit")

@given("the user is on the home screen")
def step_user_on_home_screen(context):
    print("User is on the home screen.")

@when('the user clicks "Add Deals"')
def step_user_clicks_add_deals(context):
    click_element(context, LOCATORS["add_deals_button"], "Add Deals Button")

@when('the user selects the deal "{deal_name}"')
def step_user_selects_deal(context, deal_name):
    click_element(context, LOCATORS["deal_name"](deal_name), f"Deal: {deal_name}")

@when('the user enters "{amount}" as the minimum purchase amount')
def step_user_enters_min_purchase(context, amount):
    enter_text(context, LOCATORS["min_purchase_field"], amount, "Minimum Purchase Amount")

@when('the user enters "{amount}" as the discount amount')
def step_user_enters_discount(context, amount):
    enter_text(context, LOCATORS["discount_field"], amount, "Discount Amount")

@when('the user enters "{item}" as a Item')
def step_user_enters_item(context, item):
    enter_text(context, LOCATORS["item_field"], item, "Item")

@when("the user opens the date picker")
def step_user_opens_date_picker(context):
    click_element(context, LOCATORS["date_picker"], "Date Picker")

@when('the user sets the end date to "{day}"')
def step_user_sets_end_date(context, day):
    click_element(context, LOCATORS["example_locator"], "Open Date Picker")
    date_picker_locator = LOCATORS["date_picker_day"](day)
    click_element(context, date_picker_locator, f"Select Day: {day}")


@when('the user clicks "SAVE"')
def step_user_click_save(context):
    click_element(context, LOCATORS["save_button"], "Save Button")

@when('the user clicks "Save Button"')
def step_user_click_save(context):
    click_element(context, LOCATORS["s_button"], "Save Button")

@then('the user clicks "Publish"')
def step_user_clicks_publish(context):
    click_element(context, LOCATORS["publish_button"], "Publish Button")

### Add Deals Flow
@when('the user enters "{discount}" as the discount percentage')
def step_user_enters_discount(context, discount):
    enter_text(context, LOCATORS["discount_percentage"], discount, "Discount Percentage")

@given("the user is on the reward creation screen")
def step_user_on_reward_creation_screen(context):
    print("User is on the reward creation screen.")

@when('the user clicks "Click here to Add, Stamp reward"')
def step_user_clicks_add_stamp_reward(context):
    click_element(context, LOCATORS["add_stamp_reward_button"], "Add Stamp Reward Button")

@when('the user enters "{reward_name}" as the reward name')
def step_user_enters_reward_name(context, reward_name):
    enter_text(context, LOCATORS["reward_name_field"], reward_name, "Reward Name")

@when('the user enters "{reward_value}" as the reward value')
def step_user_enters_reward_value(context, reward_value):
    enter_text(context, LOCATORS["reward_value_field"], reward_value, "Reward Value")

@when('the user clicks "Choose Stamps"')
def step_user_clicks_choose_stamps(context):
    click_element(context, LOCATORS["choose_stamps_button"], "Choose Stamps Button")

@when("the user selects the stamp")
def step_user_selects_stamp(context):
    click_element(context, LOCATORS["stamp_option"], "Stamp Option")

@when('the user enters "{days}" as the number of days')
def step_user_enters_days(context, days):
    enter_text(context, LOCATORS["days_field"], days, "Number of Days")

@when('the user enters "{description}" as the reward description')
def step_user_enters_reward_description(context, description):
    enter_text(context, LOCATORS["reward_description_field"], description, "Reward Description")

@then("the reward is created successfully")
def step_reward_created_successfully(context):
    print("Reward created successfully.")

@when('the user clicks "Print QR"')
def step_print_qr(context):
    click_element(context, LOCATORS["print_qr"], "Print QR")

@then('the clicks  Print button')
def step_p_button(context):
    click_element(context, LOCATORS["p_button"], "Print button")



@when ('the user clicks "Edit Button"')
def step_edit_deal(context):
    click_element(context, LOCATORS["edit_button1"],"Edit Button")

@when ('the user clicks "+" icon to add image')
def step_plus_icon(context):
    click_element(context, LOCATORS["add_image1"],"Plus Button")

@when ('the user select from gallery')
def step_gallery(context):
    click_element(context, LOCATORS["gallery"],"Gallery")

@when ('the user select image')
def step_select_image(context):
    click_element(context, LOCATORS["image_select"],"Select image")

@when ('the user clicks add button')
def step_add_button(context):
    click_element(context, LOCATORS["add_id"],"ADD")


@when ('the user clicks update image button')
def step_update_image(context):
    click_element(context, LOCATORS["update_image"],"Update Image")

@when ('the user change "{updated_deal_name}" as deal name')
def step_modify_dname(context, updated_deal_name):
    enter_text(context, LOCATORS["d_name"], updated_deal_name, "Updated Deal name")

@when ('the user change "{updated_deal_value}" as deal value')
def step_modify_dvalue(context, updated_deal_value):
    enter_text(context, LOCATORS["d_value"], updated_deal_value, "Updated Deal value")

@when('the user change "{updated_deal_description}" as deal short description')
def step_modify_dvalue(context, updated_deal_description):
    enter_text(context, LOCATORS["d_short_description"], updated_deal_description, "Updated Deal Description")

@when ('the user change "{updated_deal_details}" as deal details')
def step_modify_dvalue(context, updated_deal_details):
    enter_text(context, LOCATORS["d_full_details"], updated_deal_details, "Updated Deal Details")

@when ('the user enter "{additional_tandc}" as the additional T&C')
def step_modify_dvalue(context, additional_tandc):
    enter_text(context, LOCATORS["additional_t&c"], additional_tandc, "Additional T&C")

@then ('the user clicks the Update Deal button')
def step_update_deal(context):
    click_element(context, LOCATORS["update_deal"],"Update Deal")


@when ('the user clicks on deal')
def step_select_deal(context):
    click_element(context, LOCATORS["deal_selector"],"Select Deal")

@when ('the user clicks "Delete Deal" button')
def step_delete_deal(context):
    click_element(context, LOCATORS["deal_delete"],"Delete Button")
    
@then ('the user confirm')
def step_confirm_delete_deal(context):
    click_element(context, LOCATORS["confirmation"],"Confirm Delete")

@when ('the user clicks "Share icon" on Deal')
def step_share_deal(context):
    click_element(context, LOCATORS["share_button"],"Share Button")

@then ('the user share the deal on chrome')
def step_share_deal_chrome(context):
    click_element(context, LOCATORS["share_chrome"],"Share in Chrome")


@when ('the user clicks on settings icon')
def step_click_settings(context):
    click_element(context, LOCATORS["settings"],"Settings Button")

@when ('the user clicks on logout button')
def step_click_logout(context):
    click_element(context, LOCATORS["logout"],"Logout Button")

@when('the user clicks on personal info')
def step_click_personalinfo(context):
    click_element(context, LOCATORS["p_info"],"Personal info")

@when ('the user edit "{owner_name}" as the owner name')
def step_modify_ownvalue(context, owner_name):
    enter_text(context, LOCATORS["owner_name"], owner_name, "Owner name")
