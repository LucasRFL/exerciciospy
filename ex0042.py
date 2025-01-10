linha = int(input('Informe a primeira linha: '))
linha2 = int(input('Informe a segunda linha: '))
linha3 = int(input('Informe a terceira linha: '))

if (linha + linha2 < linha3) or (linha + linha3 < linha2) or (linha2 + linha3 < linha):
    print('Não é um triângulo')

elif (linha == linha2) and (linha == linha3):
    print('Esse é um triângulo equilatero!')

elif (linha == linha2) or (linha == linha3):
    print('Esse é um triâgulo isoceles!')

else:
    print('Estas medidas podem formar um triângulo escaleno!')
