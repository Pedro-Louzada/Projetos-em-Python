# Funções
# Por exemplo: Bebidas = ('Cerveja, Refrigerante e Aguá')
# 1ªfunção: import(nome da variável)
# (Importaria todas as bebidas atribuídas a variável 'Bebida')
# from(bebidas(import('Cerveja'))) <- (Posso escolher qual delas vou importar)
#2ªfunção Math <- floor(arredondo p? baixo),
# ceil(arredonda p/ cima), trunc (elimina os números depois da vírgula)
# pow (potência), sqrt (raiz quadrada), factorial (fatorial)
# se quiser só uma delas, usar desta forma:
# from(math(import(sqrt)))
# import random (vou ter uma escolha aleatória)
# random.choice() <- escolhe um
# random.shuffle() <- coloca em ordem aleatória 
#Exemplo 1 -
import math
num1 = int(input('Digite um número: '))
raiz1 = math.sqrt(num1)
print('A raiz quadrada de {} é {}.'.format(num1,math.floor(raiz1))) #arredondou p/baixo
#Exemplo 2 -
from math import sqrt
num2 = int(input('Digite um número: '))
raiz2 = sqrt(num2)
print ('A raiz de {} é {}.'.format(num2,raiz2))