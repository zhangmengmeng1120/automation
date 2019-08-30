# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class Reload:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',12)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def reload_01(self):
        action_type = 'reload_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def reload_02(self):

        action_type = 'reload_02'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def reload_03(self):
        action_type = 'reload_03'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def reload_04(self):

        action_type = 'reload_04'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def reload_05(self):
        action_type = 'reload_05'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def reload_06(self):
        action_type = 'reload_06'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def reload_07(self):
        action_type = 'reload_07'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def reload_08(self):
        action_type = 'reload_08'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def reload_cases(self):
        infos = ['reload_01','reload_02','reload_03','reload_04','reload_05','reload_06','reload_08','reload_07']
        for i in infos:
            action_type = i
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
