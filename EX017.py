from math import hypot
num = float(input('Comprimento do cateto oposto: '))
num2 = float(input('Comprimento do cateto adjacente: '))
hi = hypot(num, num2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))
