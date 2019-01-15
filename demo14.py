#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 使用allure组织报告
"""
import unittest,requests,json,sys,os,time,allure
from ddt import ddt,data,file_data,unpack
from logger import get_logger
log = get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")


@allure.feature("Demo14")
class Demo14(unittest.TestCase):

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


    @allure.story('电子书-用例1')
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
        log.info("请求接口地址:" + r.url)
        #log.info("请求接口返回数据:" + req)


    @allure.story('电子书-用例2')
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
        #log.info("请求接口返回数据:" + req)


    def tearDown(self):
        log.info("结束方法...")


    @classmethod
    def tearDownClass(cls):
        log.info("结束类...")


if __name__ == '__main__':
    unittest.main()