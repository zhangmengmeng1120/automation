#coding:utf-8
from base.base_function import BaseFunction
import time
import random
import logging
from selenium.webdriver import ActionChains

_logger = logging.getLogger(__name__)

class ActionMethod(BaseFunction):

    def __init__(self,*args):
        self.driver = args[0]
        BaseFunction.__init__(self,self.driver)


    def input(self,*args):
        '''
        给指定元素输入参数
        :param element: 元素
        :param value: 输入参数
        :param type: iOS、Android、browser
        :return:
        '''
        self.input_element(args[0],args[1])
        # elif args[2]=='ios':
        #     self.input_by_acc(args[0],args[1])
        # else:
        #     _logger.info('请传入正确的设备类型')

    def on_click(self,*args):
        '''
        点击元素的操作
        :param element: 元素
        :param type: iOS、Android、browser
        :return:
        '''
        if 'MobileBy' not in args[0][0]:
            self.click_element(args[0])
        else:
            self.click_acc(args[0][1])



    def ex_find_element(self,*args):
        '''
        查找元素
        :param element: 元素
        :param type: iOS、Android、browser
        :return:
        '''
        return self.find_element(args[0])

    def press_keycode(self,*args):
        '''
        软键盘输入
        :param element: 元素
        :param type: iOS、Android、browser
        :return:
        '''

        # self.on_click(args[0],args[2])
        if args[2] == 'android':
            self.find_element(args[0]).clear()
            self.find_element(args[0]).click()
            keycode = {
                '0': 7,
                '1': 8,
                '2': 9,
                '3': 10,
                '4': 11,
                '5': 12,
                '6': 13,
                '7': 14,
                '8': 15,
                '9': 16,
                'A':29,
                'S':47
            }
            for num in args[1]:
                self.basic_press_keycode(keycode[num],args[0])
        else:
            self.find_element_by_accessibility_id(args[0]).clear()
            self.find_element_by_accessibility_id(args[0]).click()
            for num in args[1]:
                self.click_acc(num)
    def switch_h5(self, *args):
        webview_info = None
        if args[0] == 0:
            webview_info = 'NATIVE_APP'
        elif args[0] == 1 or args[0] == 4:
            webview_info = 'WEBVIEW_com.nexttao.shopforce.enterprise'
        self.switch_to_h5(webview_info)
        time.sleep(5)


    def choose_color_size(self,*args):
        sku_infos = self.driver.find_elements_by_class_name('sku-group')
        color = sku_infos[0].find_elements_by_class_name('label-item')
        size = sku_infos[1].find_elements_by_class_name('label-item')
        random_color = random.randint(0,len(color)-1)
        random_size = random.randint(0,len(size)-1)
        color[random_color].click()
        size[random_size].click()

    def verification(self,*args):
        if args[1] == 'android':
            assert self.find_element(args[0]),'False'

        else:
            assert self.find_element_by_accessibility_id(args[0]),'False'

    def wait_sec(self,*args):
        time.sleep(args[0])

    def GetPageSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swip_info(self,info):
        page_size = self.GetPageSize()
        message = info.split(',')
        sx = page_size[0] * float(message[1])
        sy = page_size[1] * float(message[2])
        ex = page_size[0] * float(message[3])
        ey = page_size[1] * float(message[4])
        for i in range(int(message[0])):
            self.driver.swipe(sx, sy, ex, ey, '500')

    def judge(self,*args):
        response = None
        if args[2]=='android':
            response = self.find_element(args[0])
        elif args[2]=='ios':
            response = self.find_element_by_accessibility_id(args[0])
        else:
            _logger.info('请传入正确的设备类型')
        action_info = eval(args[1])
        action_key = '1'
        '''1表示继续，0表示去创建相应的订单'''
        if response == False:
            action_key = '0'
        return action_info[action_key]

    def location_click(self,*args):
        local_info = args[1].split(',')
        print '########## %s ' %local_info
        handle = self.driver.current_window_handle
        print '111111 %s' % handle
        all_handle = self.driver.window_handles
        print '333333 %s' % all_handle
        page_size = self.GetPageSize()
        print page_size
        # self.switch_h5(0)
        page_size = self.GetPageSize()
        print page_size
        locals = [(float(local_info[0]),float(local_info[1]))]
        click_locals = [(page_size[0] * x, page_size[1] * y) for (x, y) in locals]
        print click_locals
        self.driver.tap([(70,180)], 500)
        # self.switch_h5(1)

    def cascade_find(self,*args):
        element = self.find_element(args[0])
        ActionChains(self.driver).move_to_element(element).click(element).perform()
