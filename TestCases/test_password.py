#coding=utf8
from  PageObjects.index_page import Index
from PageObjects.password_page import Password
import pytest
import allure

@allure.title("修改密码功能")  # 用例标题
@allure.feature("安全信息页面")# 归为大类
class TestPassword:

    @pytest.mark.usefixtures("firsr")
    @allure.story("设置密码测试用例-成功案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('pwd01,pwd02', [("12345678","12345678")])
    def test_setpassword_success(self,access_demo,pwd01,pwd02):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开安全信息页面 2.进入设置用户密码界面
       '''
       mg = Password(access_demo)
       mg.set_password(pwd01,pwd02)
       assert mg.is_set_password(pwd01)


    @pytest.mark.usefixtures("firsr")
    @allure.story("设置密码测试用例-失败案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('pwd01,pwd02', [("1234567","1234567")])
    def test_setpassword_fail(self,access_demo,pwd01,pwd02):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开安全信息页面 2.进入设置用户密码界面
       '''
       mg = Password(access_demo)
       mg.set_password(pwd01, pwd02)
       assert not mg.is_set_password(pwd01)

    @pytest.mark.usefixtures("set_password")
    @pytest.mark.usefixtures("firsr")
    @allure.story("修改旧密码测试用例-成功案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('pwd01,pwd02,pwd03', [("12345678","12345679","12345679")])
    def test_modifypassword_success(self,access_demo,pwd01,pwd02,pwd03):
       '''
        用例描述：
        前置：初始化、登录、设置初始密码：12345678
        用例步骤：1.打开安全信息页面 2.选择进入修改旧密码界面 3.修改旧密码
       '''
       mg = Password(access_demo)
       mg.modify_password(pwd01, pwd02,pwd03)
       assert mg.is_set_password(pwd01)

    @pytest.mark.usefixtures("set_password")
    @pytest.mark.usefixtures("firsr")
    @allure.story("修改旧密码测试用例-失败案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('pwd01,pwd02,pwd03', [("12345678","1234567","1234567")])
    def test_modifypassword_fail(self,access_demo,pwd01,pwd02,pwd03):
       '''
        用例描述：
        前置：初始化、登录、设置初始密码：12345678
        用例步骤：1.打开安全信息页面 2.选择进入修改旧密码界面 3.输入错误旧密码进行修改
       '''
       mg = Password(access_demo)
       mg.modify_password(pwd01, pwd02,pwd03)
       assert not mg.is_set_password(pwd01)


    @pytest.mark.usefixtures("set_password")
    @pytest.mark.usefixtures("bind_email")
    @pytest.mark.usefixtures("firsr")
    @allure.story("通过邮箱修改密码测试用例-成功案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('num,pwd01,pwd02', [("010135@gmail.com","12345679","12345679")])
    def test_modifypassword_email_success(self,access_demo,num,pwd01,pwd02):
       '''
        用例描述：
        前置：初始化、登录、设置初始密码：12345678
        用例步骤：1.打开安全信息页面 2.选择进入邮箱修改密码界面 3.输入正确的邮箱验证码进行修改
       '''
       mg = Password(access_demo)
       mg.modify_password_email_success(num=num,pwd01=pwd01,pwd02=pwd02)
       assert mg.is_set_password(pwd01)
       mg.database_update_email()

    @pytest.mark.usefixtures("set_password")
    @pytest.mark.usefixtures("bind_email")
    @pytest.mark.usefixtures("firsr")
    @allure.story("通过邮箱修改密码测试用例-失败案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('captcha,pwd01,pwd02', [("aaaaaa","12345679","12345679")])
    def test_modifypassword_email_fail(self,access_demo,captcha,pwd01,pwd02):
       '''
        用例描述：
        前置：初始化、登录、设置初始密码：12345678
        用例步骤：1.打开安全信息页面 2.选择进入邮箱修改密码界面 3.输入错误的信息进行修改
       '''
       mg = Password(access_demo)
       mg.modify_password_email_fail(captcha=captcha,pwd01=pwd01,pwd02=pwd02)
       assert not mg.is_set_password(pwd01)
       mg.database_update_email()

    @pytest.mark.usefixtures("set_password")
    @pytest.mark.usefixtures("bind_phone")
    @pytest.mark.usefixtures("firsr")
    @allure.story("通过电话修改密码测试用例-成功案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('num,pwd01,pwd02', [("98833331","12345679","12345679")])
    def test_modifypassword_phone_success(self,access_demo,num,pwd01,pwd02):
       '''
        用例描述：
        前置：初始化、登录、设置初始密码：12345678
        用例步骤：1.打开安全信息页面 2.选择进入手机修改密码界面 3.输入正确的手机验证码进行修改
       '''
       mg = Password(access_demo)
       mg.modify_password_phone_success(num=num,pwd01=pwd01,pwd02=pwd02)
       assert mg.is_set_password(pwd01)
       mg.database_update_phone()

    @pytest.mark.usefixtures("set_password")
    @pytest.mark.usefixtures("bind_phone")
    @pytest.mark.usefixtures("firsr")
    @allure.story("通过电话修改密码测试用例-失败案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('captcha,pwd01,pwd02', [("aaaaaa","12345679","12345679")])
    def test_modifypassword_phone_fail(self,access_demo,captcha,pwd01,pwd02):
       '''
        用例描述：
        前置：初始化、登录、设置初始密码：12345678
        用例步骤：1.打开安全信息页面 2.选择进入手机修改密码界面 3.输入错误的信息进行修改
       '''
       mg = Password(access_demo)
       mg.modify_password_phone_fail(captcha=captcha,pwd01=pwd01,pwd02=pwd02)
       assert not mg.is_set_password(pwd01)
       mg.database_update_phone()
