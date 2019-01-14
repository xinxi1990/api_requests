#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest框架
"""
import unittest,requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Demo3(unittest.TestCase):


    def setUp(self):
        '''
        执行顺序:setUp->test->tearDown
        每个test方法都走上面的执行顺序
        :return:
        '''
        print "初始化..."



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
        print "结束..."

if __name__ == '__main__':
    unittest.main()