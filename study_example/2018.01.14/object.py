#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/14 20:19
# @Author :FengXiaoqing
# @file   :object.py

class person(object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def shangshan(self):
        print ("%s,%s岁,%s,上山去砍柴.") % (self.name,self.age,self.sex)

    def kaiche(self):
        print ("%s,%s岁,%s,开车去东北.") % (self.name,self.age,self.sex)

    def baojian(self):
        print ("%s,%s岁,%s,最爱大保健.") % (self.name,self.age,self.sex)

xiaoming = person('小明',10,'男')
xiaoming.shangshan()
xiaoming.kaiche()
xiaoming.baojian()
print

laoli= person('老李',90,'男')
laoli.shangshan()
laoli.kaiche()
laoli.baojian()