#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest框架的skip功能,skip作用是不执行这方法
"""
import unittest,requests,json,sys,os
from logger import get_logger
log = get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")

test_book_1_result = False

class Demo11(unittest.TestCase):


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
        log.info("*****test_book_1请求接口地址******:" + r.url)
        self.assertEqual(r_json['errCode'], 0, "断言errCode失败...")
        global  test_book_1_result
        test_book_1_result = True
        log.info("****test_book_1测试成功!******")


    @unittest.skip("跳过执行这个方法")
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
        log.info("*****test_book_2请求接口地址******:" + r.url)


    @unittest.skipIf(2 > 1,"执行test_book_3方法")
    def test_book_3(self):
        """
        获取电子书列表页数据,使用post方法
        如果skipif的条件成立,则跳过这个用例
        :return:
        """
        print test_book_1_result

        # 设置请求头
        r = requests.post(self.url, data=self.payload, headers=self.headers)
        r_json = r.json()
        # 获取返回的json数据
        log.info("*****test_book_3请求接口地址******:" + r.url)


    @unittest.expectedFailure
    def test_fail(self):
        '''
        当失败的时候,调用这个装饰器
        :return:
        '''
        self.assertEqual(1, 0, "broken")


if __name__ == '__main__':
    unittest.main()