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
    调拨入库单模块
    '''
    # suite.addTest(TestCase("tranin_01"))
    # suite.addTest(TestCase("tranin_02"))
    # suite.addTest(TestCase("tranin_04"))
    # suite.addTest(TestCase("tranin_05"))
    # suite.addTest(TestCase("tranin_06"))

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
    # suite.addTest(TestCase("delivery_receive_02"))
    # suite.addTest(TestCase("delivery_receive_04"))
    # suite.addTest(TestCase("delivery_receive_05"))
    # suite.addTest(TestCase("delivery_receive_06"))



    '''
    补货申请模块
    '''
    # suite.addTest(TestCase("shop_reload_01"))
    # suite.addTest(TestCase("shop_reload_02"))
    # suite.addTest(TestCase("shop_reload_03"))
    # suite.addTest(TestCase("shop_reload_04"))
    # suite.addTest(TestCase("shop_reload_05"))
    # suite.addTest(TestCase("shop_reload_06"))
    # suite.addTest(TestCase("shop_reload_07"))
    # suite.addTest(TestCase("shop_reload_08"))

    '''
    畅销排行模块
    '''
    # suite.addTest(TestCase("best_01"))


    '''
    数据罗盘模块
    '''
    # suite.addTest(TestCase("dash_01"))
    # suite.addTest(TestCase("dash_02"))
    # suite.addTest(TestCase("dash_03"))

    '''
    损益单模块
    '''
    # suite.addTest(TestCase("scrap_01"))
    # suite.addTest(TestCase("scrap_02"))
    # suite.addTest(TestCase("scrap_03"))
    # suite.addTest(TestCase("scrap_04"))
    # suite.addTest(TestCase("scrap_05"))
    # suite.addTest(TestCase("scrap_06"))

    '''
    盘点单模块
    '''
    # suite.addTest(TestCase("inven_01"))
    # suite.addTest(TestCase("inven_02"))
    suite.addTest(TestCase("inven_03"))
    # suite.addTest(TestCase("inven_04"))
    # suite.addTest(TestCase("inven_05"))
    # suite.addTest(TestCase("inven_06"))
    # suite.addTest(TestCase("inven_07"))
    # suite.addTest(TestCase("inven_08"))
    # suite.addTest(TestCase("inven_09"))

    '''
    报表模块
    '''
    # suite.addTest(TestCase("repo_01"))
    # suite.addTest(TestCase("repo_02"))
    # suite.addTest(TestCase("repo_03"))
    # suite.addTest(TestCase("repo_04"))
    # suite.addTest(TestCase("repo_05"))
    # suite.addTest(TestCase("repo_06"))
    # suite.addTest(TestCase("repo_07"))
    # suite.addTest(TestCase("repo_08"))
    # suite.addTest(TestCase("repo_09"))
    # suite.addTest(TestCase("repo_10"))
    # suite.addTest(TestCase("repo_11"))
    # suite.addTest(TestCase("repo_12"))
    # suite.addTest(TestCase("repo_13"))
    # suite.addTest(TestCase("repo_14"))
    # suite.addTest(TestCase("repo_15"))

    report_dir = '../report'
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReportCN(stream=f, title='测试报告', description='Android ShopForce自动化测试')
        runner.run(suite)
    f.close()


