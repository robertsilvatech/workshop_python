import csv

create_file = open('escrita.csv', 'w', newline='',encoding='utf-8')
write = csv.writer(create_file,delimiter=';')
header = ['Nome','Idade', 'Situacao']
write.writerow(header)

funcionario1 = ['Jose', '25', 'Ativo']
print('Escrevendo linha 1')
write.writerow(funcionario1)
print('Escrevendo linha 2')
funcionario2 = ['Antonio', '55', 'Aposentado']
write.writerow(funcionario2)
print('Escrevendo linha 3')
funcionario3 = ['Paulo', '51', 'Ativo']
write.writerow(funcionario3)

create_file.close()