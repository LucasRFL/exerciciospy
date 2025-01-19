from time import sleep
total = 0
produtobarato = ''
maiorvalor = 0
menorvalor = 0

print('--'*20)
print('CAMINHÃO TOMBADO')
print('--'*20)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    total += preco
    if preco > 1000:
        maiorvalor += 1
    if produtobarato == '':
        produtobarato = nome
    if menorvalor == 0:
        menorvalor = preco
    sequen = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while sequen not in 'SN':
        sequen = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if preco < menorvalor:
        menorvalor = preco
        produtobarato = nome
    if sequen == 'N':
        break
print('Calculando suas compras...')
sleep(2)
print(f'O total da compra foi R${total:.2f}')
if maiorvalor >= 1:
    print(f'Temos {maiorvalor} produtos custando mais de R$1000.00')
else:
    print('Nenhum produto ultrapassou R$1000 Reais')
print(f'O produto mais barato foi {produtobarato} que custa R${menorvalor:.2f}')
