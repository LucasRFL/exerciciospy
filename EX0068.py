maioridade = 0
RegistroH = 0
M20 = 0
print('--'*20)
print('CADASTRE UMA PESSOA')
print('--'*20)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    sequencia = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while sequencia not in 'SN':
        sequencia = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if sexo == 'M':
        RegistroH += 1
    if idade >= 18:
        maioridade += 1
    if sexo == 'F':
        if idade < 20:
            M20 += 1
    if sequencia == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Foram cadastrados {RegistroH} homens.')
print(f'E temos {M20} mulheres com menos de 20 anos!')