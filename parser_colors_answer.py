'''
Imprimir nome da cor
'''
import json

file_open = open('colors.json')
file = json.load(file_open)

for color in file['colors']:
    print(color['color'])
