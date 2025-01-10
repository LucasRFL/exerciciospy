from random import randint
from time import sleep

escolhas = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

jogador = int(input('Suas opções:\n'
                    '[0] PEDRA \n'
                    '[1] PAPEL \n'
                    '[2] TESOURA \n'
                    'QUAL É A SUA JOGADA? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!!')
sleep(0.5)

print('Computador escolheu {}'.format(escolhas[computador]))
print('Jogador jogou {}'.format(escolhas[jogador]))

if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('VITORIA DO JOGADOR ✨')
    elif jogador == 2:
        print('VITORIA DO COMPUTADOR')
    else:
        print('Jogada inválida')

elif computador == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada invalida')

elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    else:
        print('Jogada inválida')