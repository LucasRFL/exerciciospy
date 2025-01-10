print('Gerador de PA')
print('-=' * 10)
'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro + (10 - 1) * razao
valorPA = primeiro + razao
while valorPA < termo:
    print('{} > '.format(valorPA), end='')
    valorPA = valorPA + razao
print('{} > FIM'.format(valorPA))'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
