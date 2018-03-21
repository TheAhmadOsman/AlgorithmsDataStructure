class Course:
	def __init__(self, id_, dept_, number_, semester_, year_, section_, title_):		#the underscore is after to show that it is an external parmeter
		self._id = id_
		self.-..	###Keep going


#Make a course instanse and print it, what is printed?

#write a __str__ method
#get_semester and set_semester

semester = property(get_semester, set_semester) #first gets, second assigns - called decorator #It takes, getter, setter, deleter in this order

my_course.semester will allow you to use that one above

Another way

	@property
	def semester(self):
		return

	@semester.setter
	def set_semester(self, new_value_):
		if new_value_ in ['FA', 'JT', 'SP', 'SU']:
			self._semester = new_value_
		else:
			raise ValueError('Bad!')

try:
	my_course.semester = 'Hello'
except:
	print('there was a problem')

try:
	my_course.semester = 'Hello'
except ValueError as e:
	print('there was a problem')
	print(e)

x=int(input())
try:
	print(1/x)
except:
	print('ooops')
finally: #this gets printed if everything is successful
	print("Yaaay")