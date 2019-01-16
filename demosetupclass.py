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


class DemoSetUpClass(unittest.TestCase):

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

    def test_case_1(self):
        '''
        用例必须以"test"开头
        :return:
        '''
        print "test_case_1"

    def test_case_2(self):
        '''
        用例必须以"test"开头
        :return:
        '''
        print "test_case_2"


    def tearDown(self):
        print "结束方法..."

    @classmethod
    def tearDownClass(cls):
        print "结束类..."


if __name__ == '__main__':
    unittest.main()