#!/usr/bin/python
# date:2017.12.26
# Author:fengxiaoqing
i=0
num=(1,2,3,4)
for x in  num:
   for y in num:
       for z in num:
           if x != y and  x != z and  y != z :
                print x*100+y*10+z
                i=i+1
print "the total num is :%s" % i


