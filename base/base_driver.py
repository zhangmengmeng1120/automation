# encoding:utf-8
from appium import webdriver
from util.server import Server
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class BaseDriver(object):

    def __new__(cls, *args, **kwargs):
        server = Server()
        # ports = server.appium_port_list
        # server.start1()
        type = 'android'

        if not hasattr(cls,'_instance'):
            orig = super(BaseDriver, cls)
            if type == 'android':
                devices = server.android_device_list
                desired_caps = {
                    'platformName': 'Android',
                    'platformVersion': '8.1.0',
                    'deviceName': devices[0],
                    'appPackage': 'com.nexttao.shopforce.enterprise',
                    'appActivity': 'com.nexttao.shopforce.fragment.SplashActivity',
                    'unicodeKeyboard': 'True',
                    'resetKeyboard': 'True',
                    'noReset': 'True',
                    'newCommandTimeout':60,
                    'automationName':'uiautomator2'
                }
            else:
                devices = server.ios_device_list
                desired_caps = {
                    "bundleId": "com.nexttao.shopforcetest",
                    "platformName": "iOS",
                    "automationName": "XCUITest",
                    "platformVersion": "12.1",
                    "deviceName": "小杨便利店",
                    "noReset": True,
                    "udid": devices[0],
                    "showXcodeLog": True,
                    'unicodeKeyboard': 'True',
                }
            cls._instance = orig.__new__(cls)
            info = 'http://127.0.0.1:4723/wd/hub'
            cls._instance.driver = webdriver.Remote(info, desired_caps)
        return cls._instance

class DriverClient(BaseDriver):
    def get_dirver(self):
        return self.driver


def GetPageSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def swip_info(driver,info):
    page_size = GetPageSize(driver)
    message = info.split(',')
    sx = page_size[0] * float(message[1])
    sy = page_size[1] * float(message[2])
    ex = page_size[0] * float(message[3])
    ey = page_size[1] * float(message[4])
    for i in range(int(message[0])):
        driver.swipe(sx, sy, ex, ey, '500')
if __name__ == '__main__':
    driver = DriverClient().get_dirver()
    from business import login_action
    login_in = login_action.Login(driver,'android')
    login_in.login_success()
    driver.find_element_by_id('menu_btn_layout').click()
    info = "1,0.1,0.8,0.1,0.25"
    swip_info(driver, info)
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'补货订单')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'补货申请')]").click()
    time.sleep(3)
    contest = driver.contexts
    driver.switch_to.context(contest[1])
    ele = driver.find_element_by_css_selector('div[class$="empty"]')
    print ele
    # driver.find_element_by_id('details_text').click()
    # time.sleep(3)
    # contest = driver.contexts
    # driver.switch_to.context(contest[1])
    # time.sleep(5)
    # element = driver.find_element_by_css_selector('div#searchIcon>img')
    #
    # ActionChains(driver).move_to_element(element).click(element).perform()
    # # js = "document.getElementsByName(\"input-item\").style.display='block';"
    # # # 调用js脚本
    # # driver.execute_script(js)
    # time.sleep(3)
    # driver.find_element_by_class_name("input-item").send_keys("1906001")





    # products = 'S007A499'
    # keycode = {
    #     '0': 7,
    #     '1': 8,
    #     '2': 9,
    #     '3': 10,
    #     '4': 11,
    #     '5': 12,
    #     '6': 13,
    #     '7': 14,
    #     '8': 15,
    #     '9': 16,
    #     'A': 29,
    #     'S': 47
    # }
    # for num in products:
    #     if keycode[num]<=20:
    #         driver.press_keycode(keycode[num])
    #     else:
    #         driver.press_keycode(keycode[num], 64, 59)
    # driver.find_element_by_id('com.nexttao.shopforce.enterprise:id/keypad_search_btn').click()
    # time.sleep(8)
    # contest = driver.contexts
    # driver.switch_to.context(contest[1])
    # from selenium.webdriver.common.by import By
    # sku_infos = driver.find_elements(By.CLASS_NAME,'sku-group')
    # # sku_infos = driver.find_elements_by_class_name('sku-group')
    # color = sku_infos[0].find_elements_by_class_name('label-item')
    # size = sku_infos[1].find_elements_by_class_name('label-item')
    # color[0].click()
    # size[0].click()
    # bottoms = driver.find_element_by_xpath("//div[@class='bottom_kaidan']/div[2]").click()
    # time.sleep(5)
    # print driver.current_context
    # contest = driver.contexts
    # driver.switch_to.context(contest[0])
    # time.sleep(8)
    # print driver.current_context
    # driver.find_element_by_id('com.nexttao.shopforce.enterprise:id/search_product').click()
    # member_mobile = '13429849667'
    # for num in member_mobile:
    #     print 'hahhah'
    #     if keycode[num]<=20:
    #         driver.press_keycode(keycode[num])
    #     else:
    #         driver.press_keycode(keycode[num], 64, 59)
    #
    # driver.find_element_by_id('com.nexttao.shopforce.enterprise:id/keypad_search_btn').click()
    # time.sleep(5)
    # def android_driver(self):
    #     '''
    #     deviceName
    #     port
    #     :return:
    #     '''
    #     desired_caps = {
    #         'platformName': 'Android',
    #         'platformVersion': '4.4.2',
    #         'deviceName': 'E9OKBC127299',
    #         'appPackage': 'com.nexttao.shopforce.test',
    #         'appActivity': 'com.nexttao.shopforce.fragment.SplashActivity',
    #         'unicodeKeyboard': 'True',
    #         'resetKeyboard': 'True',
    #         'noReset': 'True',
    #     }
    #     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    #     return driver
    #
    # def ios_driver(self):
    #     pass
    #
    # def web_driver(self):
    #     pass
