'''
Data Structure
Organized Data
	Sort
	Arrange
	Iterate
	Add
	Read

'''

class Box:
	def __init__(self, init_length_, init_width_, init_height_):
		self._length = init_length_
		self._width = init_width_
		self._height = init_height_

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, new_height_):
		self._height = new_height_

	def __str__(self):
		return "Box's heiht is: " + str(self._height)

b = Box(1, 2, 3)
print(b)
b.height = 4
print(b)