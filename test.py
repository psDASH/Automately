from appium import webdriver
from appium.options.common import AppiumOptions

options = AppiumOptions()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.app = "C:\\Users\\prem_\\Downloads\\merchantAppV7.apk"
options.automation_name = "UiAutomator2"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
print("Driver initialized successfully.")
