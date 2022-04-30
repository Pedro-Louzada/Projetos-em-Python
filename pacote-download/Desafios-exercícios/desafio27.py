n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()

print("Prazer em te conhece-lo(a)!\n")
print("Seu primeiro nome é {}.".format(nome[0]))
print("Seu último nome é {}.".format(nome[len(nome)-1]))


