#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 部门
"""
import requests,unittest,os,yaml,json,time
from logger import get_logger
logger = get_logger()
from base import Base


class Departmen(Base):


    def setUp(self):
        '''
        读取本地token
        :return:
        '''
        super(Departmen, self).setUp()
        self.department_name = "北京研发中心"
        self.id = 2


    # def test_del_department(self):
    #     '''
    #     删除部门
    #     :return:
    #     '''
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/department/" \
    #           "create?access_token={}&id={}".format(self.token,self.id)
    #     r = requests.get(url)
    #     print r.json()
    #     self.assertEqual(r.json()["errcode"],60008)
    #     logger.info("删除部门-测试通过!")


    def test_creat_department(self):
        '''
        创建部门
        :return:
        '''
        data = \
        {
            "name": self.department_name,
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/" \
              "create?access_token={}".format(self.token)
        r = requests.post(url, data=json.dumps(data))
        self.assertEqual(r.json()["errcode"],0)
        logger.info("创建部门-测试通过!")


    def test_getlist_department(self):
        '''
        获取部门列表
        :return:
        '''
        data = \
        {
            "name": self.department_name,
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/" \
              "list?access_token={}".format(self.token)
        r = requests.get(url)
        self.assertEqual(r.json()["errcode"],0)
        logger.info("获取部门列表-测试通过!")

