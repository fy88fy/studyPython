#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/28 22:34
# @Author :FengXiaoqing
# @file   :production.py

a = [x*x for x in range(1,11) if x%2 ==0]
print (a)
print(type(a))

b = (x*x for x in range(1,11) if x%2 ==0)
print (b)
print(type(b))
for i in b:
    print(i)
print('#'*20)


def test(l):
    for i in l:
        yield i
        print("OK i = {0}".format(i))

m = test([1,2,3,4,5,6])
for i in m:
    print(i)

