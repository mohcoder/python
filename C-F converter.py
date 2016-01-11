temp = 0


def tempconverter():
    print('Welcome to Celsius - Fahrenheit Converter')
    print('=========================================')
    print('Please Choose "C" to convert from Fahrenheit to Celsius')
    print('Please Choose "F" to convert from Celsius to Fahrenheit')
    print('=========================================')
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
        temp = float(input('Please, Enter the Fahrenheit temperature: '))
        result = round((5.0 / 9.0) * (temp - 32), 2)
        celsius = '%s \u2103' % result
        print(celsius)
        print('Thanks for using our converter')
    if userChoise == 'f':
        temp = float(input('Please, Enter the Celsius temperature: '))
        result = round((1.8 * temp) + 32, 2)
        fahrenheit = '%s \u2109' % result
        print(fahrenheit)
        print('Thanks for using Python Temp Converter \u00A9')


tempconverter()