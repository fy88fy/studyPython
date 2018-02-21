#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/15 23:34
# @Author :FengXiaoqing
# @file   :register_user.py

class user(object):
    def __init__(self):
        print "*" * 41
        print ("****************Dictionary***************")
        print "*" * 41
        print ("***************Rigister user*****************")
        print ("1.注册用户")
        print ("2.查询用户")
        print ("3.返回上一级")
        print ("***************Rigister user*****************")

    def register(self):  #注册用户
        while True:
            # import datetime
            # time = datetime.datetime.now()
            print ("请软入您的个人信息：")
            while True:
                name = raw_input("请输入您的用户名:")
                if len(name) < 4 or len(name) > 10 :
                    print ("请输入输4 - 10个字符！")
                    continue
                else:
                    fd = open('users_list.txt')
                    for line in fd:
                        if name in line:
                            print ("对不起,用户已存在!")
                            continue
                        else:
                            pass

                    break

                    fd.close()

            while True:
                passwd = raw_input("请输入您的密码:")
                if len(name) < 4 or len(passwd) > 10 or not passwd.isalnum() :
                    print ("请输入输4 - 10个字母和数字组合的密码字符！")
                    continue
                else:
                    break

            age = raw_input("请输入您的年龄:")
            job = raw_input("请输入您的工作:")

            f = open('users_list.txt','a+')
            f.write(name,)
            f.write(',')
            f.write(passwd,)
            f.write(',')
            f.write(age,)
            f.write(',')
            f.write(job,)
            # f.write(time = raw_input(time),)
            f.write('\n')

            f.close()
            print ("恭喜您 \033[31m %s \033[0m 用户注册成功!") % name
            break

    def input(self):
        number = int(raw_input("请输入您的选择（1、2或3）:"))

        if number == 1 :
            print  register.register()
            print ("1-注册用户")


        elif number == 2 :
            print ("2.搜索用户")
        elif number == 3 :

            print ("3.返回上一级")
            exit
        else:
            print ("Please input 1/2/3/")

register = user()
print register.input()


