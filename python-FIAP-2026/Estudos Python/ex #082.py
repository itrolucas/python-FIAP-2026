listapar = []
listaimpar = []
listacompleta = []
pos = 0
while True:
    listacompleta.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer Continuar?: [S/N]')).upper().strip()[0]
    if pergunta in 'N':
        print('O programa acabou!!')
        while pos != len(listacompleta):
            if listacompleta[pos] % 2 == 0:
                listapar.append(listacompleta[pos])
            else:
                listaimpar.append(listacompleta[pos])
            pos += 1
        break
print(f'A lista completa ficou assim: {listacompleta}')
print(f'A lista de valores ímpares ficou assim: {listaimpar}')
print(f'A lista de valores pares ficou assim: {listapar}')

