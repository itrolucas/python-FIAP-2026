aberto = '('
fechado = ')'
contadoraberto = contadorfechado = 0


pergunta = str(input('Escreva sua expressão: '))
for c in pergunta:
    if '(' in c:
        contadoraberto += 1
    elif ')' in c:
        contadorfechado += 1
if contadorfechado == contadoraberto:
    print('A expressão é válida')
else:
    print('A expressão é inválida')