from time import sleep

contpessoas = maior = menor = 0
dados = list()
pessoas = list()

while True:
    dados.append(str(input('Nome da pessoa: ')))
    contpessoas += 1
    dados.append(float(input('Peso da pessoa: ')))
    if len(dados) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        else:
            if dados[1] < menor:
                menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    sleep(0.5)
    pergunta = str(input('Quer Continuar: [S/N]')).upper().strip()[0]
    if pergunta in 'Nn':
        sleep(0.5)
        print('Programa acabou!!')
        break
print('=' * 50)
print(f'Ao todo, você cadastrou {len(dados)} pessoas ao todo.')
print(f'o maior peso foi de {maior}Kg.', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'{p[0]}')
print(f'o menor peso foi de {menor}Kg.', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'{p[0]}')
print('=' * 50)
