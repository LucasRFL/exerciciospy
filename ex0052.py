nint = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, nint + 1):
    if nint % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n O número {} foi divisível {} vezes'.format(nint, tot))
    print('\n E por isso ele É PRIMO')
else:
    print('\n O número {} foi divisível {} vezes'.format(nint, tot))
    print('\n E por isso, ele NÃO É PRIMO')
