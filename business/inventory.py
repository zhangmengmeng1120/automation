# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class Inventory:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',7)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def inventory_01(self):
        action_type = 'inventory_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inventory_02(self):
        action_type = 'inventory_02'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def inventory_03(self):
        action_type = 'inventory_03'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inventory_04(self):
        action_type = 'inventory_04'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inventory_05(self):
        action_type = 'inventory_05'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inventory_06(self):
        action_type = 'inventory_06'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inventory_07(self):
        action_type = 'inventory_07'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inventory_08(self):
        action_type = 'inventory_08'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inventory_09(self):
        action_type = 'inventory_09'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def inven_cases(self):
        infos = ['inventory_01','inventory_02','inventory_03','inventory_04','inventory_05','inventory_06','inventory_07','inventory_08','inventory_09']
        for i in infos:
            action_type = i
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
