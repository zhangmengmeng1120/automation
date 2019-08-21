# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class Scrap:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',13)
        self.line_infos = self.case.opera_case()


    def scraping_01(self):
        action_method = CurrencyAction()
        action_method.run_method(self.line_infos['scrap_01'],self.type,self.driver)

