import allure
import pytest

class Test_02:

    def setup_class(self):
        print("---------setup_class执行--------------")

    def teardown_class(self):
        print("---------teardown_class执行--------------")

    def setup(self):
        print("---------setup执行--------------------")
    def teardown(self):
        print("---------teardown执行-----------------")
    @pytest.fixture()
    def test01(self):
        print("----------------test01---------------")
    @pytest.mark.parametrize('t',[1,2,3,4,5])
    @pytest.mark.usefixtures("test01")
    def test02(self,t):
        print(f"----------------{t}---------------")

    @allure.step(title="标题：无关紧要的测试")
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test03(self):
        allure.attach("描述主题：打印", "描述内容：随便打印一些内容吧")
        print("----------------test03---------------")

    @allure.step(title="一个assert失败的测试")
    def test04(self):
        print("")
        assert False