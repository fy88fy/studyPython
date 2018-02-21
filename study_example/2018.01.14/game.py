#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/14 17:05
# @Author :FengXiaoqing
# @file   :game.py

class game(object):
    print ("Welcom to this People Game!")
    class Person(object):
        def __init__(self,name,sex,age,fight):
            self.name =name
            self.sex = sex
            self.age = age
            self.fight = fight

        def detail(self):
            # type: () -> object
            tail = "姓名：%s ;性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.sex, self.age, self.fight)
            print tail


        def grass(self):
            """注释：草丛战斗，消耗200战斗力"""
            self.fight = self.fight - 200
            print ("You fight is : %s") % self.fight

        def selfearn(self):
            """注释：自我修炼，增长100战斗力"""
            self.fight = self.fight + 1000
            print ("You fight is : %s") % self.fight

        def multiPlayer(self):
            """注释：多人游戏，消耗500战斗力"""
            self.fight = self.fight - 500
            print ("You fight is : %s") % self.fight



cang = game.Person('苍井井', '女', 18, 1000)# 创建苍井井角色
fxq = game.Person('fxq', '男', 19, 1000)# 创建苍井井角色
cang2 = game.Person('苍井井2', '女', 28, 1000)# 创建苍井井角色
cang3 = game.Person('苍井井3', '女', 38, 1000)# 创建苍井井角色
print
cang.detail()
fxq.detail()
cang2.detail()
cang3.detail()
print
cang.grass()
fxq.selfearn()
cang2.multiPlayer()
cang3.selfearn()
print
cang.detail()
fxq.detail()
cang2.detail()
cang3.detail()

