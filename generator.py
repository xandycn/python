# -*- coding: utf-8 -*-

#generator

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n=n+1
	return 'done'
	

fib = fib(6)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

for n in fib(6):
	print(n)