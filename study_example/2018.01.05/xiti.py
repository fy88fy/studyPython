#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/9 21:02
# @Author :FengXiaoqing
# @file   :xiti.py
# 习题
# 1. 从终端接收若干个数字，要求使用filter()函数，将输入的不是数字的值剔除掉(用户输入的内容有随机性，当我们要接收一个数字的时候，他可能会输入一个字符串过来，要求当用户输入的不是数字，就剔除掉)
#
#
# 2. 从终端接收若干个以空格隔开的字符串，然后去除所有的26个字符之外的字符后，打印到屏幕上
# 要求：使用map()函数，map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#
# 3.从终端接收若干个以空格隔开的字符串
# (1).以空格隔开的字符串为用户想要输入的一个值
# (2).用户在输入时不小心按出来了字母键
# 示例如下
# "afda111 dafd222 3dfad33 4ss4dd4"
# 这个字符串，其实是用户想要求 111 222 333 444 的和
# 要求：把每个值中的字母去掉，并计算出所有值的和
# 提示：使用reduce函数，结合前两题使用过的方法，可以很简单的算出

# def funa(list1):
#     tmp = filter(lambda x:x.isdigit(),list1)
#     return tmp
# while True:
#     tmp1 = raw_input("please input a few number:")
#     print("{0}".format(funa(tmp1.split())))




# def funb(str1):
#     return filter(lambda x:x.isalpha(),str1)
# while True:
#     tmp = raw_input("Please input a sth string:")
#     tmp = tmp.split()
#     print("{0}".format(map(funb,tmp)))

# def func(str1):
#     return filter(lambda x:x.isdigit(),str1)
# while True:
#     tmp = raw_input("Please input a sth string:")
#     tmp = tmp.split()
#     list1 = map(func,tmp)
#     list1 = map(int,list1)
#     sum = reduce(lambda x,y:x+y,list1)
#     print ("sum={0}".format(sum))


def wordCont(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print lines,words,chars
s = open('/etc/passwd').read()
wordCont(s)