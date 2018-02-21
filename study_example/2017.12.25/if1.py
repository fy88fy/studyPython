#!/usr/bin/env python
x = int(raw_input("Please input First number: "))
y = int(raw_input("Please input second number: "))
z = int(raw_input("Please input Three number: "))
list =(x,y,z)
x=list[0]
y=list[1]
z=list[2]
if x <  y  and x < z :
    if y < z :
        print "%s<%s<%s" % (x,y,z)
    else:
        print "%s<%s<%s" % (x,z,y)
elif x < y and x > z:
        print "%s<%s<%s" % (z,x,y)
elif  x >y and x <z:
        print "%s<%s<%s" % (y,x,z)
elif x> y  and x > z:
    if y>z:
        print "%s<%s<%s" % (z,y,x)
    else:
        print "%s<%s<%s" % (y,z,x)
print "END"