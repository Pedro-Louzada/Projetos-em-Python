from math import pow

print('=-'*5, 'IMC', '=-'*5)

peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))

imc = peso / pow(altura,2)

print('O IMC desta pessoa é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('Cuidado, você esta abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Parabéns, você esta no Peso Ideal.')
elif 25 <= imc < 30:
    print('Cuidado, você esta com Sobrepeso.')
elif 30 <= imc < 40:
    print('Cuidado, você esta na Obesidade.')
elif imc >= 40:
    print('Cuidado, você esta na Obesidade Mórbida!')


