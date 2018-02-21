#/usr/bin/env python
# -*- coding:utf-8 -*-
# @time   :2018/1/26 20:55
# @Author :FengXiaoqing
# @file   :JiuGongGe.py
number = list()
for i in range(1,10):
    number.append(i)

for A in number:
    a = list()
    for i in range(1,10):
        a.append(i)
    a.remove(A)
    for B in a :
        b = list()
        for i in a:
            b.append(i)
        b.remove(B)

        for C in b:
            c = list()
            for i in b:
                c.append(i)
            c.remove(C)

            for D in c:
                d = list()
                for i in c:
                    d.append(i)
                d.remove(D)

                for E in d:
                    e = list()
                    for i in d:
                        e.append(i)
                    e.remove(E)

                    for F in e:
                        f = list()
                        for i in e:
                            f.append(i)
                        f.remove(F)

                        for G in f:
                            g = list()
                            for i in f:
                                g.append(i)
                            g.remove(G)

                            for H in g:
                                h = list()
                                for i in g:
                                    h.append(i)
                                h.remove(H)

                                for I in h:
                                    if (A+B+C) == (D+E+F) == (G+H++I) == (A+D+G) == (B+E+H) == (C+F+I) == (A+E+I) == (C+E+G):
                                        print('''
                                        _____________
                                        |_{0}_|_{1}_|_{2}_|
                                        |_{3}_|_{4}_|_{5}_|
                                        |_{6}_|_{7}_|_{8}_|
                                        
                                        '''.format(A,B,C,D,E,F,G,H,I))



