#coding=utf8
import time
import allure
from Common.basepage import logger
from Common.basepage import BasePage
from PageLocators.loginpage_locators import LoginPageLocators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ModifyPage(BasePage):

    @allure.step("安全信息页面_修改用户id功能")
    def modify_user_id(self,text):
        logger.info("-----------------------测试安全信息页面-修改用户id功能-----------------------")
        doc = "安全信息页面_修改用户id功能"
        self.wait_eleVisible(loc.click_userid, doc=doc)
        self.click_element(loc.click_userid, doc)
        self.wait_eleVisible(loc.set_userid, doc=doc)
        self.inpt_text(loc.set_userid, text, doc=doc)
        self.wait_eleVisible(loc.click_userid_submit, doc=doc)
        self.click_element(loc.click_userid_submit, doc)
        time.sleep(3)

    @allure.step("用户信息页面_修改用户昵称功能")
    def modify_user_name(self,text):
        logger.info("-----------------------测试用户信息页面-修改用户昵称功能-----------------------")
        doc = "用户信息页面_修改用户昵称功能"
        time.sleep(3)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.Coordinate_positioning(loc.click_username)
        time.sleep(3)
        self.wait_eleVisible(loc.set_username, doc=doc)
        self.inpt_text(loc.set_username, text, doc=doc)
        self.wait_eleVisible(loc.click_username_submit, doc=doc)
        self.click_element(loc.click_username_submit, doc)
        time.sleep(7)

    #还原用户id&昵称，随机生成数值update数据库
    def restore(self,types):
        random_number = self.generate_verification_code()
        self.connect_database_updateid(types,random_number)

    #修改用户ID成功
    @allure.step("修改用户ID结果判断")
    def is_modify_userid(self,text):

        try:
            WebDriverWait(self.driver, 8, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]')))
            logger.info("********安全信息页面_修改用户id功能：修改的用户ID为{0}【断言成功】********".format(text))
            self.save_screenshot("修改用户ID断言成功截图")
            return  True

        except:
            logger.info("********安全信息页面_修改用户id功能：修改的用户ID为{0}【断言失败】********".format(text))
            self.save_screenshot("修改用户ID断言失败截图")
            return False


    #修改用户昵称成功
    @allure.step("修改用户昵称结果判断")
    def is_modify_username(self,text):

        try:
            WebDriverWait(self.driver, 8, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH,'//*[@class="jsx-4002802977 UserInfo_New_WV_d1"]')))
            logger.info("********用户信息页面_修改用户昵称功能：修改的用户昵称为{0}【断言成功】********".format(text))
            self.save_screenshot("修改用户昵称断言成功截图")
            return  True

        except:
            logger.info("********用户信息页面_修改用户昵称功能：修改的用户昵称为{0}【断言失败】********".format(text))
            self.save_screenshot("修改用户昵称断言失败截图")
            return False





