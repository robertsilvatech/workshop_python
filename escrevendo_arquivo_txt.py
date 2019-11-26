alunos = ['Paulo','Mauricio','Daniel','Arthur','Hygor','Marcelo']
file = open('lista_alunos.txt','w')
for aluno in alunos:
    file.write(aluno + '\n')

