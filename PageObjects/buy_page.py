#coding=utf8
import time
import allure
from Common.basepage import logger
from Common.basepage import BasePage
from PageLocators.loginpage_locators import LoginPageLocators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BuyPage(BasePage):

    @allure.step("商品购买页面_google支付")
    def buy_google(self):
        logger.info("-----------------------商品购买页面_google支付-----------------------")
        doc = "商品购买页面_google支付"
        self.wait_eleVisible(loc.bug_submit, doc=doc)
        self.click_element(loc.bug_submit, doc)
        self.wait_eleVisible(loc.initialization_sdk_04, doc=doc)
        self.click_element(loc.initialization_sdk_04, doc)
        time.sleep(3)
        self.switch_scenes()
        self.wait_eleVisible(loc.click_confirm_payment, doc=doc)
        self.click_element(loc.click_confirm_payment, doc)
        time.sleep(3)
        self.Coordinate_positioning(loc.x_y_07)
        time.sleep(4)

    # 购买商品成功
    @allure.step("购买商品结果判断")
    def is_buy(self):

        try:
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[0])
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(
                (By.ID, 'com.crazycube.sdk.demo:id/button3')))
            logger.info("********商品购买页面_google支付：【断言成功】********")
            self.save_screenshot("购买商品成功截图")
            return True

        except:
            logger.info("********商品购买页面_google支付：【断言失败】********")
            self.save_screenshot("购买商品失败截图")
            return False