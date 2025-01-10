opcao = 'nN'
soma = maior = menor = contador = 0

while opcao not in 'Nn':
    n = int(input('Digite um número: '))
    soma += n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar? [S/N] ')).strip()[0]
media = soma / contador
print('Você digitou {} números e a média foi {:.2f}'.format(contador, media))
print('O Maior valor foi {} e o menor foi {}'.format(maior, menor))
 