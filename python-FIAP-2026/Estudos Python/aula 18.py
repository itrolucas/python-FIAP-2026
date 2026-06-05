pessoas = list()
dados = list()

for p in range(0,2):
    dados.append(str(input('Qual o nome?: ')))
    dados.append(int(input('Qual a idade?: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)
for c in pessoas:
    if c[1] >= 18:
        print(f' o indivíduo {c[0], } é maior de idade')

    #if pessoas[c][1] >= 18:
        #print(pessoas[c][1])
