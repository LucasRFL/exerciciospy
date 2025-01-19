
while True:
    n = int(input('Digite o valor que deseja saber a tabuada: '))
    print('-><-'*15)
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t} = {n*t}')
    print('-><-' * 15)
print('PROGRAMA ENCERRADO. Volte sempre que precisar')
