s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        s += num
print('A soma de todos os {} inteiros pares é {}'.format(cont, s))
