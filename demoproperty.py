#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 演示unittest框架的断言
"""
import unittest,requests,json,sys,os
from logger import get_logger
log = get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")


class DemoProperty(object):

    def __init__(self, score):
        self._score = score


    @property
    def score(self):
        # 定义score属性
        return self._score

    @score.setter
    def score(self, val):
        # 定义set方法
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

    @score.deleter
    def score(self):
        return self._score


if __name__ == '__main__':
    e = DemoProperty(100)
    print e.score
    e.score = 90
    print e.score




