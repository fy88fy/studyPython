#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/6 16:55
# @Author :FengXiaoqing
# @file   :test.py
# macaddr = '02:42:0e:31:98:4a'
# prefix_mac =macaddr[:-2]
# last_t = macaddr[-2]
#
# last_two = macaddr.split(':')[-1]
# print last_two
# plus_one = int(last_two,16) + 1
# print plus_one
# last_one = hex(plus_one)[-3:]
# end_two = last_one[0]+last_one[2]
# print prefix_mac.upper()+str(end_two).upper()


macaddr = '02:42:0e:31:98:0a'
prefix_mac = macaddr[:-2]   # 取出前缀：02:42:0e:31:98:
last_two = macaddr[-2:] # 取出最后2位：
plus_one = int(last_two,16)+1  # 16进制转换成10f进制加1 生成下一个MAC的最后两位。
if plus_one in range(10):       # 如果最后两位是0,1,2,3,4,...9
    new_last_two = hex(plus_one)[2:]    # 10进制转换成16进制，取最后位6
    new_last_two = '0' + new_last_two   # 把生成的新的最后一位前面加0
else:
    new_last_two = hex(plus_one)[2:]
    if len(new_last_two) == 1:    #如果下是0a p这种情况。把生成的结果前加0
    	new_last_two = '0' +new_last_two
new_mac = prefix_mac + new_last_two
print new_mac.upper()      #把mac转换成大写