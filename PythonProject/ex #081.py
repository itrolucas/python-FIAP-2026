lista = []
contador5= 0
contador = 0

while True:
    lista.append(int(input('Digite um valor:')))
    contador+=1
    if 5 in lista:
        contador5 +=1
    pergunta = str(input('Quer continuar?: [S/N]')).upper().strip()[0]
    if pergunta in 'N':
        print('O programa acabou!')
        break
if contador5 == 0:
    print('O número cinco não apareceu')
else:
    print(f'O número cinco apareceu')
print(f'A lista ficou com {contador} valor(es)')
lista.sort(reverse=True)
print(f'A lista ficou desse jeito em ordem decrescente: {lista}')


