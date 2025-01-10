print('-'*20)
print('10 Termos de uma PA')
print('-'*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + 10 * razao

for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' > ')
print('FINISH')
