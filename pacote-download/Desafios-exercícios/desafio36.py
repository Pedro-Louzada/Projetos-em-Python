print ('=-'*5, 'Aprovador de Saldo Bancário', '=-'*5)

valorCasa = float(input('Informe o valor de sua casa: '))
salario = float(input('Informe seu salario mensal: '))
tempAnos = float(input('Quantos anos gastará para pagar a casa: '))

tempMeses = tempAnos * 12
prestacaoMensal = valorCasa / tempMeses

if prestacaoMensal > ((salario*0.3)+salario):
    print('EMPRÉSTIMO NÃO APROVADO!')
elif prestacaoMensal == ((salario*0.3)+salario):
    print('EMPRÉSTIMO VÁLIDO!')
else:
    print('EMPRÉSTIMO VÁLIDO!')