from time import sleep
lista = list()

#def pode_idade(idade,renda,emprestimo):
        #situacao = ' '
        #if idade >= 18 and (20 * renda) >= emprestimo :
            #situacao = 'Aprovado'
        #if situacao == 'Aprovado':
            #print(f'O usuário {nome} foi aprovado!')
        #else:
            #print(f'O usuário {nome} foi reprovado!')
        #return idade, renda, emprestimo, nome

def pode_aprovar(idade,renda,valor):
    while resp in 'Ss':
        nome = str(input('Nome do Cliente: ')).capitalize().strip()
        sleep(0.3)

        idade = int(input('Idade do Cliente: '))
        sleep(0.3)

        renda = float(input('Renda Mensal: '))
        sleep(0.3)

        emprestimo = float(input('Valor do empréstimo: '))
        sleep(0.3)

        parcelas = int(input('Números de parcelas: '))
        sleep(0.3)

#Programa principal
resp = 'S'
while resp in 'Ss':
    nome = str(input('Nome do Cliente: ')).capitalize().strip()
    sleep(0.3)

    idade = int(input('Idade do Cliente: '))
    sleep(0.3)

    renda = float(input('Renda Mensal: '))
    sleep(0.3)

    emprestimo = float(input('Valor do empréstimo: '))
    sleep(0.3)

    parcelas = int(input('Números de parcelas: '))
    sleep(0.3)

    while 24 < parcelas or parcelas <= 2:
        parcelas = int(input('Valor inválido!!! Tente novamente... [3X-24X] '))
        sleep(0.3)

    if parcelas <= 6:
        taxa = (emprestimo * ( 1 + 0.05) ** parcelas)

    elif 12 <= parcelas <= 12:
        taxa = emprestimo * ( 1 + 0.08) ** parcelas

    elif 24 <= parcelas <= 24:
        taxa = emprestimo * ( 1 + 0.10) ** parcelas
    definir_taxa(taxa)

    resp = str(input('Quer continuar cadastrando?: [S/N]')).strip().upper()[0]








