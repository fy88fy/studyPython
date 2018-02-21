#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/2 21:06
# @Author :FengXiaoqing
# @file   :printPID.py
import sys
import os
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            print ("%s is not a number:") % s
            break
    else:
        print  s

for i in os.listdir("D:/"):
    isNum(i)