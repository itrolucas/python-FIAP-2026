from random import randint
from time import sleep



n = contadorvitorias = 0

while True:
    random = randint(1, 10)
    n = int(input('Qual número de escolha?: '))
    escolha = str(input('Par ou ímpar? [P/I]:')).upper()
    sleep(0.5)
    s = n + random
    print(f'DEU PAR' if s % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P' and s % 2 == 0:
        print(f'Você venceu!. A máquinha escolheu o número {random}')
        contadorvitorias += 1
    elif escolha == 'I' and s % 2 != 0:
        print(f'Você venceu!. A máquinha escolheu o número {random}')
        contadorvitorias += 1
    else:
        print(f'Você perdeu! A máquinha escolheu o número {random}')
        break
print(f'Você venceu {contadorvitorias} vez(es) seguidas')





