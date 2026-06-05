times = 'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'EC Vitória', 'Internacional', 'Ceará SC', 'Fortaleza', 'Juventude', 'Sport Recife'

print(f'os primeiros 5 colocados são {times[:5]}')
print('=' * 100)
print(f'os últimos 4 colocados são {times[16:21]}')
print('=' * 100)
print(f'os times em ordem alfabética: {sorted(times)}')
print('=' * 100)
print(f'O Juventude está na posição {times.index('Juventude') + 1}')