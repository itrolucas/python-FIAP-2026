from random import randint

def sorteia(lista):
    for cont in range(0,5):
        n = randint(1,10)
        print(f'{n},', end=  ' ')
        lista.append(n)

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2  == 0:
            soma += valor
    print(f'\na soma dos valores pares é: {soma} ')

números = list()
sorteia(números)
somapar(números)
