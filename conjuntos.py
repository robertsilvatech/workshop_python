print('Conjunto')

turma = ['Robert','Paulo','Mauricio','Daniel','Hygor','Marcelo','Arthur']
print('Turma: {}'.format(turma))
print('Tipo do objeto turma: {}'.format(type(turma)))
conjunto_turma = set()
for aluno in turma:
    conjunto_turma.add(aluno) # Adicionando elemento no conjunto turma
print('Alunos da turma: {}'.format(conjunto_turma))
print('Tipo do objeto conjunto_turma: {}'.format(type(conjunto_turma)))

conjunto_turma.discard('Daniel')
print(conjunto_turma)