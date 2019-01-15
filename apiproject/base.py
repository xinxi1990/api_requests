#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 部门
"""
import requests,unittest,os,yaml,json
from logger import get_logger
import time
logger = get_logger()
current_path = os.path.abspath(os.path.dirname(__file__))
token_yaml = os.path.join(current_path,"token.yaml")


class Base(unittest.TestCase):

    def setUp(self):
        '''
        读取本地token
        :return:
        '''
        with open(token_yaml, "r") as yaml_file:
            yaml_obj = yaml.load(yaml_file.read())
            self.token = yaml_obj["access_token"]


    def tearDown(self):
        logger.info("测试用例结束...")