from time import sleep
print('~'*10)
print('TABUADA')
print('~'*10)
while True:
    sleep(0.2)
    option = int(input('De qual número quer a tabuada: '))
    if option < 0:
        break
    print('-' * 30)
    for c in range(0, 11, 1):
        sleep(0.5)
        print(f'{option} x {c} = {option*c}')
    print('-' * 30)
sleep(0.2)
print('Até Logo!')


