#coding=utf8
from  PageObjects.buy_page import BuyPage
import pytest
import allure

@allure.title("google支付功能")  # 用例标题
@allure.feature("商品购买页面")# 归为大类
class TestGooglebuy:

    @pytest.mark.usefixtures("firsr_01")
    @allure.story("google支付功能-成功案例") # 归为子类
    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.parametrize('pwd01,pwd02', [("12345678","12345678")])
    def test_Googlebuy_success(self,access_demo):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开安全信息页面 2.进入设置用户密码界面
       '''
       mg = BuyPage(access_demo)
       mg.buy_google()
       assert mg.is_buy()