salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    aumento = (salario * 0.1) + salario
    print('Seu aumento foi de 10% e seu salário foi para R${}.'.format(aumento))
if salario <= 1250:
    aumento = (salario * 0.15) + salario
    print('Seu aumento foi de 15% e seu salário foi para R${}.'.format(aumento))
