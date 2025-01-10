num = int(input('Digite um numero inteiro: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)

print('Escolha uma das bases de conversão')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
escolha = int(input('Escolha a base de conversão: '))


if escolha == 1:
    print('Sua escolha foi binário')

    print('Aqui está seu resultado: {}'.format(binario[2:]))
elif escolha == 2:
    print('Sua escolha foi octal')

    print('Aqui está seu resultado: {}'.format(octal[2:]))
elif escolha == 3:
    print('Sua escolha foi hexadecimal')

    print('Aqui está seu resultado: {}'.format(hexadecimal[2:]))
else:
    print('Valor invalido. Por favor, tente novamente mais tarde.')
