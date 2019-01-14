#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest框架的setUpClass和tearDownClass
"""
import unittest,requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Demo3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        必须是静态方法
        执行顺序:setUpClass->setUp->test->tearDown->tearDownClass
        setUpClass和tearDownClass在一个类中只会执行一次
        :return:
        '''
        print "初始化类..."


    def setUp(self):
        '''
        执行顺序:setUp->test->tearDown
        每个test方法都走上面的执行顺序
        :return:
        '''
        print "初始化方法..."



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
        print "请求接口地址:" + r.url
        #print "请求接口返回数据:" + req


    def tearDown(self):
        print "结束方法..."

    @classmethod
    def tearDownClass(cls):
        print "结束类..."



if __name__ == '__main__':
    unittest.main()