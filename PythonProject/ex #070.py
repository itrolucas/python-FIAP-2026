from time import sleep

produto = preço = pergunta = 0
s = 0
contador1000 = 0


while True:
    produto = str(input('Nome do Produto:'))
    preço = int(input('Preço: '))
    if preço > 1000:
        contador1000 += 1
    s += preço
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar: [S/N] ')).upper().strip()
    if pergunta in 'Nn':
        print(f'O total da compra foi {s}')
        print(f'Produtos acima de 1000R$: {contador1000}')
        print(f'')
        break

