#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest框架的断言
"""
import unittest,requests,json,sys,os
from logger import get_logger
log = get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")



class Demo10(unittest.TestCase):

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
        self.url = "https://m.igetget.com/hybrid/api/v1/ebook/detail"
        self.payload = '{"bid":3210,"userInfo":{"uid": "229461915"}}'
        self.headers = {
            'Content-Type': "application/json",
        }


    @unittest.skip("demonstrating skipping")
    def test_book_1(self):
        """
        获取电子书列表页数据,使用post方法
        断言返回数据中:errCode
        断言返回数据中:catalogList长度
        断言返回数据中:catalogList列表中第0个level的值
        :return:
        """
        # 设置请求头
        r = requests.post(self.url, data=self.payload, headers=self.headers)
        r_json = r.json()
        # 获取返回的json数据
        # print "请求接口地址:" + r.url
        log.info("*****请求接口地址******:" + r.url)
        self.assertEqual(len(r_json['data']['catalogList']), 82, "断言catalogList的长度失败...")


    def test_book_2(self):
        """
        获取电子书列表页数据,使用post方法
        断言返回数据中:errCode
        断言返回数据中:catalogList长度
        断言返回数据中:catalogList列表中第0个level的值
        :return:
        """

        # 设置请求头
        r = requests.post(self.url, data=self.payload, headers=self.headers)
        r_json = r.json()
        # 获取返回的json数据
        log.info("*****请求接口地址******:" + r.url)



if __name__ == '__main__':
    unittest.main()