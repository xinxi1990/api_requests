#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 使用HTMLTestRunner组织报告
"""
import unittest,requests,json,sys,os,time
import HTMLTestRunner
from ddt import ddt,data,file_data,unpack
from logger import get_logger
log = get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")

test_book_1_result = False

current_path = os.path.abspath(os.path.dirname(__file__))

@ddt
class Demo13(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        '''
        必须是静态方法
        执行顺序:setUpClass->setUp->test->tearDown->tearDownClass
        setUpClass和tearDownClass在一个类中只会执行一次
        :return:
        '''
        log.info("初始化类...")


    def setUp(self):
        '''
        执行顺序:setUp->test->tearDown
        每个test方法都走上面的执行顺序
        :return:
        '''

        log.info("初始化方法...")



    def test_book_1(self):
        """
        获取电子书列表页数据,使用post方法
        :return:
        """
        url = "https://m.igetget.com/hybrid/api/v1/ebook/detail"
        payload = '{"bid":3210,"userInfo":{"uid": "229461915"}}'
        headers = {
            'Content-Type': "application/json",
        }
        # 设置请求头
        r = requests.post(url, data=payload, headers=headers)
        req = json.dumps(r.json(), indent=4)
        print "请求接口地址:" + r.url
        #print "请求接口返回数据:" + req

    def test_book_2(self):
        """
        获取电子书列表页数据,使用post方法
        :return:
        """
        url = "https://m.igetget.com/hybrid/api/v1/ebook/detail"
        payload = '{"bid":3210,"userInfo":{"uid": "229461915"}}'
        headers = {
            'Content-Type': "application/json",
        }
        # 设置请求头
        r = requests.post(url, data=payload, headers=headers)
        req = json.dumps(r.json(), indent=4)
        log.info("请求接口地址:" + r.url)
        #print "请求接口返回数据:" + req


    def tearDown(self):
        print "结束方法..."

    @classmethod
    def tearDownClass(cls):
        print "结束类..."










if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Demo13)
    alltests = unittest.TestSuite([suite])
    current_path = os.path.abspath(os.path.dirname(__file__))
    report_path = os.path.join(current_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_abspath = os.path.join(report_path, "result_" + now + ".html")
    log.info("报告地址:{}".format(report_abspath))
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    runner.run(alltests)
    fp.close()