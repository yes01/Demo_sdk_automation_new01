from appium import  webdriver
from PageObjects.loginsafety_page import LoginsafetyPage
from PageObjects.logininfo_page import LogininfoPage
from PageObjects.binding_page import Binding
from PageObjects.password_page import Password
from Common.basepage import logger
from py.xml import html
import pytest
import allure


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "Demo_sdk(UI)自动化测试"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 研发部平台组")])
    prefix.extend([html.p("测试人员: 李翔")])

driver = None
@pytest.fixture(scope="function")
@allure.step("启动demo")
def access_demo(request):
    global driver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = 'com.crazycube.hkmahjongtycoon.app'
    desired_caps['appActivity'] = 'com.crazycube.hkmahjongtycoon.app.MainActivity'
    # desired_caps['noReset'] = 'True'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    logger.info('-----开始执行当前用例-----')

    def final():
        logger.info('-----当前用例执行完毕-----')
        driver.quit()

    request.addfinalizer(final)
    return driver
    # lg = LoginPage(driver)
    # yield (driver,lg)
    # driver.quit()


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Description'))
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         # report.description = str(item.function.doc)
#
# def _capture_screenshot():
#     '''
#     截图保存为base64，展示到html中
#     :return:
#     '''
#     return driver.get_screenshot_as_base64()


@pytest.fixture(scope="function")
def firsr(access_demo):
    ng = LoginsafetyPage(access_demo)
    ng.is_authorize_login_safety()

@pytest.fixture(scope="function")
def second(access_demo):
    ng = LogininfoPage(access_demo)
    ng.is_authorize_login_info()


@pytest.fixture(scope="function")
def bind_email(access_demo):
    lg = Binding(access_demo)
    lg.bind_email_success()


@pytest.fixture(scope="function")
def bind_phone(access_demo):
    lg = Binding(access_demo)
    lg.bind_phone_success()


@pytest.fixture(scope="function")
def set_password(access_demo):
    lg = Password(access_demo)
    lg.set_password()