from random import randint
maior = menor = 0



tupla = randint(0,999), randint(0,999), randint(0,999), randint(0,999), randint(0,999)
print(tupla)
for c in range(1, len(tupla)):
    if c == 1:
        maior = tupla[c]
        menor = tupla[c]
    else:
        if tupla[c] > maior:
            maior = tupla[c]
        if tupla[c] < menor:
            menor = tupla[c]
print(menor)
print(maior)