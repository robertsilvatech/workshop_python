lista_nomes = ['José','Pedro','Paulo','Antonio']
print(len(lista_nomes))
print('O nome informado é: {}'.format(lista_nomes[0]))
print('O nome informado é: {}'.format(lista_nomes[1]))

print('')
for nome in lista_nomes:
    print('O nome informado é: {}'.format(nome))

lista_numeros = []
print('')
for item in range(1,101):
    lista_numeros.append(item)

print(len(lista_numeros))
print(lista_numeros)
