from random import randint
win = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)


while True:
    n = int(input('Digite um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    if jogador not in 'PI':
        print('Opção inválida. Inicie novamente o programa')
        break
    computador = randint(0, 10)
    s = n + computador
    tipo = ''
    print(f'Você escolheu {n} e o computador {computador}, a soma entre eles foi {s}')
    if jogador == 'P':
        if s % 2 == 0:
            win += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print(f'GAME OVER! Você venceu {win} vezes.')
            break
    if jogador == 'I':
        if s % 2 == 1:
            win += 1
            print('Você venceu!!')
            print('Vamos jogar novamente...')
        else:
            print(f'GAME OVER! Você venceu {win} vezes.')
            break
