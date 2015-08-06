# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
	x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x1,x2

a = float(input('a的值:'))
b = float(input('b的值:'))
c = float(input('c的值:'))
(x1,x2) = quadratic(a,b,c)
print('解为：%f , %f' %(x1,x2))