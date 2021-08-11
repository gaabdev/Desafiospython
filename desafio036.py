#emprestimo bancario para compra de casa

casa = float(input('valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print('para pagar uma casa de R${:.2f} '.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))  
if prestacao <= minimo:
    print('emprestimo pode ser concedido!')
else:
    print(' NEGADO!!!')
