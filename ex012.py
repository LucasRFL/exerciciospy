# Outra forma de fazer o calculo seria valor_desconto = precoProduto - (precoProduto * 5 / 100)

precoProduto = float(input('Qual o valor do produto: '))
valor_desconto = 100 * 0.05
desconto = precoProduto * 0.95
valor_cartao = precoProduto + (precoProduto * 0.09)
print('O produto que custava R${}, com desconto de 5% referente ao pix, custa R${:.2f}, aproveite!'
      .format(precoProduto, desconto))
print('A sua porcentagem de desconto é {}%'.format(valor_desconto))

print('O produto no cartão de crédito em 1x custa R${} e acima de 2x {:.2f}'.format(precoProduto, valor_cartao))
