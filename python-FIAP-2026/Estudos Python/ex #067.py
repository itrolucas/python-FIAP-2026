n = 0
x = 0
p = 'S'
while n >= 0 and p == 'S':
    n = int(input('Qual número de tabuada quer ver?: '))
    if n < 0:
        print('Número inválido')
        break
    x += 1
    for x in range (x,11):
        print(f'{n}X{x} = {n * x}')
    p = str(input('Quer continuar? [S / N] ')).upper().strip()

