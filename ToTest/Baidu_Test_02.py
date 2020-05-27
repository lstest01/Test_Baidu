import pytest

class Test_02:

    def setup_class(self):
        print("---------setup_class执行--------------")

    def teardown_class(self):
        print("---------teardown_class执行--------------")

    # def setup(self):
    #     print("---------setup执行--------------------")
    # def teardown(self):
    #     print("---------teardown执行-----------------")
    # @pytest.fixture()
    # def test01(self):
    #     print("----------------test01---------------")
    @pytest.mark.parametrize('t',[1,2,3,4,5])
    # @pytest.mark.usefixtures("test01")
    def test02(self,t):
        print(f"----------------{t}---------------")
    #
    # def test03(self):
    #     print("----------------test03---------------")