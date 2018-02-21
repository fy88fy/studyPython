#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/7 21:24
# @Author :FengXiaoqing
# @file   :test.py
import os
import sys
path = '.'
def print_files(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path,i))]
    files = [i for i in lsdir if os.path.isfile(os.path.join(path,i))]
    if dirs:
        for d in dirs:
            print_files(os.path.join(path,d))
    if files:
        for f in files:
            print os.path.join(path,f)
print_files(sys.argv[1])