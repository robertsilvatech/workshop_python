'''
Imprimir o Titulo
Imprimir o Ano
Imprimit o Generos
Imprimir os Atores
Imprimir o Idioma
'''

import json

file_open = open('movie.json')
file = json.load(file_open)

titulo = file['Title']
print(titulo)
ano = file['Year']
print(ano)
generos = file['Genre']
generos = ','.join(generos)
print(generos)
atores = file['Actors']
atores = ','.join(atores)
print(atores)
idioma = file['Language']
print(idioma)
