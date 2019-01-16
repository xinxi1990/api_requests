#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 运行入口
"""
import requests,unittest,os,yaml,json,pytest,subprocess
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


def init_report():
    '''
    生成测试报告
    :return:
    '''
    cmd = "allure generate --clean data -o reports"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    logger.info("报告地址:{}".format(report_path))






if __name__ == '__main__':
    pytest.main(["-s", "--reruns=1", ".", "--alluredir=data"])
    init_report()