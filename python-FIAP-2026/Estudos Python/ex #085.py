números = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)
print(f'os valores pares são {números[0]} e os valores ímpares são {números[1]}')



#for n in números:
    #if n[0] % 2 == 0:
        #pares.append(n)
    #else:
        #impares.append(n)


