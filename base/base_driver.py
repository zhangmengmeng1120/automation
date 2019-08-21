# encoding:utf-8
from appium import webdriver
from util.server import Server
import time

class BaseDriver(object):

    def __new__(cls, *args, **kwargs):
        server = Server()
        devices = server.device_list
        # ports = server.appium_port_list
        # server.start1()
        time.sleep(10)
        if not hasattr(cls,'_instance'):
            orig = super(BaseDriver,cls)
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
            cls._instance = orig.__new__(cls)
            # info = 'http://127.0.0.1:%s/wd/hub'%int(ports[0])
            info = 'http://127.0.0.1:4723/wd/hub'
            cls._instance.driver = webdriver.Remote(info, desired_caps)
        return cls._instance

class DriverClient(BaseDriver):
    def get_dirver(self):
        return self.driver

if __name__ == '__main__':
    driver = DriverClient().get_dirver()
    from business.login_action import Login
    login = Login(driver,'android')
    login.login_success()




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
