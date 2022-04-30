from datetime import date
qtdmaior = 0
qtdmenor = 0
atual = date.today().year
for c in range (1,8):
    age = int(input('Digite seu ano de nascimento: '))
    ano = atual - age
    if ano >= 18:
        qtdmaior += 1
    else:
        qtdmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(qtdmaior))
print('E também tivemos {} pessoas menores de idade.'.format(qtdmenor))