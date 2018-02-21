#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/2 21:06
# @Author :FengXiaoqing
# @file   :__init__.py.py
#
# var6 = '全局变量 '
# class MyClass(object):
#     var1 = '类属性，类的公有属性 var1'    ##定义在方法外
#     __var2 = '类的私有属性 __var2'
#
#     def func1(self):
#         self.var3 = '对象的公有属性 var3'      ##定义在方法内
#         self.__var4 = '对象的私有属性 __var4'
#         var5 = '函数的局部变量'
#
#     def func2(self):
#         print self.var1
#         print self.__var2
#         print self.var3
#         print self.__var4
#         print self.var6
#
#
# mc = MyClass()
# mc.func1()
#
# mc.func2()
# print '*'*50
# print mc.__dict__
# print MyClass.var1
# #print MyClass.__var2    #不测通过类访问
# print mc.var3       #对象的属性只能通过对象来访问
# #print MyClass.__var4
#
# print MyClass.__dict__



class MyClass(object):
    name = 'Test'
    def __init__(self):
        self.func1()
        self.__func2()
        self.classFun()
        self.staticFun()

    def func1(self):
        print self.name,
        print "我是公有方法."

    def __func2(self):
        print self.name,
        print "我是私有方法."

    @classmethod
    def classFun(self):
        print self.name,
        print "我是类方法."

    @staticmethod
    def staticFun():
        print MyClass.name,
        print "我是静态方法."
mc = MyClass()

