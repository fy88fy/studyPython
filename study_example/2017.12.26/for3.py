#!/usr/bin/python
# date:2017.12.26
# Author:fengxiaoqing

jia=('a','b','c')
yi=('x','y','z')
for i in jia:
    for j in yi:
        if i == 'a' and  not j == 'x':
           if i == 'c' and j not == 'x' :
                print "%s----%s" % (i,j)
            if i == 'c' and j not == 'z' :
                print "%s----%s" % (i, j)
