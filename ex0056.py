maioridadehomem = 0
somaIdade = 0
nomevelho = ''
mediaidade = 0
totmulher = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaIdade / 4
print('A média de idade do grupo é de {} ANOS'.format(mediaidade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Nos temos um total de {} mulheres com menos de 20 anos.'.format(totmulher))
