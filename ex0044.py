ValorTotal = float(input('Preço das compras: '))
descontoPIX = ValorTotal * 0.9
descontoCard = ValorTotal * 0.95
cartao = ValorTotal * 1.03
cartaoJ = ValorTotal * 1.07



print('Qual a forma de pagamento? \n'
      '[1] Á vista no dinheiro \n'
      '[2] Á vista no cartão \n'
      '[3] 2x no cartão \n'
      '[4] 3x no cartão \n')

escolha = float(input('Escolha a opção de pagamento: '))

if escolha == 1:
    print('As suas compras ficaram no valor de {}'.format(descontoPIX))

elif escolha == 2:
    print('As suas compras ficaram em {}'.format(descontoCard))

elif escolha == 3:
    print('As suas compras ficaram em {}'.format(cartao))

else:
    print('As suas compras ficaram em {}'.format(cartaoJ))
