#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/2 20:23
# @Author :FengXiaoqing
# @file   :canshu.py

# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
import sys
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            print ("%s is not a number:") % s
            sys.exit()
    else:
        print ('%s in a number') % s

isNum(sys.argv[1])