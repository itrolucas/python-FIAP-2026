dados = []
lista= list()
media = 0
while True:
    dados.append(str(input('Qual o nome do aluno?: ')).capitalize())
    dados.append(float(input('Digite a nota: ')))
    dados.append(float(input('Digite a segunda nota: ')))
    lista.append(dados[:])
    dados.clear()
    pergunta = str(input('Quer continuar?: [S/N] '))
    if pergunta in 'Nn':
        break
print('=' * 50)
print('No.', end='  ')
print('NOME', end='     ')
print('MÉDIA')
print('-' * 30)
for p, info in enumerate(lista):
    print(p, end='    ')
    print(info[0], end= '    ')
    print(((info[1] + info[2]) / 2))
    while True:
        pergunta2 = int(input('Mostrar a nota de qual aluno?: [digite 999 pra brecar] '))
        if pergunta2 == 999:
            break
        else:
            print(f'As notas de {lista[p][0]} foram {lista[p][1:]}')

