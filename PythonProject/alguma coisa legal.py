def ficha(nom = '<desconhecido>', gol = 0):
    print(f'O jogador {nom} fez {gol} gols')


jogador = str(input('O nome do jogador: '))
gols = str(input('número de gols: '))

if gols.isnumeric():
   gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(gol = gols)
else:
    ficha(jogador, gols)


