# signle underscore represents the last output.
# Using single underscore in a function means I don't wanna use it

import random


class Fruit:  # Super class

    def __init__(self, colors_, price_=0.99):
        self._color = colors_
        self._price = price_

    def __str__(self):
        return "costs " + str(self._price)


class Apple(Fruit):  # Sub Class

    def __init__(self, color_, price_, variety_):
        super().__init__(color_, price_)
        self._variety = variety_

    def make_a_pie(self):
        return "Tasty pie"

    def __str__(self):
        return 'This ' + self._color + ' ' + self._variety + ' apple ' + super().__str__()


class Orange(Fruit):

    def __init__(self, color_, price_, origin_):
        super().__init__(color_, price_)
        self._origin = origin_

    def make_juice(self):
        return "Tasty juice"

    def __str__(self):
        return 'This ' + self._color + ' ' + self._origin + ' orange ' + super().__str__()


f = Apple('Red', 0.50, 'Honey Crisp')
print(f)
print(f.make_a_pie())

o = Orange('Orange', 1.00, 'Iowa')
print(o)
print(o.make_juice())
