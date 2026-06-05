informação = dict()
visu = list()

informação['Nome']= str(input('Nome: '))
informação['Média'] = float(input('Qual a média?: '))
print(f'o nome é igual a {informação["Nome"]} ')
print(f'a média é igual a {informação["Média"]}')
if informação["Média"] >= 7:
    print(f'A situação é aprovado')
elif 4 < informação["Média"] < 7:
    print(f'A situação é recuperação')
else:
    print(f'A situação é reprovado: ')