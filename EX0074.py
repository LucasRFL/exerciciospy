from random import randint, sample

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valor sorteados foram: ', end='')

for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')