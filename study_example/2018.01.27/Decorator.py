#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/28 22:54
# @Author :FengXiaoqing
# @file   :Decorator.py
#
# def test():
#     print('#############')
#     print('#############')
#
# def hello():
#     print("hello world")
#
# print (callable(hehello()
#
# a = 'hello'
# print(a)

#
# def startend(func):
#     def start():
#         print("#########start#############")
#         func()
#         print("#########end#############")
#     return start
# def hello():
#     print("hello world!")
# hello = startend(hello)
# hello()


def startend(func):
    def start():
        print("#########start#############")
        func()
        print("#########end#############")
    return start
@startend
def hello():
    print("hello world!")
hello()