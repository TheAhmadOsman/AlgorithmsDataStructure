# signle underscore represents the last output.
#Using single underscore in a function means I don't wanna use it

import random

class Fruit:
	def __init__(self, name_type_, colors_, price_=0.99):
		self._color = random.choice(colors_)
		self._price = price_

	def ripe(self):
		self._color = "red"

	@property
	def color(self):
		return self._color

	def discount(self):
		self._price = 0.12 * self._price
		return self._price

	def __str__(self):
		return self._color + ' ' + self._name_type + ' is ' + str(self._price)

f = Fruit('Apple', ['Green', 'Yellow', 'Orange',])
print(f)

f.ripe()
print(f)

print(f.discount())
print(f)