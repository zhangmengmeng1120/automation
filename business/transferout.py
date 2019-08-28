# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class TransferOut:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',10)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def transferout_01(self):
        action_type = self.action_method.run_method(self.line_infos['transferout_01'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def transferout_02(self):

        action_type = self.action_method.run_method(self.line_infos['transferout_02'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def transferout_03(self):

        action_type = self.action_method.run_method(self.line_infos['transferout_03'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def transferout_04(self):

        action_type = self.action_method.run_method(self.line_infos['transferout_04'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def transferout_05(self):
        action_type = self.action_method.run_method(self.line_infos['transferout_05'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def transferout_06(self):
        action_type = self.action_method.run_method(self.line_infos['transferout_06'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def transferout_cases(self):
        infos = ['transferout_01','transferout_02','transferout_03','transferout_04','transferout_05','transferout_06']
        for i in infos:
            action_type = self.action_method.run_method(self.line_infos[i], self.type, self.driver)
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
