from itertools import count
from operator import index
cont = 0
num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
numeros = (num, num2, num3, num4)
print(f'Você digitou os valores: {numeros}')
if 9 in numeros:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
else:
    print('O valor 9 não foi digitado em nenhuma posição')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        cont += 1
        print(n, end=' ')
print(f'\nNos tivemos {cont} valores pares digitados')
