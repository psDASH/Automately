

from appium import webdriver
from appium.options.common.base import AppiumOptions

def before_all(context):
    # Appium options configuration
    options = AppiumOptions()
    options.load_capabilities({
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:app": "D:/V2.1.0.apk",  # Update with your APK
        "appium:autoGrantPermissions": True,
        "appium:newCommandTimeout": 3600,
    })

    # Initialize Appium driver
    context.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    print("Driver initialized successfully.")

