# encoding:utf-8
import unittest
from business import login_action
from business import shopping
from business import scrap
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

    def scrap_01(self):
        scrap_case_01 = scrap.Scrap(self.driver,self.type)
        scrap_case_01.scraping_01()



