'''
Sistem de calculo de IMC
'''
altura = float(input('Digite sua altura (1.72):'))
peso = float(input('Digite seu peso (72):'))

imc = peso / (altura**2)
# ** = operador de potencia
imc = round(imc,2)

if imc >= 16 and imc <= 16.9:
    print('Muito abaixo do peso - {}'.format(imc))
elif imc >= 17 and imc <= 18.4:
    print('Abaixo do peso - {}'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal - {}'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('Acima do peso - {}'.format(imc))
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau I - {}'.format(imc))
elif imc >= 35 and imc <= 40.00:
    print('Obesidade Grau II - {}'.format(imc))
elif imc > 40:
    print('Obesidade Grau III - {}'.format(imc))
else:
    print('Padrão não encontrado')
