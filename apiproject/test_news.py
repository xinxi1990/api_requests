#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 消息
"""
import requests,unittest,os,yaml,json,time
from logger import get_logger
logger = get_logger()
from base import Base

class News(Base):

    def setUp(self):
        '''
        读取本地token
        :return:
        '''
        super(News, self).setUp()

    def test_news(self):
        '''
        发文本消息
        :return:
        '''

        data = \
        {
            "msgtype": "text",
            "agentid": "1000002",
            "touser": "@all",
            "text": {
                "content": "接口文本消息测试_{}".format(time.time())
            },
            "safe": 0
        }

        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(self.token)
        r = requests.post(url, data=json.dumps(data))
        print r.json()
        self.assertEqual(r.json()["errcode"],0)
        logger.info("创建部门-测试通过!")


if __name__ == '__main__':
    unittest.main()