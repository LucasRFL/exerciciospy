distancia = float(input('Diga a distância da sua viagem em KM: '))
if distancia <= 200:
    valor = distancia * 0.5
    print('A sua viagem vai custar R${}'.format(valor))
else:
    valor2 = distancia * 0.45
    print('Sua viagem vai custar R${}'.format(valor2))
