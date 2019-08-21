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
        self.action_method.run_method(self.line_infos['shopping_01'],self.type,self.driver)

    def shopping_03(self):

        self.action_method.run_method(self.line_infos['shopping_03'],self.type,self.driver)


    def shopping_04(self):

        self.action_method.run_method(self.line_infos['shopping_04'],self.type,self.driver)

    def shopping_05(self):

        self.action_method.run_method(self.line_infos['shopping_05'],self.type,self.driver)

    def shopping_06(self):
        action_type = self.action_method.run_method(self.line_infos['shopping_06'],self.type,self.driver)
        self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def shopping_07(self):
        action_type = self.action_method.run_method(self.line_infos['shopping_07'],self.type,self.driver)
        self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def shopping_cases(self):
        infos = ['shopping_01','shopping_02','shopping_03','shopping_04','shopping_05','shopping_06','shopping_07']
        for i in infos:
            print i
            action_type = self.action_method.run_method(self.line_infos[i], self.type, self.driver)
            if action_type!=None:
                self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
