nomeDaCidade = str(input("Digite o nome de sua cidade:\n"))
separaNome = nomeDaCidade.split()
if (separaNome[0]) == "Santo":

    print("O primeiro nome da cidade é Santo!")

else:
    print("O primeiro nome da cidade não é Santo!")

#forma de resolução sme condicional

cid = str(input("Em que cidade você nasceu?\n")).strip()
print(cid[0:5].upper() == "SANTO")

