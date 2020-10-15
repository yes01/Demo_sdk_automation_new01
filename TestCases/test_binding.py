#coding=utf8
from  PageObjects.index_page import Index
from PageObjects.binding_page import Binding
import pytest
import allure

@allure.title("绑定账号功能")  # 用例标题
@allure.feature("安全信息页面")# 归为大类
@pytest.mark.usefixtures("firsr")
class TestBinding:

    @allure.story("绑定邮箱测试用例-成功案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('email', ["00114@qq.com"])
    def test_bindemail_success(self,access_demo,email):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开安全信息页面 2.进入绑定邮箱界面 3.输入正确的邮箱进行绑定
       '''
       mg = Binding(access_demo)
       mg.bind_email_success(num=email)
       assert mg.is_binding_email(email)
       mg.database_update_email()


    @allure.story("绑定邮箱测试用例-失败案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('email,captcha', [("0011@qq.com","qqqqqq"),("00112@qq.com","6KCDPX")])
    def test_bindemail_fail(self,access_demo,email,captcha):
        '''
         用例描述：
         前置：初始化、登录
         用例步骤：1.打开安全信息页面 2.进入绑定邮箱界面 3.输入不符合条件的邮箱验证码进行绑定
        '''
        mg = Binding(access_demo)
        mg.bind_email_fail(num=email,captcha=captcha)
        assert not mg.is_binding_email(email)

    @allure.story("绑定电话测试用例-成功案例")  # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('phone', ["99633331"])
    def test_bindphone_success(self, access_demo, phone):
        '''
         用例描述：
         前置：初始化、登录
         用例步骤：1.打开安全信息页面 2.进入绑定电话界面 3.输入正确的电话验证码进行绑定
        '''
        mg = Binding(access_demo)
        mg.bind_phone_success(num=phone)
        assert mg.is_binding_phone(phone)
        mg.database_update_phone()

    @allure.story("绑定电话测试用例-失败案例")  # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('phone,captcha', [("98833329","qqqqqq"),("98833329","6KCDPX")])
    def test_bindphone_fail(self, access_demo, phone,captcha):
        '''
         用例描述：
         前置：初始化、登录
         用例步骤：1.打开安全信息页面 2.进入绑定电话界面 3.输入不符合条件的电话验证码进行绑定
        '''
        mg = Binding(access_demo)
        mg.bind_phone_fail(num=phone,captcha=captcha)
        assert not mg.is_binding_phone(phone)


    @allure.story("绑定facebook测试用例-成功案例")  # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('account,pwd', [("17620131946","123456......")])
    def test_bindfacebook_success(self, access_demo, account,pwd):
        '''
         用例描述：
         前置：初始化、登录
         用例步骤：1.打开安全信息页面 2.进入绑定facebook界面 3.输入正确的facebook账号、密码进行绑定
        '''
        mg = Binding(access_demo)
        mg.bind_facebook_success(account=account,pwd=pwd)
        assert mg.is_binding_facebook(account)
        mg.database_update_email()

