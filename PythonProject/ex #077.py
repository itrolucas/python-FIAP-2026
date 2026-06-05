palavras = ('batuta', 'flamengo', 'igo jair', 'lepo americas')

for c in palavras:
    print(f'\na palavra {c.upper()} tem as vogais: ', end='')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')