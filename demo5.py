#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest框架的断言
"""
import unittest,requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Demo5(unittest.TestCase):

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
        print "请求接口地址:" + r.url
        self.assertEqual(r_json['errCode'],0,"断言errCode失败...")
        self.assertEqual(len(r_json['data']['catalogList']), 82, "断言catalogList的长度失败...")
        self.assertEqual(r_json['data']['catalogList'][0]['level'], 0, "断言catalogList列表中第0个level的值失败...")
        # 断言实际值和预期值是否一致
        # 三个参数: 实际值、预期值、断言失败的错误提示


    def test_assert(self):
        """
        介绍几种常见断言方法
        case.py中定义很多断言方法,此处仅仅介绍几个常见的方法
        :return:
        """
        self.assertTrue(True) # 断言正确
        self.assertFalse(False) # 断言错误
        self.assertEqual(1,1) # 断言两个值等于
        self.assertNotEqual(1,2) # 断言两个值不等于
        self.assertGreater(3,2) # 断言大于
        self.assertGreaterEqual(3, 3)  # 断言大于等于
        self.assertLess(3, 4)  # 断言小于
        self.assertLessEqual(3, 3)  # 断言小于等于




    def tearDown(self):
        print "结束方法..."



    @classmethod
    def tearDownClass(cls):
        print "结束类..."



if __name__ == '__main__':
    unittest.main()