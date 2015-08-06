# -*- coding: utf-8 -*-

def is_palindrome(n):
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	
	n = str(n)
	number = list(map(char2num, n))
	l = len(n)-1
	a = 0
	while a<l:
		if number[a] == number[l-a]:
			a=a+1
		else:
			return False
	return True
	
output = filter(is_palindrome, range(1, 1000))
print(list(output))