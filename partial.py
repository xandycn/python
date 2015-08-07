# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

print(int2('10000'))

max2 = functools.partial(max, 10)

print(max2(2,3,5))