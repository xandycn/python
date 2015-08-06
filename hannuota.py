# -*- coding: utf-8 -*-
#汉诺塔问题求解


def move(n, A, B, C):
	if n==1:
		print(A, '->', C)
	else:
		move(n-1, A, C, B)
		move(1, A, B, C)
		move(n-1, B, A, C)

n = int(input('enter the number:'))
move(n,'A','B','C')