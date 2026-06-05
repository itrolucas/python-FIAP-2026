from random import randint
cartelpc= cartelpessoa =  0



while True:
    computador = randint(1, 10)
    take = int(input('Qual seu número de escolha?: '))
    pi = str(input('Impar ou Par? [P / I]')).upper().strip()
    s = computador + take
    print(f'O computador escolheu {computador} ')
    if pi == 'P':
        if s % 2 == 0:
            print('DEU PAR! TU GANHOU!')
            cartelpessoa += 1
        else:
            print('DEU IMPAR! TU PERDEU!')
            cartelpc += 1
    if pi in 'Ii':
        if s % 2 != 0:
            print('DEU IMPAR! TU GANHOU!')
            cartelpessoa += 1
        else:
            print('DEU PAR! TU PERDEU!')
            cartelpc += 1
    pergunta = str(input('Quer continuar? [S / N] ')).upper().strip()
    if pergunta == 'N':
        print(f'Você ganhou {cartelpessoa} vez(es) e perdeu {cartelpc} veze(es)')
        break







