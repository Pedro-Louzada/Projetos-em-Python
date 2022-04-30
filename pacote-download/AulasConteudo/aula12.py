#estrtura condicional aninhada (dentro de ninhos)
nome = str(input('Digite seu nome: '))
if nome == 'Pedro':
    print('Que nome bonito!')
elif nome== 'Maria' and 'João':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal.')
print('Seja bem vindo {}.'.format(nome))
