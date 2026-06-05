def contador(i,f,p):
    print(f'contagem de {i} até {f} de {p} em {p}')

    if i > f:
        cont = i
        while cont >= f:
            print(cont, end= ' ')
            cont -= p
    else:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p





contador(10,0,1)
contador(1,10,2)
