# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class Report:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',6)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def report_01(self):
        action_type = 'report_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_02(self):
        action_type = 'report_02'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def report_03(self):
        action_type = 'report_03'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_04(self):
        action_type = 'report_04'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_05(self):
        action_type = 'report_05'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_06(self):
        action_type = 'report_06'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_07(self):
        action_type = 'report_07'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_08(self):
        action_type = 'report_08'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_09(self):
        action_type = 'report_09'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_10(self):
        action_type = 'report_10'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_11(self):
        action_type = 'report_11'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_12(self):
        action_type = 'report_12'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_13(self):
        action_type = 'report_13'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_14(self):
        action_type = 'report_14'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_15(self):
        action_type = 'report_15'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def report_cases(self):
        infos = ['report_01','report_02','report_03','report_04','report_05','report_06','report_07','report_08','report_09','report_10','report_11','report_12','report_13','report_14','report_15']
        for i in infos:
            action_type = i
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
