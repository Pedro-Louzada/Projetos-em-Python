frase = str(input('Digite uma frase: ')).strip().upper()#.strip tira os espaços antes e depois da palavra
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

'''Podemos fazer criando a variável inverso e aderindo a ela o seguinte requisíto:
inverso = junto[::-1]'''