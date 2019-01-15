#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 日志类
"""

import logging,sys,os
reload(sys)
sys.setdefaultencoding("utf-8")


def get_logger():
    '''
    追加保存本地log_test.log文件中
    在控制台可输出log日志
    :return:
    '''
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..')  # 返回脚本的路径
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='log_test.log',
                        filemode='a')
    logger = logging.getLogger()
    logger.level = logging.INFO
    # stream_handler = logging.StreamHandler(sys.stdout)
    # logger.addHandler(stream_handler)
    return logger