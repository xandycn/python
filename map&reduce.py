# -*- coding: utf-8 -*-

from functools import reduce

L1 = ['adam', 'LISA', 'barT']
def normalize(name):
	return name.capitalize()

L2 = map(normalize, L1)
print(list(L2))

def prod(L):
	def cheng(x, y):
		return x*y
	return reduce(cheng, L)

print(prod([3,4,4,4]))


def str2float(s):
	def fn(x, y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	temp = s.split('.')
	int_num = reduce(fn,map(char2num,temp[0]))
	l = len(temp[1])
	float_num = reduce(fn,map(char2num,temp[1]))/(10**l)
	return int_num+float_num
	
print(str2float('2432.436543'))