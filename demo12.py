#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示ddt
"""
import unittest,requests,json,sys,os
from ddt import ddt,data,file_data,unpack
from logger import get_logger
log = get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")

test_book_1_result = False

current_path = os.path.abspath(os.path.dirname(__file__))

@ddt
class Demo12(unittest.TestCase):


    def setUp(self):
        '''
        执行顺序:setUp->test->tearDown
        每个test方法都走上面的执行顺序
        :return:
        '''
        print "初始化方法..."
        self.url = "https://m.igetget.com/hybrid/api/v1/ebook/detail"
        self.headers = {'Content-Type': "application/json"}

    @unittest.skip("跳过执行这个方法")
    @data(3210, 3220)
    def test_book_1(self,bid):
        """
        设置多个bid参数
        :return:
        """
        self.payload = '{"bid":' + str(bid) +',"userInfo":{"uid": "229461915"}}'
        log.info("*****test_book_1请求参数******:" + self.payload)
        r = requests.post(self.url, data=self.payload, headers=self.headers,verify=False)
        r_json = r.json()
        # 获取返回的json数据
        # print "请求接口地址:" + r.url
        log.info("*****test_book_1请求接口地址******:" + r.url)
        self.assertEqual(r_json['errCode'], 0, "断言errCode失败...")
        log.info("****test_book_1测试成功!******")

    @unittest.skip("跳过执行这个方法")
    @data([3210, 229461915], [3220, 229461914])
    def test_book_2(self,value):
        """
        设置多个bid和udid两个参数
        :return:
        """
        bid =  value[0]
        udid = value[1]
        self.payload = '{"bid":' + str(bid) + ',"userInfo":{"uid":  ' + str(udid) + '}}'
        r = requests.post(self.url, data=self.payload, headers=self.headers)
        r_json = r.json()
        # 获取返回的json数据
        # print "请求接口地址:" + r.url
        log.info("*****test_book_1请求接口地址******:" + r.url)
        self.assertEqual(r_json['errCode'], 0, "断言errCode失败...")
        log.info("****test_book_1测试成功!******")

    @unittest.skip("跳过执行这个方法")
    @data([3210, 229461915], [3220, 229461914])
    @unpack
    def test_book_2(self,bid,udid):
        """
        设置多个bid和udid两个参数
        使用unpack解包上面两个参数
        :return:
        """
        self.payload = '{"bid":' + str(bid) + ',"userInfo":{"uid":  ' + str(udid) + '}}'
        r = requests.post(self.url, data=self.payload, headers=self.headers)
        r_json = r.json()
        # 获取返回的json数据
        # print "请求接口地址:" + r.url
        log.info("*****test_book_1请求接口地址******:" + r.url)
        self.assertEqual(r_json['errCode'], 0, "断言errCode失败...")
        log.info("****test_book_1测试成功!******")


    @file_data(current_path + '/datas/demoddt.json')
    def test_book_2(self,value):
        """
        设置多个bid和udid两个参数
        使用unpack解包上面两个参数
        :return:
        """
        print "****{}".format(value)
        bid = value[0]
        udid = value[1]
        self.payload = '{"bid":' + str(bid) + ',"userInfo":{"uid":  ' + str(udid) + '}}'
        r = requests.post(self.url, data=self.payload, headers=self.headers)
        r_json = r.json()
        # 获取返回的json数据
        # print "请求接口地址:" + r.url
        log.info("*****test_book_1请求接口地址******:" + r.url)
        self.assertEqual(r_json['errCode'], 0, "断言errCode失败...")
        log.info("****test_book_1测试成功!******")


    @file_data(current_path + '/datas/demoddt.yaml')
    def test_book_2(self,value):
        """
        设置多个bid和udid两个参数
        使用unpack解包上面两个参数
        :return:
        """
        print "****{}".format(value)
        bid = value[0]
        udid = value[1]
        self.payload = '{"bid":' + str(bid) + ',"userInfo":{"uid":  ' + str(udid) + '}}'
        r = requests.post(self.url, data=self.payload, headers=self.headers)
        r_json = r.json()
        # 获取返回的json数据
        # print "请求接口地址:" + r.url
        log.info("*****test_book_1请求接口地址******:" + r.url)
        self.assertEqual(r_json['errCode'], 0, "断言errCode失败...")
        log.info("****test_book_1测试成功!******")


if __name__ == '__main__':
    unittest.main()