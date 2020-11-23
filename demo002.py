# coding:utf-8
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
desired_caps = {'platformName': 'Android',
                'deviceName': 'emulator-5554',
                # 'platformVersion': '5.1.1',
                'appPackage': 'com.crazycube.hkmahjongtycoon.app',
                'appActivity': 'com.crazycube.hkmahjongtycoon.app.MainActivity'}
                # 'noReset': "True"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
# 初始化sdk
driver.find_element_by_id("com.crazycube.hkmahjongtycoon.app:id/init_sdk").click()
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.ID, 'com.crazycube.hkmahjongtycoon.app:id/button3')))
driver.find_element_by_id("com.crazycube.hkmahjongtycoon.app:id/button3").click()
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.ID, 'com.crazycube.hkmahjongtycoon.app:id/button3')))
driver.find_element_by_id("com.crazycube.hkmahjongtycoon.app:id/button3").click()
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.ID, 'com.android.permissioncontroller:id/permission_allow_button')))
driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.ID, 'com.crazycube.hkmahjongtycoon.app:id/login')))
# 登录
driver.find_element_by_id("com.crazycube.hkmahjongtycoon.app:id/login").click()
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.ID, 'com.crazycube.hkmahjongtycoon.app:id/button3')))
driver.find_element_by_id("com.crazycube.hkmahjongtycoon.app:id/button3").click()
time.sleep(6)
# 平台浮标
driver.tap([(1054,247)],500)
time.sleep(2)
#安全信息界面
driver.tap([(820,400)],500)
time.sleep(2)
# 切换到图书界面后获取所有的环境
contexts = driver.contexts
print(contexts)

# 切换到webview
# driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.crazycube.sdk.demo"})
driver.switch_to.context(contexts[1])
# 获取当前的环境，看是否切换成功
now = driver.current_context
print(now)
# print(driver.page_source)
# 设置用户号
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[2]/div[6]')))
time.sleep(2)
driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div[6]').click()
time.sleep(5)
contexts = driver.contexts
print(contexts)
windows =driver.window_handles
print(windows)
driver.switch_to.window(windows[-1])
#//*[@id="__next"]/div/div/div[2]/div[2]/div[1]
WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, 'm_login_email')))
print("11111111111111111111")
# driver.find_element_by_xpath('//*[@id="SetUserName_WV"]/div[2]/div[1]/div/input').send_keys('qqq321')
driver.find_element_by_id('m_login_email').send_keys('15574637990')
WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="m_login_password"]')))
driver.find_element_by_xpath('//*[@id="m_login_password"]').send_keys('123456......')
driver.find_element_by_xpath('//*[@name="login"]').click()
# driver.find_element_by_partial_link_text('icon-accountname.png').click()
# driver.find_element_by_id("beecf2d4-e30e-4e33-bcdf-5b8d3c27b46e").click()
time.sleep(3)
driver.quit()
# 切回native
# driver.switch_to.context(contexts[0])

# driver.switch_to.context("NATIVE_APP") # 这样也是可以的

# 获取当前的环境，看是否切换成功
# now = driver.current_context
# print(now)