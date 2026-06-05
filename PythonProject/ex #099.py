from time import sleep
maior = menor = 0


def números(* num):
    maior = menor = 0
    print(f'Analisando os valores passados...')
    cont = 0
    while len(num) != cont:
        for loop in num:
            if cont == 0:
                maior = menor = loop
            else:
                if loop > maior:
                    maior = loop
                if loop < menor:
                    menor = loop
            cont += 1
            if cont != len(num):
                print(loop, end=' ')
            else:
                print(loop)
            sleep(0.4)
    print(f'o maior número lido foi {maior}')
    print(f'o menor número lido foi {menor}')
    print(30 * '~')


números(1,2,3,4,5,6)
números(8,7,2)
