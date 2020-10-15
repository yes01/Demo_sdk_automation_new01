from Common.basepage import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Index:
    def __init__(self,driver):
        self.driver = driver



    def is_Login(self):


        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(
                (By.ID,"com.crazycube.sdk.demo:id/textView21")))
            logger.info("********SDK初始化_登录功能【断言成功】********")
            return  True

        except:
            logger.info("********SDK初始化_登录功能【断言失败】********")
            return False
    #修改用户ID成功
    def is_modify_userid01(self,text):

        try:
            WebDriverWait(self.driver, 12, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]')))
            logger.info("********安全信息页面_修改用户id功能：修改的用户ID为{0}【断言成功】********".format(text))
            return  True

        except:
            logger.info("********安全信息页面_修改用户id功能：修改的用户ID为{0}【断言失败】********".format(text))

            return False

   #修改用户ID失败--纯字符
    def is_modify_userid02(self,text):

        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH,'//*[contains(text(),"用戶名格式錯誤（不能純數字或者純符號）")]')))
            logger.info("********安全信息页面_修改用户id功能：修改的用户ID为{0}【断言成功】********".format(text))
            return  True

        except:
            logger.info("********安全信息页面_修改用户id功能：修改的用户ID为{0}【断言失败】********".format(text))
            return False


    # 设置用户密码成功
    def is_set_password(self, pwd):

        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[4]')))
            logger.info("********安全信息页面_设置用户密码功能：设置的密码为{0}【断言成功】********".format(pwd))
            return True

        except:
            logger.info("********安全信息页面_设置用户密码功能：设置的密码为{0}【断言失败】********".format(pwd))
            return False

    # 绑定邮箱成功
    def is_binding_email(self, email):

        try:
            WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]')))
            logger.info("********安全信息页面_绑定邮箱功能：绑定的邮箱为{0}【断言成功】********".format(email))
            return True

        except:
            logger.info("********安全信息页面_绑定邮箱功能：绑定的邮箱为{0}【断言失败】********".format(email))
            return False

    # 绑定电话成功
    def is_binding_phone(self, phone):

        try:
            WebDriverWait(self.driver, 15, 0.5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]')))
            logger.info("********安全信息页面_绑定电话功能：绑定的电话为{0}【断言成功】********".format(phone))
            return True

        except:
            logger.info("********安全信息页面_绑定电话功能：绑定的电话为{0}【断言失败】********".format(phone))
            return False

    # 验证切换账号登录
    def is_login_account(self, account):

        try:
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[0])
            logger.info("切换到原生页面")
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(
                (By.ID, "com.crazycube.hkmahjongtycoon.app:id/init_sdk")))
            logger.info("********用户信息页面_切换账号登录功能：切换的账号为{0}【断言成功】********".format(account))
            return True

        except:
            logger.info("********用户信息页面_切换账号登录功能：切换的账号为{0}【断言失败】********".format(account))
            return False

