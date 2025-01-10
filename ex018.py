from math import radians, sin, cos, tan

num = float(input('Digite o ângulo que você deseja: '))
rad = radians(num)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem o COSSENO de {:.2f}\n'
      'O ângulo de {} tem a TANGENTE de {:.2f}'.format(num, seno, num, cosseno, num, tangente))
