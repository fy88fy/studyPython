#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/6 16:55
# @Author :FengXiaoqing
# @file   :test.py
#打印100内偶数的平方

print ([ i**2 for i in range(1,100) if i%2==0])