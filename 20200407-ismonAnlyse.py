#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :20200407-ismonAnlyse.py
@说明    :分析飞康“ismon -l”命令产生的日志
@时间    :2020/04/07 10:16:32
@作者    :Max2055
@版本    :1.0
'''

import os, shutil, re

lnsrFile = 'D:\\Users\\wucl\\Desktop\\logs\\ismon\\ipstor_ismon_test.log'
resultFile = 'D:\\Users\\wucl\\Desktop\\logs\\ismon\\ipstor_ismon_out.txt'

with open(lnsrFile, 'r') as raw:
    for line in raw:
        print(line[1:30])

