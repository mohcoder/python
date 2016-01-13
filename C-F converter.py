# @ author(Mohammed Zaher)
# @ email (moh.zaher.coder@gmail.com)
# @ copyrights 2016

temp = 0


def tempconverter():
    print('''Welcome to Python Temperature Converter
============================================================
|| Please Choose "C" to convert from Fahrenheit to Celsius ||
|| Please Choose "F" to convert from Celsius to Fahrenheit ||
============================================================''')
    choice()


def choice():
    valid = ['c', 'f']
    while True:
        userChoice = str(input('What Would You Like To Do?... ')).lower()
        if userChoice in valid:
            inputCheck(userChoice)
            break
        else:
            print('Sorry But Your Choice is not valid ... Try Again')


def inputCheck(userChoise):
    if userChoise == 'c':
        return celsiusFunction()
    if userChoise == 'f':
        return fahrenheitFunction()


def fahrenheitFunction():
        temp = float(input('Please, Enter the Celsius temperature: '))
        result = round((1.8 * temp) + 32, 2)
        fahrenheit = 'Temp. is : %s \u2109' % result
        print('===========================')
        print(fahrenheit)
        print('===========================')
        print('Thank you for using Python Temp Converter \u00A9')


def celsiusFunction():
    temp = float(input('Please, Enter the Fahrenheit temperature: '))
    result = round((5.0 / 9.0) * (temp - 32), 2)
    celsius = 'Temp. is : %s \u2103' % result
    print('===========================')
    print(celsius)
    print('===========================')
    print('Thank you for using our converter')

tempconverter()