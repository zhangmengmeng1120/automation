# encoding:utf-8
from util.opera_case_to_json import OperaCaseToJson
from currency_action import CurrencyAction


class DeliveryReceive:

    def __init__(self,*args):
        self.driver = args[0]
        self.type=args[1]
        self.case = OperaCaseToJson(self.type,'../config/case.xls',9)
        self.line_infos = self.case.opera_case()
        self.action_method = CurrencyAction()


    def deliveryRE_01(self):
        action_type = self.action_method.run_method(self.line_infos['deliveryRecv_01'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def deliveryRE_02(self):

        action_type = self.action_method.run_method(self.line_infos['deliveryRecv_02'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def deliveryRE_03(self):

        action_type = self.action_method.run_method(self.line_infos['deliveryRecv_03'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def deliveryRE_04(self):

        action_type = self.action_method.run_method(self.line_infos['deliveryRecv_04'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def deliveryRE_05(self):
        action_type = self.action_method.run_method(self.line_infos['deliveryRecv_05'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)


    def deliveryRE_06(self):
        action_type = self.action_method.run_method(self.line_infos['deliveryRecv_06'],self.type,self.driver)
        while action_type != None:
            action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)

    def deliveryRE_cases(self):
        infos = ['deliveryRecv_01','deliveryRecv_02','deliveryRecv_03','deliveryRecv_04','deliveryRecv_05','deliveryRecv_06']
        for i in infos:
            action_type = self.action_method.run_method(self.line_infos[i], self.type, self.driver)
            while action_type != None:
                action_type = self.action_method.run_method(self.line_infos[action_type], self.type, self.driver)
