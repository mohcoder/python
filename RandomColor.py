# Random hex Color Generator
import random

# Create list of total hexdigits for colors
import webcolors
import bs4

letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
ColorGen = random.sample(letters, 6)  # a variable that create random 6 numbers from the letters list
Color = ''.join(ColorGen)  # remove the spaces
hexColor = str('#' + Color)
print(hexColor)

# rgb= hex_to_rgb(hexColor)
# print(rgb)
# print(webcolors.rgb_to_name(rgb, u'html4'))
import re

str = hexColor
match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str)

if match:
  print('Hex is valid')
  print(webcolors.hex_to_name(hexColor))
else:
  print('Hex is not valid')

# # print(webcolors.hex_to_name("#ffffff", u'css3'))
# c = input('he')
# print(webcolors.hex_to_name(c))
