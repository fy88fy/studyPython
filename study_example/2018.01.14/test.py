#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/14 13:23
# @Author :FengXiaoqing
# @file   :test.py
'''
class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = "Xi laideng"
        self.cuisine_type = "* * * * * "
    def describe_restaurant(self):
        print ("这个饭店名字：%s ") % self.restaurant_name
        print ("这个饭店等级：%s ") % self.cuisine_type

    def open_restaurant(self):
        print "这个饭店正在营业！"

restaurant = Restaurant(1,2)
print (restaurant.describe_restaurant())
print (restaurant.open_restaurant())
'''

'''
class People(object):
    color = 'yellow'
    def think(self):
        self.color = "black"
        print "I am a %s "  % self.color
        print ("I am a thinker")
ren = People()
print ren.color
print ren.think()
'''
#
# class People(object):
#     color = 'yellow'
#     __age = 30
#
#     def __str__(self):
#         return "This is a Poeple Class.."
#
#     # def __init__(self):
#     #     print ("init.....")
#     #     self.think()
#     #     self.talk()
#
#
# class Chinese(People):
#     name = "fxq"
#     # print ("I am a Chinese...")
#
# class Chinese1(object):
#     name1 = "fxq1"
#     print Chinese.name
#     print name1
#
#     # print ("I am a Chinese1111...")
#
#     def think(self):
#         self.color = 'black'
#         print ("I am a %s people") % self.color
#         print ("I can thinking...")
#         print ("I am %s year's old") % self.__age
#     think = classmethod(think)
#
#     @classmethod
#     def talk(self):
#         print ("I am talking with Tom.")
#
#     @staticmethod
#     def test():
#         print ("Testing...")
#         print People.__age
#     # def __del__(self):
#     #     print ("Dell....")
# # ren = People()
#
#
# # print People.talk()
# #ren = People()
# #print ren.color
# #print ren.think()
#
# # print People.think()
# # print '#'*50
# #print ren.test()
# # print People.sm()
# a = ' aaaaaba  sdfx qs353 235asdf '
# print (a.strip())
# print (a)
# print (a.lstrip())
# print(a.rstrip())
# ```
# name = 'fengxiaoqing'
# age = 30
# home = 'chengde'
# print('hello'+name)
# print('hello {0}').format(name)
# print('hello %s') % name
# print('hello %d') % age
# print('我的年龄是：{0} 我的家:{1}').format(age,home)
# print('{name}:{age}'.format(name='fxq',age=20))


# str1 = '12poqiwrtgopwert'
# str2 = list(str1)
# print(type(str1))
# print(type(str2))
# print(list(str1))
# print(dir(str2))
# print('####'*20)
#
# a = [123,'bbb','ace']
# print(a[1])
# print(a.index('bbb'))
# a.insert(1,'aaa')
# print(a)
#
# a.sort()
# print a
# a.reverse()
# print a
#
# a.append('ooo')
# print (a)
#
# a.pop()
# print(a)
#
# a.remove(123)
# print(a)
#
# a.pop(1)
# print(a)
#
#
#

# 切片
# a = [11,'222','33',444,555,666]
# print(a[3:])
# print(a[1:5])
# print(a[1:6:2])
# print(a[:4])
# print(a[-1])
# print(a[-2:])
# print(a[-4:-2])


a = [1,3,4,5,6,'a','b',True,{"name":'fxq'}]
# a.append(123)
# a.append(456)
# a.pop(0)
# a.sort()
# a.reverse()
index = a.index('a')
print(a)
print(index)
print(a[1:5])


