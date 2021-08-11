nome = str(input('DIGITE SEU NOME: '))
altura = float(input('DIGITE A SUA ALTURA: '))
altura_min = 1.70
if altura < altura_min:
    print('Sr.{}, você não poderá entrar para o exercito'.format(nome))
else:
    print('PARABÉNS SR. {}, você poderá se alistar no exercito'.format(nome))