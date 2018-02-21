#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/26 21:37
# @Author :FengXiaoqing
# @file   :Hanshu.py

def add(args):
    total = 0
    for i in args:
        total += i
    return total

def main():
    number = list()
    s = input("Please input some number add (a + b + c ..):")
    print(s)
    for num in s.split("+"):
        number.append(int(num.strip("+")))
        print(add(number))

if __name__ == '__main__':
    main()