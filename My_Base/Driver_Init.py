from appium import webdriver



def driver_init():
    """
    初始化driver的方法。
    :return: driver对象
    """
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "6"
    caps["deviceName"] = "test001"
    #com.smzdm.client.android /.app.HomeActivity
    caps["appPackage"] = "com.baidu.searchbox"
    caps["appActivity"] = ".MainActivity"
    caps["noReset"] = True  # 初始化，跳过新手教程等。
    caps["unicodeKeyboard"] = True
    caps["resetKeyboard"] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    return driver
