minha_tupla = () # Tupla vazia
meu_dicionario = {} # Dicionario Vazio
meu_conjunto = set() # Conjunto Vazio.


print('Tupla')
minha_tupla = ('Robert', 'Pedro', 'Paulo')
print(minha_tupla)
print(minha_tupla[1])
for nome in minha_tupla:
    print(nome)
print('')

print('Dicionario')
meu_dicionario = {'nome': 'José', 'idade': 27}
print(meu_dicionario['nome'])
print(meu_dicionario['idade'])
meu_dicionario['idade'] = 28
print(meu_dicionario['idade'])
meu_dicionario['status'] = 'Ativo'
print(meu_dicionario)
lista_notas = [7.8, 8.4, 8.7, 4.5]
meu_dicionario['notas'] = lista_notas
print(meu_dicionario)
print(meu_dicionario['notas'])
print('')

print('Conjunto')
nomes = ['Robert', 'Pedro', 'Paulo', 'Robert','Ana','Joana','Maria','Ana'] # Lista
print(nomes)
meu_conjunto = set()
for nome in nomes:
    meu_conjunto.add(nome)

print(meu_conjunto)
