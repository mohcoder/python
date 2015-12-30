a = int(input('num1: '))
b = int(input('num2: '))


class Calc:
	def __init__(self, a, b):
			self.a = a
			self.b = b

	def add(self):
		return self.a + self.b

	def multiple(self):
		return self.a * self.b

	def divide(self):
		return self.a / self.b

	def subs(self):
		return self.a - self.b
num = Calc(a, b)
print('{} + {} = {} '.format(a,b,num.add()))
print('{} * {} = {} '.format(a,b,num.multiple()))
print('{} / {} = {} '.format(a,b,num.divide()))
print('{} - {} = {} '.format(a,b,num.subs()))