print('--' * 6)
print('Sequência de fibonacci')
print('--' * 6)

termo = int(input('Quantos termos você deseja mostrar? '))
t1 = 0
t2 = 1
print('{} > {}'.format(t1, t2), end='')
contador = 3
while contador <= termo:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    contador += 1
    t1 = t2
    t2 = t3
print(' > FIM')

