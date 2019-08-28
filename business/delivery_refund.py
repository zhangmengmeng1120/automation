# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class DeliveryRefund:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',11)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def deliveryRF_01(self):
        action_type = self.action_method.run_method(self.line_infos['deliveryRF_01'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def deliveryRF_02(self):

        action_type = self.action_method.run_method(self.line_infos['deliveryRF_02'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def deliveryRF_03(self):

        action_type = self.action_method.run_method(self.line_infos['deliveryRF_03'],self.type,self.driver)
        while action_type != None:
            print action_type
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def deliveryRF_04(self):

        action_type = self.action_method.run_method(self.line_infos['deliveryRF_04'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def deliveryRF_05(self):
        action_type = self.action_method.run_method(self.line_infos['deliveryRF_05'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def deliveryRF_06(self):
        action_type = self.action_method.run_method(self.line_infos['deliveryRF_06'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def deliveryRF_cases(self):
        infos = ['deliveryRF_01','deliveryRF_02','deliveryRF_03','deliveryRF_04','deliveryRF_05','deliveryRF_06']
        for i in infos:
            action_type = self.action_method.run_method(self.line_infos[i], self.type, self.driver)
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
