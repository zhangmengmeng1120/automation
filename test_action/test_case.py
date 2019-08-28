# encoding:utf-8
import sys
sys.path.append('../')
import unittest
from case_manage.cases import TestCase
import time
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCase("go_login"))
    '''
    开单销售模块
    '''
    # suite.addTest(TestCase("shop_03"))
    # suite.addTest(TestCase("shop_04"))
    # suite.addTest(TestCase("shop_05"))
    # suite.addTest(TestCase("shop_06"))
    # suite.addTest(TestCase("shop_07"))

    '''
    调拨出库单模块
    '''
    # suite.addTest(TestCase("tranout_01"))
    # suite.addTest(TestCase("tranout_02"))
    # suite.addTest(TestCase("tranout_03"))
    # suite.addTest(TestCase("tranout_04"))
    # suite.addTest(TestCase("tranout_05"))
    # suite.addTest(TestCase("tranout_06"))

    '''
    配货退货模块
    '''
    # suite.addTest(TestCase("delivery_refund_01"))
    # suite.addTest(TestCase("delivery_refund_02"))
    # suite.addTest(TestCase("delivery_refund_03"))
    # suite.addTest(TestCase("delivery_refund_04"))
    # suite.addTest(TestCase("delivery_refund_05"))
    # suite.addTest(TestCase("delivery_refund_06"))

    '''
    配货收货模块
    '''
    # suite.addTest(TestCase("delivery_receive_01"))
    suite.addTest(TestCase("delivery_receive_02"))
    # suite.addTest(TestCase("delivery_receive_03"))
    # suite.addTest(TestCase("delivery_receive_04"))
    # suite.addTest(TestCase("delivery_receive_05"))
    # suite.addTest(TestCase("delivery_receive_06"))

    '''
    损益单模块
    '''
    # suite.addTest(TestCase("scrap_01"))
    report_dir = '../report'
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReportCN(stream=f, title='测试报告', description='Android ShopForce自动化测试')
        runner.run(suite)
    f.close()


