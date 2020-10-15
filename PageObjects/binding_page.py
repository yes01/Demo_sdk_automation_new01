#coding=utf8
import time
import allure
from Common.basepage import logger
from Common.basepage import BasePage
from PageLocators.loginpage_locators import LoginPageLocators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Binding(BasePage):

    @allure.step("安全信息页面_绑定邮箱功能【success】")
    def bind_email_success(self,database ="CubeAgePlatform",table ="AuthenticationCode",num ="010135@gmail.com"):
        logger.info("-----------------------测试安全信息页面-绑定账号功能-----------------------")
        doc = "安全信息页面_绑定邮箱功能【success】"
        time.sleep(5)
        self.wait_eleVisible(loc.click_binding_email, doc=doc)
        self.click_element(loc.click_binding_email, doc)
        self.wait_eleVisible(loc.set_binding01, doc=doc)
        self.inpt_text(loc.set_binding01, num, doc)
        self.wait_eleVisible(loc.click_captcha_send, doc=doc)
        self.click_element(loc.click_captcha_send, doc)
        time.sleep(2)
        Captcha = self.connect_database_select(database,table,num)
        self.wait_eleVisible(loc.set_binding02, doc=doc)
        self.inpt_text(loc.set_binding02,Captcha, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    @allure.step("安全信息页面_绑定邮箱功能【fail】")
    def bind_email_fail(self,num,captcha):
        logger.info("-----------------------测试安全信息页面-绑定账号功能-----------------------")
        doc = "安全信息页面_绑定邮箱功能【fail】"
        time.sleep(5)
        self.wait_eleVisible(loc.click_binding_email, doc=doc)
        self.click_element(loc.click_binding_email, doc)
        self.wait_eleVisible(loc.set_binding01, doc=doc)
        self.inpt_text(loc.set_binding01, num, doc)
        self.wait_eleVisible(loc.set_binding02, doc=doc)
        self.inpt_text(loc.set_binding02,captcha, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    @allure.step("安全信息页面_绑定电话功能【success】")
    def bind_phone_success(self,database ="CubeAgePlatform",table ="AuthenticationCode",num ="98833331"):
        logger.info("-----------------------测试安全信息页面-绑定账号功能-----------------------")
        doc = "安全信息页面_绑定电话功能【success】"
        time.sleep(5)
        self.wait_eleVisible(loc.click_binding_phone, doc=doc)
        self.click_element(loc.click_binding_phone, doc)
        self.wait_eleVisible(loc.set_binding03, doc=doc)
        self.inpt_text(loc.set_binding03, num, doc)
        self.wait_eleVisible(loc.click_captcha_send, doc=doc)
        self.click_element(loc.click_captcha_send, doc)
        time.sleep(2)
        Captcha = self.connect_database_select(database,table,num)
        self.wait_eleVisible(loc.set_binding02, doc=doc)
        self.inpt_text(loc.set_binding02, Captcha, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    @allure.step("安全信息页面_绑定电话功能【fail】")
    def bind_phone_fail(self,num,captcha):
        logger.info("-----------------------测试安全信息页面-绑定账号功能-----------------------")
        doc = "安全信息页面_绑定电话功能【fail】"
        time.sleep(5)
        self.wait_eleVisible(loc.click_binding_phone, doc=doc)
        self.click_element(loc.click_binding_phone, doc)
        self.wait_eleVisible(loc.set_binding03, doc=doc)
        self.inpt_text(loc.set_binding03, num, doc)
        self.wait_eleVisible(loc.set_binding02, doc=doc)
        self.inpt_text(loc.set_binding02, captcha, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    @allure.step("安全信息页面_绑定facebook功能【success】")
    def bind_facebook_success(self,database ="CubeAgePlatform",table ="AuthenticationCode",account ="",pwd =""):
        logger.info("-----------------------测试安全信息页面-绑定账号功能-----------------------")
        doc = "安全信息页面_绑定facebook功能【success】"
        time.sleep(5)
        self.wait_eleVisible(loc.click_binding_facebook, doc=doc)
        self.click_element(loc.click_binding_facebook, doc)
        time.sleep(3)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.wait_eleVisible(loc.set_account_facebook, doc=doc)
        self.inpt_text(loc.set_account_facebook, account, doc)
        self.wait_eleVisible(loc.set_password_facebook, doc=doc)
        self.inpt_text(loc.set_password_facebook, pwd, doc)
        self.wait_eleVisible(loc.click_login_facebook, doc=doc)
        self.click_element(loc.click_login_facebook, doc)
        time.sleep(3)
        self.Coordinate_positioning(loc.x_y_06)
        # time.sleep(2)
        # self.wait_eleVisible(loc.click_keeplogin_facebook02, doc=doc)
        # self.click_element(loc.click_keeplogin_facebook02, doc)
        time.sleep(10)


    def database_update_email(self):
        logger.info("修改通过email绑定的数据库相关信息")
        self.connect_database_update(loc.sql01,loc.sql03)

    def database_update_phone(self):
        logger.info("修改通过phone绑定的数据库相关信息")
        self.connect_database_update(loc.sql02,loc.sql03)


    # 绑定邮箱成功
    @allure.step("绑定邮箱结果判断")
    def is_binding_email(self, email):

        try:
            WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]')))
            logger.info("********安全信息页面_绑定邮箱功能：绑定的邮箱为{0}【断言成功】********".format(email))
            self.save_screenshot("绑定邮箱断言成功截图")
            return True

        except:
            logger.info("********安全信息页面_绑定邮箱功能：绑定的邮箱为{0}【断言失败】********".format(email))
            self.save_screenshot("绑定邮箱断言失败截图")
            return False

    # 绑定电话成功
    @allure.step("绑定电话结果判断")
    def is_binding_phone(self, phone):

        try:
            WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]')))
            logger.info("********安全信息页面_绑定电话功能：绑定的电话为{0}【断言成功】********".format(phone))
            self.save_screenshot("绑定电话断言成功截图")
            return True

        except:
            logger.info("********安全信息页面_绑定电话功能：绑定的电话为{0}【断言失败】********".format(phone))
            self.save_screenshot("绑定电话断言失败截图")
            return False

    # 绑定facebook成功
    @allure.step("绑定facebook结果判断")
    def is_binding_facebook(self, account):

        try:
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[0])
            WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[6]')))
            logger.info("********安全信息页面_绑定facebook功能：绑定的facebook账号为{0}【断言成功】********".format(account))
            self.save_screenshot("绑定facebook断言成功截图")
            return True

        except:
            logger.info("********安全信息页面_绑定facebook功能：绑定的facebook账号为{0}【断言失败】********".format(account))
            self.save_screenshot("绑定facebook断言失败截图")
            return False







