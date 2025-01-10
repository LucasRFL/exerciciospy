from time import sleep
WARNING = '\033[93m'
OKGREEN = '\033[92m'

numero = int(input('Me diga um número: '))
resultado = numero % 2

sleep(2)

if resultado == 0:
    print(f'{OKGREEN}{numero} é um número par')
else:
    print(f'{WARNING}{numero} é um número impar')
