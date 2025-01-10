'''from math import factorial
n1 = int(input('Digite um número: '))
fatorial = factorial(n1)
print(fatorial)'''
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
resultado = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado *= c
    c -= 1
print('{}'.format(resultado))
