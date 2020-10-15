#coding=utf8
from PageLocators.loginpage_locators import LoginPageLocators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.basepage import logger
from Common.basepage import BasePage
import allure
import time

class AddaccountPage(BasePage):

     # 添加账号进行账号、密码登录_email、phone
    @allure.step("通过密码添加账号【email、phone】")
    def addaccount_password_login(self,account,pwd):
        logger.info("-----------------------测试信息页面-通过密码添加账号【email、phone】-----------------------")
        doc = "测试信息页面-通过密码添加账号登录功能"
        self.wait_eleVisible(loc.click_switchaccount, doc=doc)
        self.click_element(loc.click_switchaccount, doc)
        self.wait_eleVisible(loc.click_addaccount, doc=doc)
        self.click_element(loc.click_addaccount, doc)
        time.sleep(8)
        self.wait_eleVisible(loc.click_define, doc=doc)
        self.click_element(loc.click_define, doc)
        self.wait_eleVisible(loc.set_account, doc=doc)
        self.inpt_text(loc.set_account, account, doc)
        self.wait_eleVisible(loc.set_pwd, doc=doc)
        self.inpt_text(loc.set_pwd, pwd, doc)
        self.wait_eleVisible(loc.click_login, doc=doc)
        self.click_element(loc.click_login, doc)
        self.wait_eleVisible(loc.click_Choose_role, doc=doc)
        self.click_element(loc.click_Choose_role, doc)


     # 添加账号进行验证码登录_email、phone
    @allure.step("通过验证码添加账号【email、phone】")
    def addaccount_captcha_login(self,database ="CubeAgePlatform",table ="AuthenticationCode",num ="010126@gmail.com"):
        logger.info("-----------------------测试信息页面-通过验证码添加账号【email、phone】-----------------------")
        doc = "测试信息页面-通过验证码添加账号登录功能"
        self.wait_eleVisible(loc.click_switchaccount, doc=doc)
        self.click_element(loc.click_switchaccount, doc)
        self.wait_eleVisible(loc.click_addaccount, doc=doc)
        self.click_element(loc.click_addaccount, doc)
        time.sleep(8)
        self.wait_eleVisible(loc.click_define, doc=doc)
        self.click_element(loc.click_define, doc)
        self.wait_eleVisible(loc.click_captcha_login, doc=doc)
        self.click_element(loc.click_captcha_login, doc)
        self.wait_eleVisible(loc.set_account, doc=doc)
        self.inpt_text(loc.set_account, num, doc)
        self.wait_eleVisible(loc.click_captcha_send, doc=doc)
        self.click_element(loc.click_captcha_send, doc)
        time.sleep(2)
        Captcha = self.connect_database_select(database, table, num)
        self.wait_eleVisible(loc.set_captcha, doc=doc)
        self.inpt_text(loc.set_captcha, Captcha, doc)
        self.wait_eleVisible(loc.click_login, doc=doc)
        self.click_element(loc.click_login, doc)
        self.wait_eleVisible(loc.click_Choose_role, doc=doc)
        self.click_element(loc.click_Choose_role, doc)

     # 添加账号进行facebook登录
    @allure.step("通过facebook添加账号")
    def addaccount_facebook_login(self, account, pwd):
        logger.info("-----------------------测试信息页面-通过facebook添加账号-----------------------")
        doc = "测试信息页面-通过facebook添加账号登录功能"
        self.wait_eleVisible(loc.click_switchaccount, doc=doc)
        self.click_element(loc.click_switchaccount, doc)
        self.wait_eleVisible(loc.click_addaccount, doc=doc)
        self.click_element(loc.click_addaccount, doc)
        time.sleep(8)
        self.wait_eleVisible(loc.click_define, doc=doc)
        self.click_element(loc.click_define, doc)
        self.wait_eleVisible(loc.set_account, doc=doc)
        self.inpt_text(loc.set_account, account, doc)
        self.wait_eleVisible(loc.set_pwd, doc=doc)
        self.inpt_text(loc.set_pwd, pwd, doc)
        self.wait_eleVisible(loc.click_login, doc=doc)
        self.click_element(loc.click_login, doc)
        self.wait_eleVisible(loc.click_Choose_role, doc=doc)
        self.click_element(loc.click_Choose_role, doc)

     # 添加账号进行错误验证码登录_email、phone
    @allure.step("通过错误验证码添加账号【email、phone】")
    def addaccount_errorcaptcha_login(self,account,captcha ="363636"):
        logger.info("-----------------------测试信息页面-通过错误验证码添加账号【email、phone】-----------------------")
        doc = "测试信息页面-通过错误验证码添加账号登录功能"
        self.wait_eleVisible(loc.click_switchaccount, doc=doc)
        self.click_element(loc.click_switchaccount, doc)
        self.wait_eleVisible(loc.click_addaccount, doc=doc)
        self.click_element(loc.click_addaccount, doc)
        time.sleep(8)
        self.wait_eleVisible(loc.click_define, doc=doc)
        self.click_element(loc.click_define, doc)
        self.wait_eleVisible(loc.click_captcha_login, doc=doc)
        self.click_element(loc.click_captcha_login, doc)
        self.wait_eleVisible(loc.set_account, doc=doc)
        self.inpt_text(loc.set_account, account, doc)
        self.wait_eleVisible(loc.set_captcha, doc=doc)
        self.inpt_text(loc.set_captcha, captcha, doc)
        self.wait_eleVisible(loc.click_login, doc=doc)
        self.click_element(loc.click_login)
        time.sleep(2)


     # 添加账号进行错误账号、密码登录_email、phone
    @allure.step("通过错误密码添加账号【email、phone】")
    def addaccount_errorpassword_login(self,account,pwd):
        logger.info("-----------------------测试信息页面-通过错误密码添加账号【email、phone】-----------------------")
        doc = "测试信息页面-通过错误密码添加账号登录功能"
        self.wait_eleVisible(loc.click_switchaccount, doc=doc)
        self.click_element(loc.click_switchaccount, doc)
        self.wait_eleVisible(loc.click_addaccount, doc=doc)
        self.click_element(loc.click_addaccount, doc)
        time.sleep(8)
        self.wait_eleVisible(loc.click_define, doc=doc)
        self.click_element(loc.click_define, doc)
        self.wait_eleVisible(loc.set_account, doc=doc)
        self.inpt_text(loc.set_account, account, doc)
        self.wait_eleVisible(loc.set_pwd, doc=doc)
        self.inpt_text(loc.set_pwd, pwd, doc)
        self.wait_eleVisible(loc.click_login, doc=doc)
        self.click_element(loc.click_login, doc)


    # 验证切换账号登录
    @allure.step("验证切换账号登录结果判断")
    def is_login_account(self, account):

        '''判断是否验证切换账号登录成功 True  False'''
        try:
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[0])
            logger.info("切换到原生页面")
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(
                (By.ID, "com.crazycube.hkmahjongtycoon.app:id/init_sdk")))
            logger.info("********用户信息页面_切换账号登录功能：切换的账号为{0}【断言成功】********".format(account))
            self.save_screenshot("切换账号登录断言成功截图")
            return True

        except:
            logger.info("********用户信息页面_切换账号登录功能：切换的账号为{0}【断言失败】********".format(account))
            self.save_screenshot("切换账号登录断言失败截图")
            return False





