#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/4 0:19
# @Author :FengXiaoqing
# @file   :trunslateWords.py
word = raw_input("Please input a word:")
def fun():
        global word
        with open("docs.txt") as file:
            for line in file:
                if line.startswith(word+' '):
                    mean = line.split()[1]
                    print "%s : %s" % (word,mean)
                    print "#####################"
            else:
                print "sorry,下面再无相关信息"
fun()
