#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/26 21:53
# @Author :FengXiaoqing
# @file   :dateTime.py
from datetime import datetime  # 这样才是把datetime中的datetime类给导入
y = int(input('请输入4位数字的年份（如：2018）：'))  # 获取年份
m = int(input('请输入月份（如：05）：'))  # 获取月份
d = int(input('请输入是哪一天（如：12）：'))  # 获取“日”
dt = datetime(y, m, d)
print("您输入的日期是{0}第".format(y)+dt.strftime("%j")+"天")  # a.strftime("%Y-%m-%d %H:%M:%S")  a.strftime("%T")