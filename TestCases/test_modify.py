from PageObjects.modify_page import ModifyPage
from  PageObjects.index_page import Index
import pytest
import allure


@allure.title("修改用户id功能")  # 用例标题
@allure.feature("安全信息页面")# 归为大类
@pytest.mark.usefixtures("firsr")
class TestModify:
    # @pytest.mark.success
    @allure.story("修改用户id测试用例-成功案例") # 归为子类
    @allure.severity(allure.severity_level.NORMAL)  # 发生BUG时的严重程度
    @pytest.mark.parametrize('text', ["qqq016","qqqqqqqqqq1111111112","a.....",
                                      "aqqqqqqqqq__________","21____","2111111111..........",
                                      "a2....","21111..........aqqqq"])
    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_userid_success(self,access_demo,text):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开安全信息页面 2.进入修改用户id界面
       '''
       mg = ModifyPage(access_demo)
       mg.modify_user_id(text)
       assert mg.is_modify_userid(text)
       mg.restore("account_name")


    # @pytest.mark.fail
    @allure.story("修改用户id测试用例-失败案例") # 归为子类
    @allure.severity(allure.severity_level.NORMAL)  # 发生BUG时的严重程度
    @pytest.mark.parametrize('text', [".........","qqqqq","qqqqqqqqqq11111111112",
                                      "111111","QQQQQQ","@@@@@@","!@#$%^"])
    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_userid_fail(self,access_demo,text):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开安全信息页面 2.进入修改用户id界面
       '''
       mg = ModifyPage(access_demo)
       mg.modify_user_id(text)
       assert not mg.is_modify_userid(text)


    @allure.story("修改用户昵称测试用例-成功案例") # 归为子类
    @allure.severity(allure.severity_level.NORMAL)  # 发生BUG时的严重程度
    @pytest.mark.parametrize('text', ["qqq016"])
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_username_success(self,access_demo,text):
       '''
        用例描述：
        前置：初始化、登录
        用例步骤：1.打开用户信息页面 2.进入修改用户昵称界面
       '''
       mg = ModifyPage(access_demo)
       mg.modify_user_name(text)
       assert mg.is_modify_username(text)
       mg.restore("UserName")

