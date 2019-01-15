#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 用户
"""

import requests,unittest,os,yaml,json
from logger import get_logger
logger = get_logger()
from base import Base


class User(Base):

    def setUp(self):
        '''
        读取本地token
        :return:
        '''
        super(User,self).setUp()
        self.userid = "testuser"


    def test_del_user(self):
        '''
        删除成员
        :return:
        '''
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={}&userid={}".format(self.token,self.userid)
        r = requests.get(url)
        self.assertEqual(r.json()["errcode"], 0, '删除成员失败!')
        logger.info("删除成员-测试通过!")


    def test_creat_user(self):
        '''
        创建成员
        :return:
        '''
        data = {"userid": self.userid,
                "name": "测试账号",
                "mobile": "13800138000",
                "department": [1]}
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={}".format(self.token)
        r = requests.post(url, data=json.dumps(data))
        self.assertEqual(r.json()["errcode"],0,'创建成员失败!')
        logger.info("创建成员-测试通过!")


    def test_get_user(self):
        '''
        获取成员
        :return:
        '''
        params = {"access_token": self.token,
                  "userid": self.userid}
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = requests.get(url, params=params)
        self.assertEqual(r.json()["errmsg"], 'ok', '获取成员失败!')
        logger.info("获取成员-测试通过!")



