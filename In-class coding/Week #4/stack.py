'''
Stack ADT(Abstract Data Type)
stack()
peek() last element looked at
len()/size()
push()
pop() last element removed
is_empty()
'''

class Stack():
	def __init__(self):
		self._items = []

	def push(self, new_item_):
		self._items.append(new_item_)

	def peek(self):
		if len(self._items) >= 1:
			return self._items[-1]
		else:
			raise IndexError("The stack is empty!")

	def __len__(self):
		return len(self._items)

	def size(self):
		return len(self._items)

	def pop(self):
		if len(self._items) >= 1:
			return self._items.pop()
		else:
			raise IndexError("The stack is empty!")

	def is_empty():
		return len(self_items) == 0

s = Stack()
s.push(52)
print(s.peek())
print(s.pop())

try:
	print(s.peek())
except IndexError as ie:
	print('Ooops!')
	print(ie)