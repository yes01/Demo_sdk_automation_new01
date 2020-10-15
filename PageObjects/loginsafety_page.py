from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.basepage import logger
from Common.basepage import BasePage
import time
import allure

class LoginsafetyPage(BasePage):

     #SDK初始化_登录功能
    @allure.step("SDK授权初始化_登录功能")
    def is_authorize_login_safety(self):
        logger.info("-----------------------SDK授权初始化_登录功能-----------------------")
        doc = "SDK授权初始化_登录功能"
        self.click_element(loc.initialization_sdk_01, doc)
        self.wait_eleVisible(loc.initialization_sdk_02, doc=doc)
        self.click_element(loc.initialization_sdk_02, doc)
        self.wait_eleVisible(loc.initialization_sdk_02, doc=doc)
        self.click_element(loc.initialization_sdk_02, doc)
        # self.wait_eleVisible(loc.initialization_sdk_03, doc=doc)
        # self.click_element(loc.initialization_sdk_03, doc)
        # self.wait_eleVisible(loc.initialization_sdk_03, doc=doc)
        # self.click_element(loc.initialization_sdk_03, doc)
        self.wait_eleVisible(loc.login_sdk, doc=doc)
        self.click_element(loc.login_sdk, doc)
        self.wait_eleVisible(loc.login_success, doc=doc)
        self.click_element(loc.login_success, doc)
        time.sleep(3)
        # 平台浮标
        self.Coordinate_positioning(loc.x_y_01)
        time.sleep(2)
        self.Coordinate_positioning(loc.x_y_02)
        self.switch_scenes()

    # SDK初始化_登录功能
    @allure.step("SDK未授权初始化_登录功能")
    def not_authorize_login_safety(self):
        logger.info("-----------------------SDK未授权初始化_登录功能-----------------------")
        doc = "SDK未授权初始化_登录功能"
        self.click_element(loc.initialization_sdk_01, doc)
        self.wait_eleVisible(loc.initialization_sdk_02, doc=doc)
        self.click_element(loc.initialization_sdk_02, doc)
        self.wait_eleVisible(loc.initialization_sdk_02, doc=doc)
        self.click_element(loc.initialization_sdk_02, doc)
        self.wait_eleVisible(loc.login_sdk, doc=doc)
        self.click_element(loc.login_sdk, doc)
        self.wait_eleVisible(loc.login_success, doc=doc)
        self.click_element(loc.login_success, doc)
        time.sleep(8)
        # 平台浮标
        self.Coordinate_positioning(loc.x_y_01)
        time.sleep(2)
        self.Coordinate_positioning(loc.x_y_02)
        self.switch_scenes()







