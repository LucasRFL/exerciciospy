from random import randint
from time import sleep
print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
sleep(2)
tentativas = 1
computador = randint(0, 10)
usuario = int(input('Qual é o seu palpite: '))
while usuario != computador:
    if usuario < computador:
        print('mais...')
        usuario = int(input('Tente novamente. Não são tantas opções assim. Qual é o seu palpite: '))
        tentativas += 1
    else:
        print('menos...')
        usuario = int(input('Tente novamente. Não são tantas opções assim. Qual é o seu palpite: '))
        tentativas += 1
if tentativas <= 5:
    print('Fim. Você levou {} tentativas até acertar...nada mal.'.format(tentativas))
else:
    print('Péssimo...')
