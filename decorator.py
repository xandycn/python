# -*- coding: utf-8 -*-

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*arg,**kw):
		print('begin call')
		f = func(*arg, **kw)
		print('end call')
		return f
	return wrapper

@log
def now():
	print('中间')
	return 1
	
now()
