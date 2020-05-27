from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from My_Base.Driver_Init import driver_init
from My_Page import seach_button


class Base:
    """
    封装基础类的方法。 find/click/sendkeys等
    """
    def __init__(self):
        self.driver = driver_init()

    def find_ele(self,loc,time = 10,p =0.5):
        """
        显式等待 寻找元素的方法封装。
        :param loc: 元组格式， 内容为寻找方法(By.id)+元素,
        :param time: 显式等待 寻找时间默认10秒
        :param frequency: 显式等待，寻找频率，默认0.5秒寻找一次。
        :return: 元素对象
        """
        return WebDriverWait(self.driver,time,p).until(lambda x: x.find_element(*loc))


    def find_eles(self, loc):
        return WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_elements(*loc))


    def click_ele(self,loc):
        """点击元素方法"""
        self.find_ele(loc).click()
    def input_ele(self, loc, text):
        """元素输入"""
        ele = self.find_ele(loc)
        ele.clear()
        ele.send_keys(text)
    def phone_home(self):
        self.driver.press_keycode(3)

    def phone_back(self):
        self.driver.press_keycode(4)

    def quit(self):
        self.driver.quit()








