from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nascimento
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1
print('Ao todo tivemos {} maiores de idade'.format(cont))
print('E também tivemos {} menores de idade'.format(cont2))