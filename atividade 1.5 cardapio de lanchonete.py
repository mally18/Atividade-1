print('================================= \n| COD |     PRODUTO     | VALOR | \n| 100 | Cachorro quente | 1,20R$| \n'
      '| 101 | Bauru Simples   | 1,30R$|\n| 102 | Bauru com ovo   | 1,50R$|\n| 103 | Hamburguer      | 1,20R$| \n'
      '| 104 | Chessburguer    | 1,70R$|\n| 105 | Suco            | 2,20R$| \n| 106 | Refrigerante    | 1,00R$|\n'
      '=================================\n Para sair digite 999')
total = 0
while True:
    q = int(input('Informe o codigo: '))
    if(q == 999):
        break
    qtd = int(input('Informe a quantidade: '))
    if q == 100:
        total = 1.20 * q
    elif q == 101:
        total = 1.30 * q
    elif q == 102:
        total = 1.50 * q
    elif q == 103:
        total = 1.20 * q
    elif q == 104:
        total = 1.70 * q
    elif q == 105:
        total = 2.20 * q
    elif q == 106:
        total = 1 * q
    else:
        print('Codigo invalido')
print(total, 'reais')
