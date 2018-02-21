
#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/2/1 21:53
# @Author :FengXiaoqing
# @file   :test.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

# import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 画雪
#



# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 画彩虹
#


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 时钟
#

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='提交', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()



#!/usr/bin/env python
# Author : fengxiaoqing
# Date : 2018.02.04
import commands
import os
print ("hellow world!")
ls = commands.getoutput("df -h")
print(ls)
date = commands.getoutput("date +%F")
print(date)
with open("1.txt","ab") as df:
    df.write("############## start {0}  ########################".format(date))
    df.write(ls)
    df.write("\n")
    df.write("############## END ##########################")



