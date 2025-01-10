from time import sleep

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
prog = int(input('Quantas progressões devo mostrar? '))
termo = primeiro
contador = 0
'''pause = False'''
progressao = prog
while progressao != 0:
    while contador < prog:
        print('{} > '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    progressao = int(input('Quantos termos você quer mostrar a mais? '))
    prog += progressao
print('Sua progressão foi pausada.')
sleep(1)
print('Calculando números de termos exibidos...')
sleep(2)
print('Foram exibidos {} termos.'.format(contador))

'''while not pause:
    while contador < segPA:
        print('{} > '.format(termo), end='')
        termo += razao
        contador = contador + 1
        if contador >= segPA:
            print('PAUSA')
            progressao = int(input('Quantos termos você quer mostrar a mais? '))
            segPA = progressao + contador
        if progressao == 0:
            var = pause == True
            print('Sua progressão foi pausada.')
            sleep(1)
            print('Calculando números de termos exibidos...')
            sleep(2)
            print('Foram exibidos {} termos.'.format(contador))'''
