matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valores = cont = soma = coluna3 = maior = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Qual valor você que para posição ({l},{c}): '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
for som in range(0,3):
    coluna3 += matriz[som][2]
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'o somatório de todos os valores pares: {soma}')
print(f'o somatório de todos valores da terceira coluna: {coluna3}')
matriz[1].sort(reverse=True)
print(f'o maior valor da segunda linha é: {matriz[1][0]}')
