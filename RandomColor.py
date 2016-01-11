### Random hex Color Generator 
import random 
#Creat list of total hexdigits for colors
letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
ColorGen = random.sample(letters, 6) # a variable that creat random 6 numbers from the letters list
Color = ''.join(ColorGen) #remove the spaces
hexColor = ('#'+Color)
print(hexColor)
