from time import sleep
import time
from selenium.webdriver.common.by import By
from My_Base.Base import Base
import My_Page
from My_Page import seach_button
import os,sys
sys.path.append(os.getcwd())


class Seach(Base):

    def __init__(self):
        Base.__init__(self)

    def seach_button_click(self):
        # 点击搜索按钮。
        print(seach_button)
        self.click_ele(seach_button)

    def seach_text(self,loc,text):
        # 输入内容。
        self.input_ele(loc,text)

    def seach_top1_click(self):
        self.click_ele(My_Page.seach_1_click)

    def seach(self, text):
        """搜索方法 汇总， 返回值为页面所有元素 可供assert"""
        self.seach_button_click()
        print(My_Page.seach_text)
        self.seach_text(My_Page.seach_text,text)
        print("输入完毕")
        self.seach_top1_click()
        print("搜索完毕")
        sleep(5)
        name = time.strftime("%Y-%m-%d-%H-%M-%S")
        self.driver.get_screenshot_as_file(f"./TheResult/{name}.png")
        print("截图完毕")
        result = self.driver.page_source
        self.phone_back()
        # return result

