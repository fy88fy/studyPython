#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/17 22:18
# @Author :FengXiaoqing
# @file   :login.py.py

class login(object):
    def __init__(self):
        # self.name = name
        # self.sex = sex
        # self.age = age
        # self.job = job
        print "*" * 41
        print ("****************Dictionary***************")
        print "*" * 41
        print ("***************Login user*****************")
        print ("1.用户登录")
        print ("2.退出软件")
        print ("3.返回上一级")
        print ("***************Login user*****************")

    def login(self):
        print ("请输入登录用户名和密码")
        name = raw_input("请输入登录用户名:")
        passwd = raw_input("请输入登录密码:")

        file_passwd =open('users_list.txt')
        while True:
            for line in file_passwd:
                if name in line and passwd in line :
                    print ("登录成功！！")
                    break
                else:
                    continue
            if name not in line and passwd not in line:
                print ("用户名或密码错误")
            break

    def input(self):
        number = int(raw_input("请输入您的选择（1、2或3）:"))

        if number == 1 :
            print  login.login()
            print ("1-用户登录")


        elif number == 2 :
            print ("2.退出软件")
            exit
        elif number == 3 :

            print ("3.返回上一级")
            exit
        else:
            print ("Please input 1/2/3/")



login = login()
login.input()

