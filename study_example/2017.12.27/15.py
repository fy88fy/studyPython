#!/usr/bin/python
sth=''
while sth != 'q':
    print 'hellow'
    sth=raw_input("please input sth,q for exit.")
    if not sth:
        break
    if sth == 'quit':
        continue
    print 'continue'
else:
         print 'world'