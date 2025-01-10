salario = float(input('Qual é o salário do funcionário: '))
salario_novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${} com 15% de aumento, passa a receber R${:.2f}'
      .format(salario, salario_novo))
