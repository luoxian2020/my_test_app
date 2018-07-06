import allure
import pytest

class Test_001:

    @allure.step(title='第一个测试')
    def test_001_1(self):
        allure.attach('描述','输入用户名')
        allure.attach('描述','输入密码')
        assert 0

