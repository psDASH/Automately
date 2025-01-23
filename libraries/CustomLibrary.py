from libraries.ConfigReader import ConfigReader

class CustomLibrary:
    def __init__(self):
        self.config = ConfigReader()

    def get_appium_server_url(self):
        return self.config.get("appium.server_url")

    def get_platform(self):
        return self.config.get("appium.platform")

    def get_device_name(self):
        return self.config.get("appium.device_name")

    def get_app_path(self):
        return self.config.get("appium.app_path")
