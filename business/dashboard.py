# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class Dashbosrd:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',4)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def dashboard_01(self):
        action_type = 'dashboard_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)

    def dashboard_02(self):
        action_type = 'dashboard_02'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)

    def dashboard_03(self):
        action_type = 'dashboard_03'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type],self.type,self.driver)

    def dashboard_cases(self):
        infos = ['dashboard_01','dashboard_02','dashboard_03']
        for i in infos:
            action_type = i
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

