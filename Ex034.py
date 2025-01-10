salario = float(input('Qual é o salário do funcionário: '))
if salario >= 5000:
    novo = salario + (salario * 10/100)
else:
    novo = salario + (salario * 15/100)
print('Quem ganhava {} passa a ganhar {}'.format(salario, novo))
