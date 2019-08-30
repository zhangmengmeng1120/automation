# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class Scrap:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',13)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def scraping_01(self):
        action_type = 'scrap_01'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def scraping_02(self):
        action_type = 'scrap_02'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def scraping_03(self):
        action_type = 'scrap_03'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def scraping_04(self):
        action_type = 'scrap_04'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def scraping_05(self):
        action_type = 'scrap_05'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def scraping_06(self):
        action_type = 'scrap_06'
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def scrap_cases(self):
        infos = ['scrap_01','scrap_02','scrap_03','scrap_04','scrap_05','scrap_06']
        for i in infos:
            action_type = i
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)