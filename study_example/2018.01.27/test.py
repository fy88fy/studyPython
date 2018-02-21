#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/27 14:21
# @Author :FengXiaoqing
# @file   :test.py
# def sum(x,y):
#     print('x = {0}'.format(x))
#     print('x = {0}'.format(y))
#     return x+y
# m = sum(3,10)
# print(m)


# def funcA(a,b=0):
#     print(a)
#     print(b)
# funcA(1)
# print('#'*20)
# def funcA(a,b=0):
#     print(a)
#     print(b)
# funcA(1,20)
# print('#'*20)
#
# def funcD(a,b,*c):
#     print(a)
#     print(b)
#     print('length of c is : {0}'.format(len(c)) )
#     print(c)
# funcD(1,2,3,543,646,778,8)

#
# def funcF(a,**b):
#     print(a)
#     for x in b:
#         print(x+ ":" + str(b[x]))
# funcF(100,x='hello',y='你好')
# args = {'1':'a','2':'b'}
# funcF(100,**args)

# lt = (x*x for x in range(1,11) if x%2 ==0)
# for i in lt:
#     print(i)


# class ren(object):
#     name = 'meizi'
#     sex = 'F'
#     def hello(self):
#         print('hello world')
# a = ren()
#
# print(type(a))
# print(a.name)
# print(a.sex)
# a.hello()
# a.name = 'meinv'
# print('#'*20)
# print(a.name)


# class ren():
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#
#     def hello(self):
#         print('hello {0}'.format(self.name))
# ren = ren('fxq','M')
# ren.hello()
# print(ren.name)
# #############################################
# class A():
#     pass
#
# class B(A):
#     pass
#
# class C(A,B): #多继承
#     pass

# class parent(object):
#     parent_name = 'parent'
#     sex = 'Man'
#     def __init__(self,address,age):
#         self.age =  90
#         self.address = 'beijing'
#         print('my name is {0}'.format(self.parent_name))
#     def get_name(self):
#         return self.parent_name
#     def get_sex(self):
#         return self.sex
#
# class child(parent):
#     child_name = 'child'
#     # sex = 'woman'
#     def __init__(self,address,age):
#         super(child, self).__init__(address,age)
#         print('my name is {0}'.format(self.child_name))
#     def hello(self):
#         print('hello world!')
#     def get_name(self):
#         super(child,self).get_name()
#         print("today is  a nice day")
#
# # parent = parent()
# child =child('beijing',11)
# print(child.get_name)
# print(child.sex)
# print(child.address)
# print(child.age)
# # print(child.get_sex())
# # child.hello()





try:
    a = 10
    b = 0
    a/b
except Exception as e:
    print('error')
else:
    print('this is OK!')
finally:
    print('END')


print('################################')
a = [1,3,4]
try:
    print(a[4])
except Exception as e:
    print(e)

