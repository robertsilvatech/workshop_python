try:
    arquivo = open('tentativa.txt')
    print('Arquivo aberto')

    def imprimi_algo():
        pass

    print('Ok')
except Exception as err:
    print('Não foi possível abrir o arquivo')
    print('Erro: {}'.format(err))



