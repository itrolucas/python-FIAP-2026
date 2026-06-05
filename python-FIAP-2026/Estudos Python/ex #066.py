s= n = c = 0

while True:
    n = int(input('Qual número quieres?: '))
    c += 1
    if n == 999:
        break
    s+= n
print(f'Foram lidos {c-1} valores e a soma desses gurizões é {s} ')
