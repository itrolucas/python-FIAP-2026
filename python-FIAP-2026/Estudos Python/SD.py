maior = menor = 0
p = 'S'
s = x = 0
while p == 'S':
    n = int(input('Qual número?: '))
    x += 1
    s = s + n
    if x == 1:
        menor = maior = n
    if n > maior:
        maior = n
    else:
        menor = n
    p = str(input('Quer continuar? [S / N]')).upper().strip()
print(f'A média dos valores lidos foi {s / x}')
print(f'O menor valor lido foi {menor} e o maior foi {maior}')