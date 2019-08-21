# encoding:utf-8
import unittest
from case_manage.cases import TestCase
import time
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCase("go_login"))
    suite.addTest(TestCase("shopping_all"))
    # suite.addTest(TestCase("shop_03"))
    # suite.addTest(TestCase("shop_04"))
    # suite.addTest(TestCase("shop_05"))
    # suite.addTest(TestCase("shop_06"))
    # suite.addTest(TestCase("shop_07"))
    # suite.addTest(TestCase("scrap_01"))
    report_dir = '../report'
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReportCN(stream=f, title='测试报告', description='Android ShopForce自动化测试')
        runner.run(suite)
    f.close()


