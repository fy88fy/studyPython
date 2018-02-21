#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/2 19:49
# @Author :FengXiaoqing
# @file   :int.py

def fun():
    sth = raw_input("Please input sth: ")
    try: #捕异常
        if type(int(sth))==type(1):
            print("%s is a number") % sth
    except:
        print("%s is not number") % sth
fun()

