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
        print(num.powerx())
        print(num.powery())
    elif userChoice == '/':
        print(num.divide())
    elif userChoice == 's':
        print(num.x_root())
        print(num.y_root())
    elif userChoice == 'f':
        print(num.x_fact())
        print(num.y_root())
   

class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return ('%s + %s = %s' % (x, y, (self.x + self.y)))

    def multiple(self):
        return ('%s * %s = %s' % (x, y, (self.x * self.y)))

    def divide(self):
        return (('%s / %s = %s' % (x, y, (self.x / self.y))))

    def subs(self):
        return ('%s - %s = %s' % (x, y, (self.x - self.y)))
    
    def powerx(self):
        return ('%s Power %s = %s'% (x, y,  (pow(self.x, self.y))))
    
    def powery(self):
        return ('%s Power %s = %s'% (y, x,  (pow(self.y, self.x))))
        
    def x_root(self):
        return ('Square Root of %s = %s'% (x, (math.sqrt(x))))

    def y_root(self):
        return ('Square Root of %s = %s'% (y, (math.sqrt(y))))

    def x_fact(self):
        return ('Factorial of %s = %s'% (x, (math.factorial(x))))

    def y_fact(self):
        return ('Factorial of %s = %s'% (y, (math.factorial(y))))


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
