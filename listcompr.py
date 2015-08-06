# -*- coding: utf-8 -*-

a = [x*x for x in range(1, 11) if x%2 ==0]
b = [m+n for m in 'ABC' for n in 'XYZ']

L1 = ['Hello', 'World', 15, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]

print(L2)