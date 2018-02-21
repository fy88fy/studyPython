#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/2/4 22:37
# @Author :FengXiaoqing
# @file   :CheckServer.py
import commands

date = commands.getoutput("date +%F")
cmd = commands.getoutput("df -h")
ps = commands.getoutput("ps aux | wc -l ")
net = commands.getoutput("netstat -lntp")

with open("1.txt", "ab") as df:
    df.write("############## start {0}  ########################".format(date))
    df.write("\n")
    df.write("cmd")
    df.write("\n")
    df.write("服务器的进行数量是：{0}".format(ps))
    df.write("\n")
    df.write("\n")
    df.write("服务器的启用的端口是：\n{0}".format(net))
    df.write("\n")
    df.write("############## END ##########################")
    df.write("\n")
