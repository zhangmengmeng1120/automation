# encoding:utf-8
import unittest
from business import login_action
from business import shopping
from business import scrap
from business import transferout
from business import delivery_refund
from business import delivery_receive
from business import bestselling
from business import dashboard
from business import transferin
from business import reload
from business import inventory
from  business import report
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
    调拨入库模块
    '''
    def transferin_all(self):
        all_cases = transferin.TransferIn(self.driver, self.type)
        all_cases.transferin_cases()

    def tranin_01(self):
        transferin_case_01 = transferin.TransferIn(self.driver,self.type)
        transferin_case_01.transferin_01()

    def tranin_02(self):
        transferin_case_02 = transferin.TransferIn(self.driver,self.type)
        transferin_case_02.transferin_02()

    def tranin_04(self):
        transferin_case_04 = transferin.TransferIn(self.driver,self.type)
        transferin_case_04.transferin_04()

    def tranin_05(self):
        transferin_case_05 = transferin.TransferIn(self.driver,self.type)
        transferin_case_05.transferin_05()

    def tranin_06(self):
        transferin_case_06 = transferin.TransferIn(self.driver,self.type)
        transferin_case_06.transferin_06()


    '''
    补货申请、审批模块
    '''
    def reload_all(self):
        all_cases = reload.Reload(self.driver, self.type)
        all_cases.reload_cases()

    def shop_reload_01(self):
        reload_case_01 = reload.Reload(self.driver,self.type)
        reload_case_01.reload_01()

    def shop_reload_02(self):
        reload_case_02 = reload.Reload(self.driver,self.type)
        reload_case_02.reload_02()

    def shop_reload_03(self):
        reload_case_03 = reload.Reload(self.driver,self.type)
        reload_case_03.reload_03()

    def shop_reload_04(self):
        reload_case_04 = reload.Reload(self.driver,self.type)
        reload_case_04.reload_04()

    def shop_reload_05(self):
        reload_case_05 = reload.Reload(self.driver,self.type)
        reload_case_05.reload_05()

    def shop_reload_06(self):
        reload_case_06 = reload.Reload(self.driver,self.type)
        reload_case_06.reload_06()

    def shop_reload_07(self):
        reload_case_07 = reload.Reload(self.driver,self.type)
        reload_case_07.reload_07()

    def shop_reload_08(self):
        reload_case_08 = reload.Reload(self.driver,self.type)
        reload_case_08.reload_08()

    '''
    畅销排行模块
    '''

    def best_01(self):
        best_case_01 = bestselling.Bestselling(self.driver, self.type)
        best_case_01.bestSelling_01()


    '''
    数据罗盘模块
    '''
    def dash_all(self):
        all_cases = dashboard.Dashbosrd(self.driver, self.type)
        all_cases.dashboard_cases()

    def dash_01(self):
        dashboard_case_01 = dashboard.Dashbosrd(self.driver, self.type)
        dashboard_case_01.dashboard_01()

    def dash_02(self):
        dashboard_case_02 = dashboard.Dashbosrd(self.driver, self.type)
        dashboard_case_02.dashboard_02()

    def dash_03(self):
        dashboard_case_03 = dashboard.Dashbosrd(self.driver, self.type)
        dashboard_case_03.dashboard_03()

    '''
    损益单模块
    '''
    def scrap_all(self):
        all_cases = scrap.Scrap(self.driver, self.type)
        all_cases.scrap_cases()

    def scrap_01(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_01()

    def scrap_02(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_02()

    def scrap_03(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_03()

    def scrap_04(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_04()

    def scrap_05(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_05()

    def scrap_06(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_06()

    '''
    盘点单模块
    '''
    def inven_all(self):
        inventory_cases = inventory.Inventory(self.driver,self.type)
        inventory_cases.inven_cases()

    def inven_01(self):
        inventory_case_01 = inventory.Inventory(self.driver,self.type)
        inventory_case_01.inventory_01()

    def inven_02(self):
        inventory_case_02 = inventory.Inventory(self.driver,self.type)
        inventory_case_02.inventory_02()

    def inven_03(self):
        inventory_case_03 = inventory.Inventory(self.driver,self.type)
        inventory_case_03.inventory_03()

    def inven_04(self):
        inventory_case_04 = inventory.Inventory(self.driver,self.type)
        inventory_case_04.inventory_04()

    def inven_05(self):
        inventory_case_05 = inventory.Inventory(self.driver,self.type)
        inventory_case_05.inventory_05()

    def inven_06(self):
        inventory_case_06 = inventory.Inventory(self.driver,self.type)
        inventory_case_06.inventory_06()

    def inven_07(self):
        inventory_case_07 = inventory.Inventory(self.driver,self.type)
        inventory_case_07.inventory_07()

    def inven_08(self):
        inventory_case_08 = inventory.Inventory(self.driver,self.type)
        inventory_case_08.inventory_08()

    def inven_09(self):
        inventory_case_09 = inventory.Inventory(self.driver,self.type)
        inventory_case_09.inventory_09()

    '''
    报表模块
    '''
    def report_all(self):
        report_cases = report.Report(self.driver,self.type)
        report_cases.report_cases()

    def repo_01(self):
        repo_case_01 = report.Report(self.driver,self.type)
        repo_case_01.report_01()

    def repo_02(self):
        repo_case_02 = report.Report(self.driver,self.type)
        repo_case_02.report_02()

    def repo_03(self):
        repo_case_03 = report.Report(self.driver,self.type)
        repo_case_03.report_03()

    def repo_04(self):
        repo_case_04 = report.Report(self.driver,self.type)
        repo_case_04.report_04()

    def repo_05(self):
        inventory_case_05 = report.Report(self.driver,self.type)
        inventory_case_05.inventory_05()

    def repo_06(self):
        repo_case_06 = report.Report(self.driver,self.type)
        repo_case_06.report_06()

    def repo_07(self):
        repo_case_07 = report.Report(self.driver,self.type)
        repo_case_07.report_07()

    def repo_08(self):
        repo_case_08 = report.Report(self.driver,self.type)
        repo_case_08.report_08()

    def repo_09(self):
        repo_case_09 = report.Report(self.driver,self.type)
        repo_case_09.report_09()

    def repo_10(self):
        repo_case_10 = report.Report(self.driver,self.type)
        repo_case_10.report_10()

    def repo_11(self):
        repo_case_11 = report.Report(self.driver,self.type)
        repo_case_11.report_11()

    def repo_12(self):
        repo_case_12 = report.Report(self.driver,self.type)
        repo_case_12.report_12()

    def repo_13(self):
        repo_case_13 = report.Report(self.driver,self.type)
        repo_case_13.report_13()

    def repo_14(self):
        repo_case_14 = report.Report(self.driver,self.type)
        repo_case_14.report_14()

    def repo_15(self):
        repo_case_15 = report.Report(self.driver,self.type)
        repo_case_15.report_15()