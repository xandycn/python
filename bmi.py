# -*- coding: utf-8 -*-

#BMI指数计算

height = float(input('请输入你的身高（单位：米）：'))
weight = float(input('请输入你的体重（单位：千克）：'))

bmi = weight/height**2
if bmi < 18.5:
	output = '过轻'
elif bmi < 25:
	output = '正常'
elif bmi < 28:
	output = '过重'
elif bmi < 32:
	output = '肥胖'
else:
	output = '严重肥胖'

print('BMI指数为%.2f,%s' % (bmi,output))
