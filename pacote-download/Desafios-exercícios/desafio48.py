s = 0
for c in range (1,501):
    if(c % 2 !=0 and c % 3 ==0):
        s += c
print('A soma dos números ímpares e múltiplos de 3 no intervalo entre 1 e 500 foi de {}.'.format(s))

#outra maneira de fazer ...

qtd = 0
soma = 0
for cont in range(1,501,2):#1-500 pulando de 2 em 2
    if(cont % 3 ==0):
        qtd += 1
        soma += cont
print('A soma dos números ímpares e múltiplos de 3 no intervalo entre 1 e 500 foi de {}.'.format(soma))
print('E a quantidade de números somados foi de {}.'.format(qtd))
