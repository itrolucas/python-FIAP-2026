n = 0


tupla = (int(input('Digite um número ')),
int(input('Digite um número ')),
int(input('Digite um número ')),
int(input('Digite um número ')))
print(f'os valores lidos foram: {tupla}')
print(f'O valor número 9 apareceu {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(''f'o número 3 foi encontrado pela primeira vez na posição {tupla.index(3)}')
else:
    print('Não tem o número 3 na tupla')
print('os valores pares foram ', end='')
for pos in range(0, len(tupla)):
    if tupla[pos] % 2 == 0:
        print(tupla[pos], end=' ')