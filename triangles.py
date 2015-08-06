# -*- coding: utf-8 -*-

def triangles():
    L=[1];
    while(True):
        yield L;
        L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1];
		
for n in triangles():
	print(L)