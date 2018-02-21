#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/15 22:54
# @Author :FengXiaoqing
# @file   :docs.py.py
import sys
import  os


class dic(object):
    def __init__(self):
        print ("*"*41)
        print ("****************Dictionary***************")
        print ("*"*41)
        print ("***************MENU LIST*****************")
        print ("1.查询单词")
        print ("2.注册用户")
        print ("3.退出软件")
        print ("***************MENU LIST*****************")

    def input(self):
        number = int(input("请输入您的选择（1、2或3）:"))

        if number == 1 :
            print ("1-查询单词")
        elif number == 2 :
            register = user()
            print (register.input())

            print ("2.注册用户")
        elif number == 3 :
            print ("3.退出成功")
            exit
        else:
            print ("Please input 1/2/3/")

dic = dic()
dic.input()