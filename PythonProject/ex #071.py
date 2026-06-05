from time import sleep
valor = 0
cédula1 = 0
cédula10 = 0
cédula20 = 0
cédula50 = 0
cédula = 0
print('=' * 50)
print('BEM-VINDO AO BANCO DO LUCÃO')
print('=' * 50)
sleep(0.5)
valor = int(input('Qual o valor a ser sacado? '))
while valor != 0:
    while valor >= 50 :

        cédula50 = valor // 50
        valor = valor - (cédula50 * 50)
        print(f'Total de {cédula50} cédula(s) de 50R$')

    while valor < 50 and valor >= 20:
        cédula20 = valor // 20
        valor = valor - (cédula20 * 20)
        print(f'Total de {cédula20} cédula(s) de 20R$')

    while valor < 20 and valor >= 10:
        cédula10 = valor // 10
        valor = valor - (cédula10 * 10)
        print(f'Total de {cédula10} cédula(s) de 10R$')

    while valor >= 1:
        cédula1 = valor // 1
        valor = valor - (cédula1 * 1)
        print(f'Total de {cédula1} moeda(s) de 1R$')