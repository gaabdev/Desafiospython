num = int(input('DIGITE UM NÚMERO INTEIRO: '))
num2 = int(input('DIGITE OUTRO NÚMERO INTEIRO: '))
if num > num2:
    print('O numero {} é maior que {}'.format(num, num2))
elif num < num2:
    print('o numero {} é maior que {}'.format(num2, num))
else:
    print('não existe valor maior, os dois são iguais!!!')