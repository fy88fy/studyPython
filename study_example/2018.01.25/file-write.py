#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/25 20:25
# @Author :FengXiaoqing
# @file   :file-write.py



class File():
    ENCODING = "utf-8"
    def wirteFile(self):
        filename = input("Please input the file name: ")
        f = open(filename,'w',encoding=File.ENCODING)
        while 1:
            context = input("Please input the file context: ")
            if context == "EOF":
                break
            f.write(context)
            f.write("\n")

    def readFile(self):
        print("####################STAT######################")
        readfile = input("Please input your read file name: ")

        fileread = open(readfile,encoding=File.ENCODING)
        readContext = fileread.read()
        print(readContext)
        print("################### END ######################")
        fileread.close()

if __name__ == '__main__':
    import codecs
    File = File()
    File.wirteFile()
    File.readFile()
