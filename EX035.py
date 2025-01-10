line = float(input('Informe a primeira linha: '))
line2 = float(input('Informe a segunda linha: '))
line3 = float(input('Informe a terceira linha: '))
if (line + line2 < line3) or (line + line3 < line2) or (line2 + line3 < line):
    print('Não é um triângulo')
elif (line == line2) and (line == line3):
    print('este é um triângulo equilatero.')
elif (line == line2) or (line == line3) or (line2 == line3):
    print('Este é um triângulo Isósceles')
else:
    print('Este é um triângulo escaleno')
