sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite seu sexo novamente [F/M]: ')).strip().upper()[0]
print('FIM. Sexo {} registrado com sucesso.'.format(sexo))
