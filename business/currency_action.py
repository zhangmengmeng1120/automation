# encoding:utf-8
from key_word.action_methond import ActionMethod
from selenium.webdriver.common.by import By
from util.get_by_local import GetByLocal
import datetime


class CurrencyAction:
    def run_method(self,line_infos,type,driver):
        self.action_method = ActionMethod(driver)
        action_key = None
        for info in line_infos:
            if info['element_key'] != None:
                element_value = self.get_element(info['element_key'], info['file_path'], info['section'],'com.nexttao.shopforce.enterprise')
                element_list = element_value.split(',,')
                element_value_tu = self.tuple_make(element_list[0], element_list[1])
            excute_method = getattr(self.action_method, info['handle_step'])
            print 'handle_value %s'%info['handle_value']
            if  info['handle_step'] == 'switch_h5' or info['handle_step'] == 'wait_sec':
                excute_method(int(info['handle_value']))
            elif info['handle_step']== 'swip_info':
                excute_method(info['handle_value'])
            elif info['handle_step']== 'judge':
                action_key  = excute_method(element_value_tu, info['handle_value'], type)
            elif info['handle_value'] == 'random_value':
                info['handle_value'] = "%02d" % (datetime.datetime.now().microsecond / 20000)
                excute_method(element_value_tu, info['handle_value'], type)
            elif info['handle_value'] != None:
                excute_method(element_value_tu, info['handle_value'], type)
            else:
                excute_method(element_value_tu, type)

        return action_key



    def get_element(self, *args):
        get_by_local = GetByLocal()
        element_location = get_by_local.get_element(key=args[0],file_path=args[1],section=args[2],package_name=args[3])
        return element_location

    def tuple_make(self, *args):
        element_value_tu = ()
        if args[0] == 'By.ID':
            element_value_tu = (By.ID, args[1])
        elif args[0] == 'By.XPATH':
            element_value_tu = (By.XPATH, args[1])
        elif args[0] == 'By.CLASS_NAME':
            element_value_tu = (By.CLASS_NAME, args[1])
        elif args[0] == 'MobileBy.ACCESSIBILITY_ID':
            element_value_tu = ('MobileBy.ACCESSIBILITY_ID', args[1])
        elif args[0] == 'By.CSS_SELECTOR':
            element_value_tu = (By.CSS_SELECTOR, args[1])
        return element_value_tu
