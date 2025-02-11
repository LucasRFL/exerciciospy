print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
pprodutos = ('Lápis', 2.56,
             'Caderno', 14.25,
             'Borracha', 2.40,
             'Mochila', 144.99,
             'Estojo', 7.33,
             'Canetas', 11.29,
             'Livro', 6.45)
for pos in range(0, len(pprodutos)):
    if pos % 2 == 0:
        print(f'{pprodutos[pos]:.<30}', end='')
    else:
        print(f'R${pprodutos[pos]:>}')
print('---'*13)