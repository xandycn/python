# -*- coding: utf-8 -*-

#获取对象信息

print(type(123))
print(type('123'))
print(type(None))

print(type(abs))
print(type(a))

import types
def fn()
	pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(isinstance('a', str))
print(isinstance((1,2,2), (list, tuple))

print(dir('abc'))

class MyObject(object):
	def __init__(self)
		self.x = 9
	def power(self)
		return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
setattr(obj, 'y', 19)
print(getattr(obj, 'y'))

print(hasattr(obj, 'power'))
fnn = getattr(obj, 'power')
print(fn)
print(fn())


