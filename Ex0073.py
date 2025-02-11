times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitoria',
         'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR',
         'Criciúma', 'Atlético-GO', 'Cuibá')
print('Confira os times do Brasileirão Série A')
print('-=-'*9)
print(times)
print('-=-'*9)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*9)
print(f'Os 4 últimos:{times[-4:]}')
print('-=-'*9)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=-'*9)
print(f'O Bragantino está na {times.index('Bragantino')+1}º posição!')