reais = float(input('Quantos reais você tem na carteira? R$'))
dolar = reais / 5.62
euro = reais / 6.09
print('Com R${:.2f} você pode comprar US${:.2f} ou {:.2f} Euros'.format(reais, dolar, euro))
