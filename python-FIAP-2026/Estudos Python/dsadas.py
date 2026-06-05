lista = []
contador5= 0
contador = pos = 0

while True:
    valores = int(input('Digite um valor: '))
    contador +=1
    lista.append(valores)
    if 5 in lista:
        contador5 +=1
    pos += 1
    pergunta = str(input('Quer continuar?: [S/N]')).upper().strip()[0]
    if pergunta in 'N':
        print('Programa acabou!')
        break
if contador5 == 0:
    print('O número cinco não apareceu')
else:
    print(f'O número cinco apareceu')
    print(f'A lista ficou desse jeito: {lista.sort(reverse=True)}')
print(f'A lista ficou com {contador} valor(es)')