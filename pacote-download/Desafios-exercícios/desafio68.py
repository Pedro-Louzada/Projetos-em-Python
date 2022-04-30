from random import randint
print('-'*20)
print('Jogo do Pár ou Ímpar')
print('-'*20)
qtdVit = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    option = ' '
    while option not in 'PI':
        option = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Eu escolhi o número {computador} e você {jogador}, totalizando em {soma}.')
    if option == 'P':
        if soma % 2 == 0:
            print('Jogador ganhou!')
            qtdVit += 1
        else:
            print('Computador ganhou!')
            break
    elif option == 'I':
        if soma % 2 != 0:
            print('Jogador ganhou!')
            qtdVit += 1
        else:
            print('Computador ganhou!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você conseguiou ganhar {qtdVit} vezes.')
print('Até Logo!')



