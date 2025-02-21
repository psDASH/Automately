import yaml

class ConfigReader:
    def __init__(self, file_path="config/devices/android.yaml"):
        try:
            with open(file_path, "r") as file:
                self.config = yaml.safe_load(file)
                appium_config = self.get("appium")
                print("Appium Config:", appium_config)

            if not self.config:
                raise ValueError("Config file is empty or improperly formatted.")
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = {}

    def get(self, key, default=None):
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k, default)
        return value
