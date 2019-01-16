#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示requests几个常用的方法
"""
import requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Demo2():


    def test_demo(self):
        """
        获取电子书列表页数据,使用post方法
        :return:
        """
        url = "https://m.igetget.com/hybrid/api/v1/ebook/detail"
        payload = '{"bid":3210,"userInfo":{"uid": "229461915"}}'
        headers = {
            'Content-Type': "application/json",
        }
        # 设置请求头
        r = requests.post(url, data=payload, headers=headers)
        req = json.dumps(r.json(), indent=4)
        print "请求接口地址:" + r.url
        print "请求接口返回数据:" + req
        print "请求接口状态码:{}".format(r.status_code)
        print "请求接口耗时:{}".format(r.elapsed)
        print "请求接口响应header头:{}".format(r.headers)
        print "请求接口响应cookies:{}".format(r.cookies)
        print "请求接口响应content:{}".format(r.content)
        print "请求接口响应raw:{}".format(r.raw)
        print "请求接口响应text:{}".format(r.text)


if __name__ == '__main__':
    Demo2().test_demo()