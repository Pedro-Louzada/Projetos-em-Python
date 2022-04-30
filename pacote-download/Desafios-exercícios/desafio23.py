print("-"*5+"Desafio23"+"-"*5)
print("-"*5+"Executando com strings"+"-"*5)

num = int(input("Coloque qualquer numero de 0 a 9999: \n"))
n = str(num) #vai estar trasnformando a variável int em string

print("Analisando o número {} ...".format(num))
print("Unidade: {}".format(n[3]))
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))

print("-"*5+"Executando com inteiros"+"-"*5)

num = int(input("Coloque qualquer numero de 0 a 9999: \n"))
# // <- divisao exata sem número decimal
u = num // 1 % 10 # o resto da divisao exata será a unidade
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
# pegar o resto da divisão por 10 no final, te trará a última casa do número
print("Analisando o número {} ...".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))





