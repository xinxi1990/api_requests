#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 登录
"""

import requests,unittest,os,yaml
from logger import get_logger
from config import *
logger = get_logger()
current_path = os.path.abspath(os.path.dirname(__file__))
token_yaml = os.path.join(current_path,"token.yaml")


class Login(unittest.TestCase):

    def test_get_token(self):
        '''
        获取token
        :return:
        '''
        params = {"corpid":corpid,"corpsecret":corpsecret}
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        self.r = requests.get(url,params=params)
        self.assertEqual(self.r.status_code,200)
        self.assertEqual(self.r.json()['errmsg'], 'ok')
        logger.info("获取token-测试通过!")


    def tearDown(self):
        with open(token_yaml, "w") as yaml_file:
            yaml_obj = {}
            yaml_obj["access_token"] = self.r.json()['access_token']
            yaml.dump(yaml_obj, yaml_file)

