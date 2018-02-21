#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/28 18:55
# @Author :FengXiaoqing
# @file   :dicSort.py

def sortDictValue(dict1):
    print(sorted(dict1.items(),key=lambda d:d[1],reverse=False))

if __name__ == '__main__':
    aaa = dict(a=100,b=10,c=50,d=1)
    l = list()
    l = sortDictValue(aaa)
    print(l)
    print(sortDictValue(l))

    # add(1,2,3,4,5)
    # s1 = lambda x,y:x+y
    # print(s1(10,20))
