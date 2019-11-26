'''
aluno = 'Pedro'
nota1 = 10
nota2 = 5
nota3 = 7
nota4 = 10
media = (nota1+nota2+nota3+nota4)/4
print(media)
'''

# Criando um método (sem return)
def calcula_media(nome, nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4)/4
    print('A media do aluno: {} é: {}'.format(nome,str(media)))

media_paulo = calcula_media('Paulo', 4, 3, 10, 10)
media_mauricio = calcula_media('Mauricio', 7, 8, 7, 8)

print('')
print('Exemplo de função com return')
print('')

# Exemplo de função (com return)
def calcula_media2(nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4)/4
    return media

def verifica_media(nome, nota1, nota2, nota3, nota4):
    status = ['Aprovado','Reprovado']
    media_final = calcula_media2(nota1,nota2, nota3, nota4)
    if media_final >= 7:
        print('O aluno {} foi {}'.format(nome, status[0]))
    else:
        print('O aluno {} foi {}'.format(nome,status[1]))
    
media_paulo = verifica_media('Paulo', 4, 5, 10, 10)

