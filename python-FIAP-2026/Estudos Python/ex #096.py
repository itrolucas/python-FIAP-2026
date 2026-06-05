lista = list()

def mostrarlinha():
    print('-' * 30)

mostrarlinha()
print('  área do retãngulo   ')
mostrarlinha()


def área(l,c):
    areafinal = l * c
    print(areafinal)

lista.append(float(input('Largura: ')))
lista.append(float(input('Comprimento: ')))

área(lista[0], lista[1])
