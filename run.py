#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 使用allure组织报告
"""
import pytest,os,subprocess
from logger import get_logger
log = get_logger()


def init_report():
    '''
    生成测试报告
    :return:
    '''
    cmd = "allure generate --clean data -o reports"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    log.info("报告地址:{}".format(report_path))


pytest.main(["-s","--reruns=1", "demosuite","--alluredir=data"])
init_report()