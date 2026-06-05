from random import randint

jogos = int(input('Quantos jogos você quer sortear?: '))
dados = list()
lista = list()
while True:
    num = (randint(0,60))
    if num not in dados:
        dados.append(num)
    if len(dados) == 6:
        lista.append(dados[:])
        dados.clear()
    if len(lista) == jogos:
        break
for p, c in enumerate(lista):
    print(f'Jogo {p+1}: {c}')


