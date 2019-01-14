#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 第一个接口测试
"""

import requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Demo1():

    def test_hot(self):
        """
        获取正在热映的电影数据,使用get方法
        :return:
        """
        hot_url = "https://api.douban.com/v2/movie/in_theaters"
        # 获取正在热映的电影
        params = {"city":"广州",
                  "start":0,
                  "count":10}
        # 拼接get请求参数
        r  = requests.get(hot_url,params=params)
        print "请求接口地址:" + r.url
        req = json.dumps(r.json(),indent=4)
        print "请求接口返回数据:" + req


    def test_book(self):
        """
        获取电子书列表页数据,使用post方法
        :return:
        """
        url = "https://m.igetget.com/hybrid/api/v1/ebook/detail"
        payload = '{"bid":3210,"userInfo":{"uid": "229461915"}}'
        headers = {
            'Content-Type': "application/json",
        }
        r = requests.post(url, data=payload, headers=headers)
        req = json.dumps(r.json(), indent=4)
        print "请求接口地址:" + r.url
        print "请求接口返回数据:" + req



if __name__ == '__main__':
    Demo1().test_book()