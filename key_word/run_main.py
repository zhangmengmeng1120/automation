#coding:utf-8
from get_data import GetData
from action_methond import ActionMethod
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
from selenium.webdriver.common.by import By


import time

class RunMain:
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver()
        self.get_by_local = GetByLocal()
        self.action_method = ActionMethod(self.driver)
    def run_method(self):
        data = GetData()
        lines = data.get_case_line()
        for i in range(1,lines):
            handle_step = data.get_handle_step(i)
            element_key = data.get_element_key(i)
            handle_value = data.get_hadle_value(i)
            expect_element = data.get_expect_element_key(i)
            excute_method = getattr(login_action_method, handle_step)
            element_value = self.get_element(element_key)
            element_list = element_value.split(',')
            element_value_tu = self.tuple_make(element_list[0], element_list[1])
            if handle_value!=None:
                excute_method(element_key,handle_value,'android')
            else:
                excute_method(element_key,'android')
        time.sleep(10)

    def get_element(self,*args):
        element_location = self.get_by_local.get_element(key=args[0])
        return element_location

    def tuple_make(self,*args):
        element_value_tu = ()
        if args[0] == 'By.ID':
            element_value_tu = (By.ID,args[1])
        elif args[0] == 'By.XPATH':
            element_value_tu = (By.XPATH, args[1])
        elif args[0] == 'By.CLASS_NAME':
            element_value_tu = (By.CLASS_NAME, args[1])
        return element_value_tu

if __name__ == '__main__':
    run = RunMain()
    run.run_method()