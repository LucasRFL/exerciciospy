from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print(
        '[1] Somar\n'
        '[2] Multiplicar\n'
        '[3] Maior\n'
        '[4] Novos números\n'
        '[5] Sair do programa\n'
)
escolha = int(input('Escolha uma opção: '))
while escolha != 5:
    if escolha == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é = {}\n'
              '---------------------------------'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} x {} é = {}\n'
              '---------------------------------'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 <= n2:
            print(' O número {} é maior que {}\n'
                  '----------------------------------'.format(n2, n1))
        else:
            print('o número {} é maior que {}\n'
                  '-----------------------------------'.format(n1, n2))
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    print(
        '[1] Somar\n'
        '[2] Multiplicar\n'
        '[3] Maior\n'
        '[4] Novos números\n'
        '[5] Sair do programa\n'
    )
    escolha = int(input('Escolha uma opção: '))
print('Finalizando programa...')
sleep(2)
print('Fim do teste.')
