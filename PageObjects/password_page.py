#coding=utf8
import time
import allure
from Common.basepage import logger
from Common.basepage import BasePage
from PageLocators.loginpage_locators import LoginPageLocators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Password(BasePage):

    @allure.step("安全信息页面_设置密码功能")
    def set_password(self,pwd01 ="12345678",pwd02 ="12345678"):
        logger.info("-----------------------测试安全信息页面-设置密码功能-----------------------")
        doc = "安全信息页面_设置密码功能"
        time.sleep(10)
        self.wait_eleVisible(loc.click_password_set, doc=doc)
        self.click_element(loc.click_password_set, doc)
        self.wait_eleVisible(loc.set_password01, doc=doc)
        self.inpt_text(loc.set_password01, pwd01, doc)
        self.wait_eleVisible(loc.set_password02, doc=doc)
        self.inpt_text(loc.set_password02,pwd02, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)
        time.sleep(6)

    @allure.step("安全信息页面_修改密码功能_旧密码")
    def modify_password(self,pwd01,pwd02,pwd03):
        logger.info("-----------------------测试安全信息页面-修改密码功能_旧密码-----------------------")
        doc = "安全信息页面_修改密码功能_旧密码"
        time.sleep(6)
        self.wait_eleVisible(loc.click_password01, doc=doc)
        self.click_element(loc.click_password01, doc)
        self.wait_eleVisible(loc.click_password02, doc=doc)
        self.click_element(loc.click_password02, doc)
        self.wait_eleVisible(loc.set_password01, doc=doc)
        self.inpt_text(loc.set_password01, pwd01)
        self.wait_eleVisible(loc.set_password02, doc=doc)
        self.inpt_text(loc.set_password02,pwd02, doc)
        self.wait_eleVisible(loc.set_password03, doc=doc)
        self.inpt_text(loc.set_password03,pwd03, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    @allure.step("安全信息页面_修改密码功能_email【success】")
    def modify_password_email_success(self,database ="CubeAgePlatform",table ="AuthenticationCode",num ="010119@gmail.com",pwd01 ="12345678",pwd02 ="12345678"):
        logger.info("-----------------------测试安全信息页面-修改密码功能_email【success】-----------------------")
        doc = "安全信息页面_修改密码功能_email【success】"
        time.sleep(4)
        self.wait_eleVisible(loc.click_password01, doc=doc)
        self.click_element(loc.click_password01, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_password03, doc=doc)
        self.click_element(loc.click_password03, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_captcha_send, doc=doc)
        self.click_element(loc.click_captcha_send, doc)
        time.sleep(3)
        Captcha = self.connect_database_select(database, table, num)
        self.wait_eleVisible(loc.set_password02, doc=doc)
        self.inpt_text(loc.set_password02, Captcha, doc)
        self.wait_eleVisible(loc.set_password03, doc=doc)
        self.inpt_text(loc.set_password03,pwd01, doc)
        self.wait_eleVisible(loc.set_password04, doc=doc)
        self.inpt_text(loc.set_password04,pwd02, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    @allure.step("安全信息页面_修改密码功能_email【fail】")
    def modify_password_email_fail(self,captcha,pwd01,pwd02):
        logger.info("-----------------------测试安全信息页面-修改密码功能_email【fail】-----------------------")
        doc = "安全信息页面_修改密码功能_email【fail】"
        time.sleep(4)
        self.wait_eleVisible(loc.click_password01, doc=doc)
        self.click_element(loc.click_password01, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_password03, doc=doc)
        self.click_element(loc.click_password03, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_captcha_send, doc=doc)
        self.click_element(loc.click_captcha_send, doc)
        self.wait_eleVisible(loc.set_password02, doc=doc)
        self.inpt_text(loc.set_password02, captcha, doc)
        self.wait_eleVisible(loc.set_password03, doc=doc)
        self.inpt_text(loc.set_password03,pwd01, doc)
        self.wait_eleVisible(loc.set_password04, doc=doc)
        self.inpt_text(loc.set_password04,pwd02, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    @allure.step("安全信息页面_修改密码功能_phone【success】")
    def modify_password_phone_success(self,database ="CubeAgePlatform",table ="AuthenticationCode",num ="98833325",pwd01 ="12345678",pwd02 ="12345678"):
        logger.info("-----------------------测试安全信息页面-修改密码功能_phone【success】-----------------------")
        doc = "安全信息页面_修改密码功能_phone【success】"
        time.sleep(4)
        self.wait_eleVisible(loc.click_password01, doc=doc)
        self.click_element(loc.click_password01, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_password04, doc=doc)
        self.click_element(loc.click_password04, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_captcha_send, doc=doc)
        self.click_element(loc.click_captcha_send, doc)
        time.sleep(3)
        Captcha = self.connect_database_select(database, table, num)
        self.wait_eleVisible(loc.set_password02, doc=doc)
        self.inpt_text(loc.set_password02, Captcha, doc)
        self.wait_eleVisible(loc.set_password03, doc=doc)
        self.inpt_text(loc.set_password03,pwd01, doc)
        self.wait_eleVisible(loc.set_password04, doc=doc)
        self.inpt_text(loc.set_password04,pwd02, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)


    @allure.step("安全信息页面_修改密码功能_phone【fail】")
    def modify_password_phone_fail(self,captcha,pwd01,pwd02):
        logger.info("-----------------------测试安全信息页面-修改密码功能_phone【fail】-----------------------")
        doc = "安全信息页面_修改密码功能_phone【fail】"
        time.sleep(4)
        self.wait_eleVisible(loc.click_password01, doc=doc)
        self.click_element(loc.click_password01, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_password04, doc=doc)
        self.click_element(loc.click_password04, doc)
        time.sleep(2)
        self.wait_eleVisible(loc.click_captcha_send, doc=doc)
        self.click_element(loc.click_captcha_send, doc)
        self.wait_eleVisible(loc.set_password02, doc=doc)
        self.inpt_text(loc.set_password02, captcha, doc)
        self.wait_eleVisible(loc.set_password03, doc=doc)
        self.inpt_text(loc.set_password03,pwd01, doc)
        self.wait_eleVisible(loc.set_password04, doc=doc)
        self.inpt_text(loc.set_password04,pwd02, doc)
        self.wait_eleVisible(loc.click_submit, doc=doc)
        self.click_element(loc.click_submit, doc)

    def database_update_email(self):
        logger.info("修改通过email绑定的数据库相关信息")
        self.connect_database_update(loc.sql01,loc.sql03)

    def database_update_phone(self):
        logger.info("修改通过phone绑定的数据库相关信息")
        self.connect_database_update(loc.sql02,loc.sql03)

    # 设置用户密码成功
    @allure.step("设置用户密码结果判断")
    def is_set_password(self, pwd):

        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[4]')))
            logger.info("********安全信息页面_设置用户密码功能：设置的密码为{0}【断言成功】********".format(pwd))
            self.save_screenshot("设置用户密码成功截图")
            return True

        except:
            logger.info("********安全信息页面_设置用户密码功能：设置的密码为{0}【断言失败】********".format(pwd))
            self.save_screenshot("设置用户密码失败截图")
            return False










