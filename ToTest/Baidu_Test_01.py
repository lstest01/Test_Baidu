# from Data.SeachData import testData
import allure

from My_Page import Page
import pytest
from My_Page.baidu_Seach import Seach

class Test_01:
    def setup_class(self):
        print("开始执行")

    def teardown_class(self):
        Seach().quit()

    # def test0001(self):
    #     print("*"*50)
    #     print(testData())
    @allure.step(title="标题:测试百度搜索")
    # @pytest.allure.severity(pytest.allure.severity_level.BLACKER)
    @pytest.mark.parametrize("td",[1,2,3,4,5])
    def test_01(self,td):
        allure.attach("测试输入和搜索", "搜索列表[1,2,3,4,5]")
        Seach().seach(td)
        # assert td in result

