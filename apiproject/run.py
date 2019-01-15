#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 运行入口
"""
import requests,unittest,os,yaml,json
from logger import get_logger
logger = get_logger()
from test_user import User
from test_login import Login
from test_news import News


def main():
    logger.info("*" * 10 + "运行开始" + "*" * 10)
    suite = unittest.TestSuite()
    suite.addTest(Login('test_get_token'))
    suite.addTest(User('test_del_user'))
    suite.addTest(User('test_creat_user'))
    suite.addTest(User('test_get_user'))
    suite.addTest(News('test_news'))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    logger.info("*" * 10 + "运行结束" + "*" * 10)
    print(test_result.testsRun)

if __name__ == '__main__':
    main()