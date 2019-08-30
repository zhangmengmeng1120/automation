# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class Bestselling:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',5)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def bestSelling_01(self):
        action_type = 'bestSelling_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)




