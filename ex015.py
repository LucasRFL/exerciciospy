km = float(input('Quantos KMs foram percorridos durante o aluguel? '))
dias = int(input('Por quantos dias o veículo foi alugado? '))
precoTotal = (km * 0.15) + (dias * 60)
print('O total a se pagar é R${:.2f}'.format(precoTotal))
