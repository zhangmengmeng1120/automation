# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class ShoppingCard:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',1)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def shopping_01(self):
        action_type = 'shopping_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)

    def shopping_02(self):
        action_type = 'shopping_02'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)

    def shopping_03(self):
        action_type = 'shopping_03'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def shopping_04(self):
        action_type = 'shopping_04'
        while action_type != None:
            self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)

    def shopping_05(self):
        action_type = 'shopping_05'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)

    def shopping_06(self):
        action_type = 'shopping_06'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def shopping_07(self):
        action_type = 'shopping_07'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def shopping_cases(self):
        infos = ['shopping_01','shopping_02','shopping_03','shopping_04','shopping_05','shopping_06','shopping_07']
        for i in infos:
            print i
            action_type = i
            if action_type != None:
                self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
