import math
x = int(input('num1: '))
y = int(input('num2: '))

class Calc:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self):
		return self.x + self.y

	def multiple(self):
		return self.x * self.y

	def divide(self):
		return self.x / self.y

	def subs(self):
		return self.x - self.y


class ScientificCalc(Calc):
	def power(self):
		return pow(self.x, self.y)

	def x_root(self):
		return math.sqrt(x)

	def y_root(self):
		return math.sqrt(y)

	def x_fact(self):
		return math.factorial(x)

	def y_fact(self):
		return math.factorial(y)

num = ScientificCalc(x, y)

print('{} + {} = {} '.format(x, y, num.add()))
print('{} * {} = {} '.format(x, y, num.multiple()))
print('{} / {} = {} '.format(x, y, num.divide()))
print('{} - {} = {} '.format(x, y, num.subs()))
print('{} ^ {} = {} '.format(x, y, num.power()))
print('Square of {} = {} '.format(x, num.x_root()))
print('Square of {} = {} '.format(y, num.y_root()))
print('Factorial number of {} = {} '.format(x, num.x_fact()))
print('Factorial number of {} = {} '.format(y, num.y_fact()))