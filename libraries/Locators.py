from appium.webdriver.common.appiumby import AppiumBy

LOCATORS = {
    "skip_button": ("accessibility id", "Skip"),
    "next_button": ("accessibility id", "Next"),
    "register_button": ("accessibility id", "Register"),
    "country_code_picker": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+1")'),
    "country_search": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("countryCodesPickerSearchInput")'),
    "country_code": lambda code: (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{code}")'),
    "phone_number_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Phone Number")'),
    "phone_number": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone Number")'),
    "send_otp_button": ("accessibility id", "Send OTP"),
    "otp_input": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)'),
    "login_button": ("accessibility id", "Login"),
    "submit_button": ("accessibility id", "Submit"),
    "s_button": ("accessibility id", "Save"),


    "add_deals_button": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add Deals")'),
    "deal_name": lambda name: (AppiumBy.ACCESSIBILITY_ID, name),
    "min_purchase_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("$Amt").instance(0)'),
    "discount_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("$Amt")'),
    "item_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Item")'),
    "date_picker": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)'),
    "date_picker_day": lambda day: (AppiumBy.ACCESSIBILITY_ID, day),
    "save_button": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SAVE")'),
    "publish_button": (AppiumBy.ACCESSIBILITY_ID, "Publish"),


    "add_deals_button": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add Deals")'),
    "deal_name": lambda name: (AppiumBy.ACCESSIBILITY_ID, name),
    "discount_percentage": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("%")'),
    "min_purchase_amount": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("$Amt")'),
    "next_button": (AppiumBy.ACCESSIBILITY_ID, "Next"),
    "expiry_date": lambda date: (AppiumBy.ACCESSIBILITY_ID, date),
    "publish_button": (AppiumBy.ACCESSIBILITY_ID, "Publish"),

    "date_picker_day": lambda day: (AppiumBy.ACCESSIBILITY_ID, day),
    "example_locator": (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]'),

     

    "add_stamp_reward_button": (AppiumBy.ACCESSIBILITY_ID, "Click here to Add, Stamp reward"),
    "reward_name_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter reward name")'),
    "reward_value_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter reward value")'),
    "choose_stamps_button": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Choose Stamps")'),
    "stamp_option": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(15)'),
    "days_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Days")'),
    "reward_description_field": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter reward description")'),


    "print_qr":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(20)'),
    "p_button":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("")'),



    "edit_button1":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("󰏫").instance(0)'),
    "add_image1":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(26)'),
    "gallery":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Gallery")'),
    "camera":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Camera")'),
    "image_select":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(5)'),
    "add_id":(AppiumBy.ID,'com.google.android.providers.media.module:id/button_add'),
    "update_image":(AppiumBy.ACCESSIBILITY_ID,"Update Image"),
    "d_name":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(0)'),
    "d_value":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(1)'),
    "d_short_description":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(2)'),
    "d_full_details":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(3)'),
    "check_box0":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("RNE__Checkbox__Icon").instance(0)'),
    "check_box1":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("RNE__Checkbox__Icon").instance(1)'),
    "check_box2":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("RNE__Checkbox__Icon").instance(2)'),
    "check_box3":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("RNE__Checkbox__Icon").instance(3)'),
    "check_box4":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("RNE__Checkbox__Icon").instance(4)'),
    "additional_t&c":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(4)'),
    "update_deal":(AppiumBy.ACCESSIBILITY_ID,"Update Deal"),


    "deal_selector":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(43)'),
    "deal_delete":(AppiumBy.ACCESSIBILITY_ID,"Delete Deal"),
    "confirmation":(AppiumBy.ACCESSIBILITY_ID,"Yes"),

    "share_button":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("").instance(0)'),
    "share_chrome":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Chrome")'),
    "logout":(AppiumBy.ACCESSIBILITY_ID,", Log Out"),
    "settings":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Settings")'),
    "p_info":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Personal Info")'),
    "b_info":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Business Info")'),
    "add_emp":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(19)'),
    "stamp_reward":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Stamp Reward")'),
    "owner_name":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(12)'),
    "business_name":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(12)'),
    "business_category":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(14)'),
    

}
