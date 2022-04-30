from random import randint
from time import sleep
computador = randint(0,10)
sleep(0.5)
print('Irei sortear um número de 0 à 10...')
sleep(1)
print('Será que você consegue acertar? ')
right = False
palpite = 0
while not right:
    sleep(1)
    jogador = int(input('Qual seu palpite: '))
    palpite += 1
    sleep(0.5)
    print('Processando...')
    sleep(0.5)
    if jogador == computador:
        right = True
    else:
        if jogador < computador:
            print('Mais... Tente Novamente.')
        else:
            print('Menos... Tente Novamente.')
print('Parabéns você acertou com {} tentativas.'.format(palpite))

