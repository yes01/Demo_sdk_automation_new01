from selenium.webdriver.common.by import By
import time

class LoginPageLocators:

    # sql查询语句
    sql01 = ("UPDATE User SET Email='' WHERE CreatedAtUtc=(select max_time from(SELECT MAX(CreatedAtUtc) as max_time  FROM User)as a)")
    sql02 = ("UPDATE User SET CountryCode='' ,Phone='' WHERE CreatedAtUtc=(select max_time from(SELECT MAX(CreatedAtUtc) as max_time  FROM User)as a)")
    sql03 = ("UPDATE UserBindAccount SET IsBound='0'  WHERE CreatedAtUtc=(select max_time from(SELECT MAX(CreatedAtUtc) as max_time  FROM UserBindAccount)as a)")
    sql04 = ("select * from Level")

    # 初始化
    initialization_sdk_01 = (By.ID, "com.crazycube.hkmahjongtycoon.app:id/init_sdk")
    initialization_sdk_02 = (By.ID, "com.crazycube.hkmahjongtycoon.app:id/button3")
    # initialization_sdk_03 = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")

    # 登录
    login_sdk = (By.ID, "com.crazycube.hkmahjongtycoon.app:id/login")
    login_success = (By.ID,"com.crazycube.hkmahjongtycoon.app:id/button3")

    # 平台浮标
    x_y_01 = [[(65, 1693)],500]

    # 平台浮标功能页面
    x_y_02 = [[(508,1683)], 500]# 安全页面
    x_y_03 = [[(188, 1683)], 500]  # 信息页面
    x_y_04 = [[(294, 1683)], 500]  # 成就页面
    x_y_05 = [[(400, 296)], 500]  # 游戏页面
    x_y_06 = [[(561, 1111)], 500]  # 继续Facebook登录


    # 信息页面_添加账号登录
    click_switchaccount = (By.XPATH, '//*[@class="jsx-4002802977 UserInfo_New_WV_d1"]')  # 账号切换
    click_addaccount = (By.XPATH, '//*[@class="Btn4WvComp"]')  # 添加账号按钮
    click_define = (By.XPATH, '//*[@class="Btn4WvNewComp_text"]')  # 确定按钮
    set_account = (By.XPATH, '//*[@placeholder="請輸入郵箱/手機號碼"]')  # email、phone输入框
    set_pwd = (By.XPATH, '//*[@placeholder="請輸入密碼"]')  # 密码输入框
    set_captcha = (By.XPATH, '//*[@placeholder="請輸入驗證碼"]')  # 验证码输入框
    click_captcha_login = (By.XPATH, '//*[@class="M4L_WV_d1_sp6" and contains(text(),"驗證碼登錄")]')  # 验证码登录按钮
    click_captcha_send = (By.XPATH, '//*[@class="d1_d2"]')  # 验证码发送按钮
    click_remember_pwd = (By.XPATH, '//*[@id="login_n_wv"]/div/div/div/div[2]/div[1]/div[2]/div[5]/div')  # 记住密码按钮
    click_login = (By.XPATH, '//*[@class="Btn4WvNewComp_text" ]')  # 注册/登录按钮
    click_forget_pwd = (By.XPATH, '//*[@class="M4L_WV_d1_sp6" and contains(text(),"忘記密碼")]')  # 忘记密码按钮
    click_Choose_role = (By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[1]')  # 选择第一个角色

    # 信息页面_修改用户昵称功能
    click_username = [[(730,733)], 500]# 用户昵称页面
    set_username = (By.XPATH, '//*[@id="SetNickName_WV"]/div[2]/div[1]/div/input')
    click_username_submit = (By.XPATH, '//*[contains(text(),"提交") and @class="Btn4WvNewComp_text" ]')

    # 安全信息页面_修改用户id功能
    click_userid = (By.XPATH, '//*[contains(text(),"設置用戶號") and @class="jsx-3199281062" ]')
    set_userid = (By.XPATH, '//*[@class="ipt1"]')
    click_userid_submit = (By.XPATH, '//*[contains(text(),"提交") and @class="Btn4WvNewComp_text" ]')

    # 安全信息页面_修改密码功能
    click_password_set = (By.XPATH, '//*[contains(text(),"設置密碼") and @class="jsx-3199281062"]')  # 进入设置密码界面
    click_password01 = (By.XPATH, '//*[contains(text(),"修改密碼") and @class="jsx-3199281062"]')  # 进入修改密码界面
    click_password02 = (By.XPATH, '//*[contains(text(),"舊密碼修改") and @class="CEPP_WV_d1_d1"]')  # 进入修改旧密码界面
    click_password03 = (By.XPATH, '//*[contains(text(),"郵箱驗證碼修改") and @class="CEPP_WV_d1_d1"]')  # 进入email修改密码界面
    click_password04 = (By.XPATH, '//*[contains(text(),"手機驗證碼修改") and @class="CEPP_WV_d1_d1"]')  # 进入phone修改密码界面
    set_password01 = (By.XPATH, '//*[@id="ChangePassword_WV"]/div[2]/div[1]/div[1]/input')  # 设置密码输入框&旧密码输入框&修改密码账号显示框_email、phone
    set_password02 = (By.XPATH, '//*[@id="ChangePassword_WV"]/div[2]/div[2]/div[1]/input') # 设置密码输入框&新密码输入框&修改密码验证码输入框_email、phone
    set_password03 = (By.XPATH, '//*[@id="ChangePassword_WV"]/div[2]/div[3]/div[1]/input') # 修改旧密码再次确认输入框&修改密码新密码输入框_email、phone
    set_password04 = (By.XPATH, '//*[@placeholder="再次輸入密碼"]')  # &修改密码新密码确认框_email、phone

    # 账号绑定
    click_binding_email = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]')  # 进入绑定邮箱界面
    click_binding_phone = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]')  # 进入绑定电话界面
    click_binding_facebook = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[6]')  # 进入绑定facebook界面
    click_binding_google = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[7]')  # 进入绑定google界面
    set_binding01 = (By.XPATH, '//*[@placeholder="請輸入郵箱"]')  # 邮箱输入框
    set_binding02 = (By.XPATH, '//*[@placeholder="請輸入驗證碼"]')  # 验证码输入框
    set_binding03 = (By.XPATH, '//*[@placeholder="請輸入手機號碼"]')  # 电话输入框
    click_submit = (By.XPATH, '//*[@class="Btn4WvNewComp_text"]')  # 绑定邮箱、电话确认按钮&设置密码、修改密码确认按钮_旧密码、email、phone

    # 登录
    click_account_facebook = (By.XPATH, '//*[@class="M4NL_WV_d0_d2_d1_d5"]/div[1]')  # 点击facebook登录按钮
    click_account_google = (By.XPATH, '//*[@class="M4NL_WV_d0_d2_d1_d5"]/div[3]')  # 点击google登录按钮
    click_login_facebook = (By.XPATH, '//*[@name="login"]')  # facebook登录按钮
    click_compatible_facebook = (By.XPATH, '//*[@class="img img _2sxw"]')  # facebook登录取消保存密码（手机兼容操作）
    click_keeplogin_facebook01 = (By.XPATH, '//*[@id="u_0_5"]')  # facebook继续登录按钮
    click_keeplogin_facebook02 = (By.XPATH, '//*[@id="u_0_1"]')  # facebook继续登录按钮
    click_cancellogin_facebook = (By.XPATH, '//*[@class="_55sr" and contains(text(),"取消")]')  # facebook取消登录按钮
    #//*[@id="platformDialogContent"]/div/div[2]/footer/div/button/span
    set_account_facebook = (By.ID, 'm_login_email')  # facebook账号输入框
    set_password_facebook = (By.XPATH, '//*[@id="m_login_password"]')  # facebook密码输入框
