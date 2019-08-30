# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class TransferIn:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',8)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def transferin_01(self):
        action_type = 'transferin_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def transferin_02(self):

        action_type = 'transferin_02'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def transferin_04(self):

        action_type = 'transferin_04'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def transferin_05(self):
        action_type = 'transferin_05'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def transferin_06(self):
        action_type = 'transferin_06'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def transferin_cases(self):
        infos = ['transferin_01','transferin_02','transferin_04','transferin_05','transferin_06']
        for i in infos:
            action_type = i
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
