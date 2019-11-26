file = open('lista_alunos.txt','r')
alunos = file.readlines()
for aluno in alunos:
    print(aluno.replace('\n',''))