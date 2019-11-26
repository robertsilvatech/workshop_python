notas = [] # Declando uma lista vazia.
notas = [7.0, 8.5, 8.4, 3.0]
print('Acessando indices.')
print('Lista completa: {}'.format(notas))
print('Acessando primeiro indice: {}'.format(notas[0]))
print('Acessando o ultimo indice: {}'.format(notas[-1]))

print('')
print('Operacoes com listas')
notas.append(9.2) # Adicionando elemento da lista.
print(notas)
notas.remove(3.0) # Removendo elemento da lista.
print(notas)
notas.insert(3, 8.5) # Inserindo o elemento no indice 3 da lista
print(notas)
notas[0] = 9.8 # Alterando o valor do indice 0
print(notas)

print('')
print('Funções utulizadas com listas')
print('Tamanho da lista: {}'.format(len(notas)))
print('Quantidade de elementos 8.5 que estão na lista: {}'.format(notas.count(8.5)))


