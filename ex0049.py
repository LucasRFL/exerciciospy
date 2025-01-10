n = int(input('Digite o número que deseja saber a tabuada: '))
for c in range(1, 11):
    print('{} x {:1} = {}'.format(n, c, n*c))
