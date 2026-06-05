from time import sleep



valores = []
pergunta = 'S'
while True:
    valor = int(input('Qual valor tu quer?: '))
    if valor not in valores:
        sleep(0.1)
        print(f'Valor {valor} adicionado... ')
        valores.append(valor)
    else:
        sleep(0.1)
        print('Valor não adicionado, pois repetiu')
    pergunta = str(input('Tu quer continuar: [S/N] ')).upper().strip()[0]
    if pergunta in 'N':
        break
valores.sort()
print(f'essa é sua lista sem repetição e em ordem: {valores}')