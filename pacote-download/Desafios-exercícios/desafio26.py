frase = str(input("Digite uma frase: ")).upper()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra A esta na posição {}.".format(frase.find("A")+1))
print('A última letra A esta na posição {}.'.format(frase.rfind("A")))
#rfind() procura a partir do lado direito