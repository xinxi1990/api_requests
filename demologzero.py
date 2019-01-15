#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 使用logzero作为log日志
"""

import logging
from logzero import logger
from logzero import setup_logger

def get_logger():
    logger = setup_logger(name="mylogger", logfile="logger.log", level=logging.INFO)
    return logger

if __name__ == '__main__':
    get_logger().info("logzero logger test")