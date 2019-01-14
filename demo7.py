#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest的测试方法执行,自定义
"""
import unittest,requests,json,sys
from demo4 import Demo4
from demo5 import Demo5
from demo6 import Demo6
reload(sys)
sys.setdefaultencoding("utf-8")


class Demo7():

    def suite_method(self):
        '''
        定义一个suite
        可以把多个测试类的指定方法加入都一个用例集中
        :return:
        '''
        suite = unittest.TestSuite()
        suite.addTest(Demo5('test_book_1'))
        suite.addTest(Demo6('test_book_2'))
        return suite


    def suite_class(self):
        '''
        定义一个suite
        可以把多个测试类的每个方法加入都一个用例集中
        :return:
        '''
        print "运行suite_2"
        suite1 = Demo4.TheTestSuite()
        suite2 = Demo5.TheTestSuite()
        suite3 = Demo6.TheTestSuite()
        alltests = unittest.TestSuite([suite1, suite2])
        return suite

    def suite_class_new(self):
        '''
        定义一个suite
        可以把多个测试类的每个方法加入都一个用例集中 等同于上边的
        :return:
        '''
        print "运行suite_2"
        suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo4)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo5)
        suite3 = unittest.TestLoader().loadTestsFromTestCase(Demo6)
        alltests = unittest.TestSuite([suite1, suite2])
        return suite


if __name__ == '__main__':
    test_suite = Demo7().suite_class_new()
    unittest.TextTestRunner(verbosity=2).run(test_suite)