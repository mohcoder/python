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
        return round((self.x / self.y), 4)

    def subs(self):
        return self.x - self.y


class ScientificCalc(Calc):
    def power(self):
        return round(pow(self.x, self.y), 3)

    def x_root(self):
        return round(math.sqrt(x), 2)

    def y_root(self):
        return round(math.sqrt(y), 2)

    def x_fact(self):
        return round(math.factorial(x), 2)

    def y_fact(self):
        return round(math.factorial(y), 2)


num = ScientificCalc(x, y)
print('======================')
print('{} + {} = {} '.format(x, y, num.add()))
print('======================')
print('{} * {} = {} '.format(x, y, num.multiple()))
print('======================')
print('{} / {} = {} '.format(x, y, num.divide()))
print('======================')
print('{} - {} = {} '.format(x, y, num.subs()))
print('======================')
print('{} ^ {} = {} '.format(x, y, num.power()))
print('======================')
print('Square of {} = {} '.format(x, num.x_root()))
print('======================')
print('Square of {} = {} '.format(y, num.y_root()))
print('======================')
print('Factorial number of {} = {} '.format(x, num.x_fact()))
print('======================')
print('Factorial number of {} = {} '.format(y, num.y_fact()))
print('======================')
