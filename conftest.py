from appium import webdriver

"""set capabilities for your emulator, based on appium inspector"""


class RemoteDriverCaps:
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "13",
        "deviceName": "emulator-5554",
        "appPackage": "com.booking",
        "appActivity": "com.booking.startup.HomeActivity",
        "app": "path to your app",
        "ensureWebviewsHavePages": True,
        "nativeWebScreenshot": True,
        "appWaitDuration": 60000,
        "newCommandTimeout": 35000,
        "autoGrantPermissions": True,
        "connectHardwareKeyboard": True

    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    driver.implicitly_wait(60)


# Create an instance of the RemoteDriverCaps class
remote_driver = RemoteDriverCaps()

# Access the driver instance from the created instance
my_driver = remote_driver.driver
