from time import sleep
velocidade = int(input('Qual a velocidade do se veículo? '))

WARNING = '\033[93m' #Amarelo
OKGREEN = '\033[92m' #Verde
FAIL = '\033[91m' #VERMELHO
multa = (velocidade-80)*7
if velocidade <=80:
    print(f'{OKGREEN}Você está dentro do limite de velocidade, continue respeitando as leis de transito!')
else:
    print(f'{FAIL}Você está acima do limite de velocidade. O órgão responsável vai calcular a sua multa.')
    print('Calculando multa...')
    sleep(4)
    print('-----------'*20)
    print(f'{WARNING}Sua multa ficou em {multa}R$ Reais, pague dentro de 30 dias, ou seu veículo será apreendido.')
