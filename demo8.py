#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest的测试方法执行,懒加载所有"*_test.py"的文件, Test Discover模式
"""
import unittest,requests,json,sys
from demo5 import Demo5
from demo6 import Demo6
reload(sys)
sys.setdefaultencoding("utf-8")


class Demo7():
    pass

if __name__ == '__main__':
    test_dir = './demosuite'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)
    # 使用discover模式(匹配模式),运行所有test*.py中所有测试类
    # run()方法执行discover，大大简化了测试用例的查找与执行