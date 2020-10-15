# -*- coding: UTF-8 -*-
from appium import webdriver
from Common.Log import Log
# from sshtunnel import SSHTunnelForwarder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string, random
import traceback
import pymysql
import datetime
import  time
import allure
import os

logger = Log(logger="BasePage").getlog()
class  BasePage:


    def __init__(self,driver):
        self.driver = driver



    #等待元素可见
    def wait_eleVisible(self,locator,times=20,poll_frequency=0.5,doc=""):
        try:

            #开始等待时间
            star = datetime.datetime.now()
            # return WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待的时间
            end = datetime.datetime.now()
            times = str((end - star).seconds)
            logger.info("等待元素{0}可见".format(locator))
            logger.info("等待时长为：{}秒".format(times))
        except:
            logger.exception("等待元素可见失败！！！{}".format(locator))
            #截图
            self.save_screenshot(doc)
            raise

    #查找元素
    def get_element(self,locator,doc=""):
        logger.info("查找元素：{}成功".format(locator))
        try:
            return self.driver.find_element(*locator)

        except:
            logger.exception("查找元素失败！！！{}".format(locator))
            #截图
            self.save_screenshot(doc)
            raise

    # 坐标查找元素
    def Coordinate_positioning(self, locator):
        try:
            self.driver.tap(locator[0],locator[1])
            logger.info("坐标查找元素：{}成功".format(locator))
        except:
            logger.exception("坐标查找元素失败！！！{}".format(locator))
            # 截图
            # self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator,doc=""):
        #找元素
        ele = self.get_element(locator,doc)
        try:
            ele.click()
            logger.info("点击元素：{}成功".format(locator))
        except:
            logger.exception("元素点击失败！！！{}".format(locator))
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def inpt_text(self, locator,text,doc=""):
        # 找元素
        ele = self.get_element(locator,doc)
        try:
            ele.clear()
            logger.info("成功清空输入框内容")
            ele.send_keys(text)
            logger.info("输入的文本内容为：{}".format(text))
        except:
            logger.exception("元素输入操作失败！！！{}".format(text))
            # 截图
            # self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator):
        # 找元素
        ele = self.get_element(locator)
        try:
            return ele.text
        except:
            logger.exception("获取元素的文本内容失败！！！")
            # 截图
            # self.save_screenshot(doc)
            raise


    # 获取元素属性
    def get_elment_attribute(self, locator,attr):
        # 找元素
        ele = self.get_element(locator)
        try:
            return ele.get_attribute(attr)
        except:
            logger.exception("获取元素属性失败！！！")
            # 截图
            # self.save_screenshot(doc)
            raise

    def save_screenshot(self, name):
        # 生成年月日时分秒时间
        contexts = self.driver.contexts
        self.driver.switch_to.context(contexts[0])
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 图片名称：模块名_页面名称_操作名称_时间.png
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        OUTPUTS_DIR = os.path.join(BASE_PATH, "Outputs", "screenshots")
        file_name = OUTPUTS_DIR + "\\{}_{}.png".format(name, picture_time)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, name, allure.attachment_type.PNG)
        logger.info("demo截图文件保存在：{}".format(file_name))

    # def save_screenshot1(self, img_doc):
    #     '''
    #     页面截屏保存截图
    #     :param img_doc: 截图说明
    #     :return:
    #     '''
    #     BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    #     OUTPUTS_DIR =os.path.join(BASE_PATH, "Outputs","screenshots")
    #     file_name = OUTPUTS_DIR + "\\{}_{}.png".format(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())), img_doc)
    #     print(file_name)
    #     self.driver.save_screenshot(file_name)
    #     # with open(file_name, mode='rb') as f:
    #     #     file = f.read()
    #     # allure.attach(file, img_doc, allure.attachment_type.PNG)
    #     logger.info("页面截图文件保存在：{}".format(file_name))

    def switch_scenes(self):
        # 获取所有的环境
        contexts = self.driver.contexts
        # print(contexts)
        # 切换到webview
        # driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.crazycube.sdk.demo"})
        self.driver.switch_to.context(contexts[1])
        # 获取当前的环境，看是否切换成功
        # now = self.driver.current_context

    # 连接数据库
    def connect_database_select(self,database,table,num):
        connect = pymysql.Connect(
            host='8.210.102.39',
            port=31007,
            user='root',
            passwd='CrazyCube!@#',
            db=database,  # 数据库名称
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)  # sql查询结果返回类型：DictCursor 为字典类型， 没有指定为 数组
        cursor = connect.cursor()
        try:
            sql = "select Value from {0} where StorageData ='{1}'  ORDER BY CreatedAtUtc DESC LIMIT 1 ".format(table,num)
            cursor.execute(sql)
            customers = cursor.fetchall()
            for customer in customers:
                logger.info("连接{0}库中{1}表成功，获取{2}验证码：{3}".format(database,table,num,customer["Value"]))

        except Exception as e:  # 捕捉异常，并打印
            traceback.print_exc()
            # 关闭数据库连接
        cursor.close()
        connect.close()

        return customer["Value"]

    def connect_database_update(self, num01, num02):
        connect = pymysql.Connect(
            host='8.210.102.39',
            port=31007,
            user='root',
            passwd='CrazyCube!@#',
            db='CubeAgePlatform',  # 数据库名称
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)  # sql查询结果返回类型：DictCursor 为字典类型， 没有指定为 数组
        cursor = connect.cursor()
        try:
            cursor.execute(num01)
            cursor.execute(num02)
            connect.commit()  # 统一提交
            logger.info("CubeAgePlatform数据库进行update操作【执行成功】")
        except Exception as e:  # 捕捉异常，并打印
            traceback.print_exc()
            # 关闭数据库连接
        cursor.close()
        connect.close()

    def connect_database_updateid(self,types,num):
        connect = pymysql.Connect(
            host='8.210.102.39',
            port=31007,
            user='root',
            passwd='CrazyCube!@#',
            db='CubeAgePlatform',  # 数据库名称
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)  # sql查询结果返回类型：DictCursor 为字典类型， 没有指定为 数组
        cursor = connect.cursor()
        try:
            sql = "UPDATE User SET {0}='{1}' WHERE CreatedAtUtc=(select max_time from(SELECT MAX(CreatedAtUtc) as max_time  FROM User)as a)".format(types,num)
            cursor.execute(sql)
            connect.commit()  # 统一提交
            logger.info("CubeAgePlatform数据库进行updateid操作【执行成功】")

        except Exception as e:  # 捕捉异常，并打印
            traceback.print_exc()
        # 关闭数据库连接
        cursor.close()
        connect.close()

    # 生成随机验证码
    def generate_verification_code(self):
        capta = ''
        words = ''.join((string.ascii_lowercase, string.digits))  ##生成6位小写字母和数字串随机组合
        for i in range(6):
            capta += random.choice(words)  ##随机选择一个字母或数字
        return capta




