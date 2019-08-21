# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction
import time


class Login:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',0)
        self.line_infos = self.case.opera_case()


    def login_success(self):
        action_method = CurrencyAction()
        action_method.run_method(self.line_infos['login_01'],self.type,self.driver)
