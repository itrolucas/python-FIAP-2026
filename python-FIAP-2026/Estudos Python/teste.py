from time import sleep

lepo = ''
preço = contador1000 = pergunta = soma = menor = quantidade =  0
while True:
    #somatório para controlar as escolhas
    quantidade += 1
    nome = str(input('Nome do produto:  '))
    sleep(0.5)
    valor = int(input('Preço:  '))
    if valor>= 1000:
        contador1000 += 1
    soma += valor
    if quantidade == 1:
        menor = valor = lepo = nome
    else:
        if valor < menor:
            menor = valor
            lepo = nome
    pergunta = ' '
    #variável para iniciar um while, loop de pergunta se não estiver em 'SN'
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'O valor total foi {soma}')
print(f'produtos acima de 1000R$ foi {contador1000}')
print(f'O produto mais barato é: {lepo} ')







