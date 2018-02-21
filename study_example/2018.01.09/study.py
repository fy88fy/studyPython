#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/8 20:42
# @Author :FengXiaoqing
# @file   :study.py

for i in xrange(1,10):
    for j in xrange(1,i+1):
        print "%s x %s = %s " % (j,i,j*i),
    print