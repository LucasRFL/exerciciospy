from time import sleep

valorC = float(input('Qual o valor do imóvel que iremos financiar? '))
valorS = float(input('Qual a sua renda mensal? '))
valorA = float(input('Em quantos anos você pretende pagar? '))
valorP = (valorC / valorA) / 12
#minimo = valorS * 30 / 100
sleep(1)
print('Sua parcela ficou em {:.2f}R$'.format(valorP))
sleep(1)
print('Verificando disponibilidade de empréstimo ✋...')
sleep(3)
# if valorP <= minimo: também funcionaria
if valorP > valorS * 0.3:
    print('Não podemos aprovar seu empréstimo, podemos apresentar uma solução.')
else:
    print('Parabéns, você conseguiu o empréstimo! Basta apenas nos informar o restante dos seus dados')
