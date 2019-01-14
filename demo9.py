#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest的命令行执行
"""
import unittest,requests,json,sys
from demo5 import Demo5
from demo6 import Demo6
reload(sys)
sys.setdefaultencoding("utf-8")

'''
查看命令行参数
python -m unittest -h

 -v, --verbose    Verbose output(输出日志等级)
  -f, --failfast   Stop on first failure(停止运行当第一个失败)
  -c, --catch      Catch control-C and display results
  -b, --buffer     Buffer stdout and stderr during test runs
  -s directory     Directory to start discovery ('.' default)
  -p pattern       Pattern to match test files ('test*.py' default)
  -t directory     Top level directory of project (default to
                   start directory)

'''

'''
执行某个类中的某个方法
python -m unittest demo5.Demo5.test_book_1
'''

'''
执行某个类中所有方法
python -m unittest demo5.Demo5
'''

'''
-v参数的打印详情
python -m unittest -v demo5
'''

'''
-f停止运行当第一个失败
python -m unittest -f -v demo10
如果一个class中有两个测试类,执行第一个测试类方法,则不会继续执行第二个测试方法

'''

'''
python -m unittest discover -s /Users/xinxi/PycharmProjects/api_requests/demosuite -p "test*.py"
命令行discover匹配模式
'''

