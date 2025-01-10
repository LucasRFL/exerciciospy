num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O numero {} é o maior entre os dois!'.format(num1))
elif num1 == num2:
    print('Não existe número maior, os dois são iguais.')
else:
    print('O numero {} é o maior entre os dois!'.format(num2))
