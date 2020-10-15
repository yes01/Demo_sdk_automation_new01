#coding=utf8
from  PageObjects.index_page import Index
from PageObjects.addaccount_page import AddaccountPage
import pytest
import allure

@allure.title("添加账号登录")  # 用例标题
@allure.feature("用户信息页面")# 归为大类
@pytest.mark.usefixtures("second")
class TestAccountlogin:

    @allure.story("账号、密码登录测试用例-成功案例") # 归为子类
    @pytest.mark.parametrize('account,pwd', [("1@qq.com","12345678"),("98833329","12345678")])
    def test_accountemail_password_success(self,access_demo,account,pwd):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开信息页面 2.选择添加账号 3.进入登录界面  4.输入正确的账号、密码进行登录
       '''
       mg = AddaccountPage(access_demo)
       mg.addaccount_password_login(account,pwd)
       assert mg.is_login_account(account)

    @allure.story("账号、密码登录测试用例-失败案例")  # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('account,pwd', [("1@qq.com", "123456789"),("98833329","12345679")])
    def test_accountemail_password_fail(self, access_demo, account, pwd):
        '''
         用例描述：
         前置：初始化、登录
         用例步骤：1.打开信息页面 2.选择添加账号 3.进入登录界面  4.输入错误的账号、密码进行登录
        '''
        mg = AddaccountPage(access_demo)
        mg.addaccount_errorpassword_login(account, pwd)
        assert not mg.is_login_account(account)


    @allure.story("验证码登录测试用例-成功案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('account', ["98833329","1@qq.com"])
    def test_accountphone_captcha_success(self,access_demo,account):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开信息页面 2.选择添加账号 3.进入登录界面  4.输入正确的验证码进行登录
       '''
       mg = AddaccountPage(access_demo)
       mg.addaccount_captcha_login("CubeAgePlatform","AuthenticationCode",num=account)
       assert mg.is_login_account(account)


    @allure.story("验证码登录测试用例-失败案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('account', ["98833329","23@qq.com"])
    def test_captchalogin_fail(self,access_demo,account):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开信息页面 2.选择添加账号 3.进入登录界面  4.输入错误的验证码进行登录
       '''
       mg = AddaccountPage(access_demo)
       mg.addaccount_errorcaptcha_login(account)
       assert not mg.is_login_account(account)