soma = 0
maiorIdade = 0
nomeHomem = ''
qtdMulher = 0
for c in range (1,5):
    print('-'*5,'{}ª PESSOA'.format(c),'-'*5)
    name = str(input('Digite seu nome: ')).strip()
    age = int(input('Digite sua idade: '))
    genre = str(input('Digite M se for homem ou F se for mulher: ')).strip()
    soma += age
    media = soma / 4
    if c == 1 and genre in 'Mm':
        maiorIdade= age
        nomeHomem = name
    if genre in 'Mm' and age > maiorIdade:
        maiorIdade = age
        nomeHomem = name
    if genre in "Ff" and age < 20:
        qtdMulher += 1
print('A média das idades foi de {:.1f}'.format(media))
print('O homem mais velho tem {} anos e ele se chama {}.'.format(maiorIdade, name))
print('A quantidade de mulheres menores que 20 anos totalizou em {} mulheres.'.format(qtdMulher))