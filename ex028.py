from random import randint
from time import sleep
import colorama
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('-=-' * 20)
player = int(input('Escolha seu número! '))
print('Analisando....')
sleep(3)
print('Você está tenso, as máquinas percebem, tome cuidado...')
sleep(3)
print('É eu sei, eu sou um saco, mas você não tem opção, jovem...')
sleep(4)
if player == computador:
    print('PARABÉNS! Você ganhou, é um feito e tanto! Na próxima eu te mato antes :)')
else:
    print('Eu sou um adversário difícil, tente novamente.')
