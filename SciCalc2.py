import math


def calc():
    choice()


print(''' Welcome to Python3 Scientific Calculator
''')

x = int(input('num1: '))
y = int(input('num2: '))


def choice():
    valid = ['+','-','x','/','p', 's', 'f']
    while True:
        userChoice = input('Please, Enter Operation (+, -, x, /, p for power, f for factorial, s of square root):  ')
        if userChoice in valid:
            inputCheck(userChoice)
            break
        else:
            print('Sorry But Your Choice is not valid ... Try Again')
       
            
def inputCheck(userChoice):
    if userChoice == '+':
        print(num.add())
    elif userChoice == '-':
        print(num.subs())
    elif userChoice == 'p':
        print(num.power())
    elif userChoice == '/':
        print(num.divide())
    elif userChoice == 's':
        print(num.sqrroot())
    elif userChoice == 'f':
        print(num.fact())

class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return ('%s + %s = %s' % (x, y, (self.x + self.y)))

    def multiple(self):
        result = round((self.x * self.y), 3)
        return ('%s * %s = %s' % (x, y, result))

    def divide(self):
        result1 = round((self.x / self.y), 3)
        result2 = round((self.y / self.x), 3)
        return (('%s / %s = %s' % (x, y, result1))) + '\n' + (('%s / %s = %s' % (y, x, result2)))

    def subs(self):
        return ('%s - %s = %s' % (x, y, (self.x - self.y)))
    
    def power(self): 
        return ('%s Power %s = %s'% (x, y,  (round(pow(self.x, self.y), 3)))) + '\n' + ('%s Power %s = %s'% (y, x,  (round(pow(self.y, self.x), 3))))

    def sqrroot(self):
        return ('Square Root of %s = %s'% (x, (round(math.sqrt(x), 3)))) + '\n' + ('Square Root of %s = %s'% (y, (round(math.sqrt(y), 3))))

    def fact(self):
        return ('Factorial of %s = %s'% (x, (math.factorial(x)))) + '\n' + ('Factorial of %s = %s'% (y, (math.factorial(y))))

num = Calc(x, y)

calc()

# print('======================')
# print('%s + %s = %s ' % (x, y, num.add()))
# print('======================')
# print('{} * {} = {} '.format(x, y, num.multiple()))
# print('======================')
# print('{} / {} = {} '.format(x, y, num.divide()))
# print('======================')
# print('{} - {} = {} '.format(x, y, num.subs()))
# print('======================')
# print('{} ^ {} = {} '.format(x, y, num.powerx()))
# print('======================')
# print('Square of {} = {} '.format(x, num.x_root()))
# print('======================')
# print('Square of {} = {} '.format(y, num.y_root()))
# print('======================')
# print('Factorial number of {} = {} '.format(x, num.x_fact()))
# print('======================')
# print('Factorial number of {} = {} '.format(y, num.y_fact()))
# print('======================')
