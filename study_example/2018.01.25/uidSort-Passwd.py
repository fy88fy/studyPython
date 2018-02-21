#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/25 22:11
# @Author :FengXiaoqing
# @file   :uidSort-Passwd.py
import codecs
file = "passwd.txt"
sortfile = "sortpasswd.txt"
fileContext = []
sortuid = []
with codecs.open(sortfile,'wb') as fsort:
        with codecs.open(file,encoding='utf-8') as f:
            fileContext += f.readlines()
            for line in fileContext:
                sortuid.append(int(line.split(':')[2]))
            sortuid.sort()
            for uid in sortuid:
                for line in fileContext:
                    if str(uid) == line.split(":")[2]:
                        print(line)
                        fsort.write(line.encode("utf-8"))


