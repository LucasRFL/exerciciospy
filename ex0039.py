import datetime
hoje = datetime.date.today().year

nascimento = int(input('Qual o seu ano de nascimento: '))
idade = hoje - nascimento
alistamento = nascimento + 18
saldo = alistamento - hoje

if alistamento > hoje:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, hoje))
    print('faltam {} para você se alistar!'.format(saldo))
    print('Seu alistamento será em {}'.format(alistamento))

elif alistamento == hoje:
    print('Quem nasceu em {} tem {} em {}.'.format(nascimento, idade, hoje))
    print('Seu alistamento é agora em {}'.format(alistamento))
    print('Se aliste imediatamente!')

else:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, hoje))
    print('VOCÊ JA DEVERIA TER SE ALISTADO HÁ {} ANOS.'.format(hoje - alistamento))
    print('Seu alistamento foi em {}'.format(alistamento))
