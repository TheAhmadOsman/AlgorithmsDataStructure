class Student:
	def __init__(self, init_name):
		self._name = init_name						#If anything starts with '_', it means a private variable and should not be used

	def get_name(self):
		return self._name

	def set_name(self, new_name):
		self._name = new_name

	def __str__(self):
		return 'Hi, I\'m ' + self._name

	def __eq__(self, other):							#Without this, Python compares memory addresses(id)
		return self._name == other.get_name()

	#Python Magic Functiins
	#def __gt__ for greater than
	#def __lt__ for less than
	#def __ge__ for greater than or equal
	#def __lc__ for less than or equal
	#def __rer__ for how the object should be represented -> search for this

	def __add__(self, other):
		#return self._name + ', ' + other.get_name()
		#return [self._name, other.get_name()]
		if isinstance(other, Student):										#Checking if something is of a certain type
			#return [self._name, other.get_name()]
			return Student(self._name + ' ' + other.get_name())
		else:
			print("don't do this")

s = Student('Alice')
print(s)

s._name = 'Ahmad'

print(s)
print(s._name)

print(s.get_name())

s.set_name("Khaled")
print(s)

s2 = Student("Ahmad")

print(s==s2)

print(s+s2)

s3 = Student("Magdy")

print(s+s2+s3)