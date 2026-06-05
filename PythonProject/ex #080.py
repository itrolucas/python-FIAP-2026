lista = []


for posição in range(0, 5):

    valores = (int(input('Qual o número?: ')))
    if posição == 0 or valores > lista[-1]:
        lista.append(valores)
        pos = 0
        while pos != (len(lista)):
            if lista[pos] >= valores:
                lista.insert(pos, valores)
                break
            pos += 1
print(lista)