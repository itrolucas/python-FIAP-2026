produtos = ('Lápis', 2,
'Borracha', 3,
'Apontador', 2,
'Chip', 5,
'Régua', 3,
'Chocolate', 7)
print('='*50)
print('Tabela de Preços')
print('='*50)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(produtos[c], end=' ')
    print('.' * 20, end='')
    if c % 2 != 0:
        print(f' {(float(produtos[c]))}R$')