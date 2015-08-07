class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.score = score
	def print_score(self):
		print('%s:%s' % (self.__name, self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
		
		
bart = Student('doubi', 87)
bart.print_score()
print(bart.get_grade())

print(bart._Student__name)	#强行访问
print(bart.score)
print(bart.__name)	#私有对象，不能在外部访问