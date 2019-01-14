#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest的测试方法执行,自定义
"""
import unittest,requests,json,sys
from demo5 import Demo5
from demo6 import Demo6
reload(sys)
sys.setdefaultencoding("utf-8")


class Demo7():

    def suite_1(self):
        '''
        定义一个suite
        :return:
        '''
        suite = unittest.TestSuite()
        suite.addTest(Demo5('test_book_1'))
        suite.addTest(Demo6('test_book_2'))
        # 可以把多个测试类的方法加入都一个用例集中
        return suite



if __name__ == '__main__':
    test_suite_1 = Demo7().suite_1()
    unittest.TextTestRunner(verbosity=2).run(test_suite_1)