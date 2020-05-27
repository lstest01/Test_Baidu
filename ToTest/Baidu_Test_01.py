# from Data.SeachData import testData
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

    @pytest.mark.parametrize("td",[1,2,3,4,5])
    def test_01(self,td):
        Seach().seach(td)
        # assert td in result

