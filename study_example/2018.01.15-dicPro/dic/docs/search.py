#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/17 23:05
# @Author :FengXiaoqing
# @file   :search.py

class search(object):
    def __init__(self):
        print ("*" * 41)
        print ("****************Dictionary***************")
        print ("*" * 41)
        print ("***************Search Words*****************")
        print ("1.单词查询")
        print ("2.查询历史")
        print ("3.返回上一级")
        print ("***************Search Words*****************")

    def search(self): #查询单词
        word = input("请输入查询的单词：")
        file_dic = open('dictionary.txt')
        for line in file_dic:
            line = line.split()
            word = word.strip()
            if word == line[0]:
                print (line[1])

            else:
                pass

    def serrch_log(self): # 记录查询历史
        search()

        f_search = open('../history/serch_history.log','a+')
        f_search.write(word, )
        f_search.write(',')
        f_search.write(line, )
        f_search.write(',')
        f_search.write('age,' )
        f_search.write(',')
        f_search.write('job,' )
        f_search.write(time = input(time),)
        f_search.write('\n')
        f_search.close()
    def input(self):

            number = int(input("请输入您的选择（1、2或3）:"))
            if number == 1 :
                print  (search.search())
                search.serrch_log()
            elif number == 2 :
                print ("2.查询历史")
            elif number == 3 :
                print ("3.返回上一级")
                exit
            else:
                print ("Please input 1/2/3/")
search = search()
search.input()





