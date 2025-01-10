from datetime import date
atual = date.today().year

nascimento = int(input('Qual o seu ano de nascimento? '))
idade = atual - nascimento

if idade <= 9:
    print('Sua CLASSIFICAÇÃO: MIRIM!')

elif idade <= 14:
    print('Sua CLASSIFICAÇÃO: INFANTIL!')

elif idade <= 19:
    print('Sua CLASSIFICAÇÃO: JUNIOR!')

elif idade <= 25:
    print('Sua CLASSIFICAÇÃO: SENIOR!')
else:
    print('Sua CLASSIFICAÇÃO: MASTER, PARABÉNS!')