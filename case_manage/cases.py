# encoding:utf-8
import unittest
from business import login_action
from business import shopping
from business import scrap
from business import transferout
from business import delivery_refund
from business import delivery_receive
from base  import base_driver
import time

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = base_driver.DriverClient().get_dirver()
        self.type = 'android'

    @classmethod
    def tearDownClass(self):
        pass

    def go_login(self):
        time.sleep(20)
        login_act = login_action.Login(self.driver,self.type)
        login_act.login_success()

    '''
    购物车模块
    '''
    def shopping_all(self):
        all_cases = shopping.ShoppingCard(self.driver, self.type)
        all_cases.shopping_cases()

    def shop_01(self):
        shoping_case_01 = shopping.ShoppingCard(self.driver,self.type)
        shoping_case_01.shopping_01()

    def shop_03(self):
        shoping_case_03 = shopping.ShoppingCard(self.driver,self.type)
        shoping_case_03.shopping_03()

    def shop_04(self):
        shoping_case_04 = shopping.ShoppingCard(self.driver,self.type)
        shoping_case_04.shopping_04()

    def shop_05(self):
        shoping_case_05 = shopping.ShoppingCard(self.driver,self.type)
        shoping_case_05.shopping_05()

    def shop_06(self):
        shoping_case_06 = shopping.ShoppingCard(self.driver,self.type)
        shoping_case_06.shopping_06()

    def shop_07(self):
        shoping_case_07 = shopping.ShoppingCard(self.driver,self.type)
        shoping_case_07.shopping_07()


    '''
    配货退货模块
    '''
    def delivery_refund_all(self):
        all_cases = delivery_refund.DeliveryRefund(self.driver, self.type)
        all_cases.deliveryRF_cases()

    def delivery_refund_01(self):
        deliveryRf_case_01 = delivery_refund.DeliveryRefund(self.driver,self.type)
        deliveryRf_case_01.deliveryRF_01()

    def delivery_refund_02(self):
        deliveryRf_case_02 = delivery_refund.DeliveryRefund(self.driver,self.type)
        deliveryRf_case_02.deliveryRF_02()

    def delivery_refund_03(self):
        deliveryRf_case_03 = delivery_refund.DeliveryRefund(self.driver,self.type)
        deliveryRf_case_03.deliveryRF_03()

    def delivery_refund_04(self):
        deliveryRf_case_04 = delivery_refund.DeliveryRefund(self.driver,self.type)
        deliveryRf_case_04.deliveryRF_04()

    def delivery_refund_05(self):
        deliveryRf_case_05 = delivery_refund.DeliveryRefund(self.driver,self.type)
        deliveryRf_case_05.deliveryRF_05()

    def delivery_refund_06(self):
        deliveryRf_case_06 = delivery_refund.DeliveryRefund(self.driver,self.type)
        deliveryRf_case_06.deliveryRF_06()

    '''
        配货收货模块
        '''

    def delivery_receive_all(self):
        all_cases = delivery_receive.DeliveryReceive(self.driver, self.type)
        all_cases.deliveryRE_cases()

    def delivery_receive_01(self):
        deliveryRe_case_01 = delivery_receive.DeliveryReceive(self.driver, self.type)
        deliveryRe_case_01.deliveryRE_01()

    def delivery_receive_02(self):
        deliveryRe_case_02 = delivery_receive.DeliveryReceive(self.driver, self.type)
        deliveryRe_case_02.deliveryRE_02()

    def delivery_receive_03(self):
        deliveryRe_case_03 = delivery_receive.DeliveryReceive(self.driver, self.type)
        deliveryRe_case_03.deliveryRE_03()

    def delivery_receive_04(self):
        deliveryRe_case_04 = delivery_receive.DeliveryReceive(self.driver, self.type)
        deliveryRe_case_04.deliveryRE_04()

    def delivery_receive_05(self):
        deliveryRe_case_05 = delivery_receive.DeliveryReceive(self.driver, self.type)
        deliveryRe_case_05.deliveryRE_05()

    def delivery_receive_06(self):
        deliveryRe_case_06 = delivery_receive.DeliveryReceive(self.driver, self.type)
        deliveryRe_case_06.deliveryRE_06()

    '''
    调拨出库模块
    '''
    def transferout_all(self):
        all_cases = transferout.TransferOut(self.driver, self.type)
        all_cases.transferout_cases()

    def tranout_01(self):
        transferout_case_01 = transferout.TransferOut(self.driver,self.type)
        transferout_case_01.transferout_01()

    def tranout_02(self):
        transferout_case_02 = transferout.TransferOut(self.driver,self.type)
        transferout_case_02.transferout_02()

    def tranout_03(self):
        transferout_case_03 = transferout.TransferOut(self.driver,self.type)
        transferout_case_03.transferout_03()

    def tranout_04(self):
        transferout_case_04 = transferout.TransferOut(self.driver,self.type)
        transferout_case_04.transferout_04()

    def tranout_05(self):
        transferout_case_05 = transferout.TransferOut(self.driver,self.type)
        transferout_case_05.transferout_05()

    def tranout_06(self):
        transferout_case_06 = transferout.TransferOut(self.driver,self.type)
        transferout_case_06.transferout_06()

    '''
    损益单模块
    '''
    def scrap_01(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_01()



