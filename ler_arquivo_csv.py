import csv

open_file = open('alunos.csv','r')
file_csv = csv.reader(open_file,delimiter=';')
for [data,nome,status] in file_csv:
    print('{} - {} - {}'.format(data,nome,status))