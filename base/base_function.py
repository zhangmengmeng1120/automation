#!/usr/bin/python
# encoding:utf-8
import time
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.switch_to import MobileCommand
from appium.webdriver.common.mobileby import MobileBy


class BaseFunction(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))
        except:
            return False

    def ex_find_elements(self, loc,timeout=10):
        '''封装一组元素定位方法'''
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_elements(*loc).is_displayed())
            return WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(*loc))
        except:
            return False

    def click_element(self, loc, timeout=1):
        self.find_element(loc).click()
        time.sleep(timeout)

    def input_element(self, loc, text):
        self.inp = self.find_element(loc)
        self.inp.clear()
        self.inp.send_keys(text)

    #    软键盘输入
    def basic_press_keycode(self,*args):
        '''

        :param args: android是通过press_keycode软键盘输入，ios是通过click输入的
        :return: args[1] type:ios/android
        '''
        # self.find_element(args[1]).click()
        if args[0]<20:
            self.driver.press_keycode(args[0])
        else:
            self.driver.press_keycode(args[0],64,59)

    # Native APP 与H5的切换
    def switch_to_h5(self, context_name):
        """
        Sets the context for the current session.

        :Args:
         - context_name: The name of the context to switch to.

        :Usage:
            driver.switch_to.context('WEBVIEW_1')
        """
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': context_name})


    def find_element_by_accessibility_id(self, accessibility_id,timeout=10):
        """Finds an element by accessibility id.

        :Args:
         - accessibility_id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_element_by_accessibility_id()
        """
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=accessibility_id).is_displayed())
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*accessibility_id))

    def click_acc(self,accessibility_id):
        self.find_element_by_accessibility_id(accessibility_id).click()
        time.sleep(1)

    def input_by_acc(self,accessibility_id,text):
        self.inp = self.find_element_by_accessibility_id(accessibility_id)
        self.inp.clear()
        self.inp.send_keys(text)