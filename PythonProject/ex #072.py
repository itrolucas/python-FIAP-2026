n = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'dezoito'


while True:
    número = int(input('Qual número vc quer?: '))
    if  0 <= número <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'o seu número de escolha é {n[número]}')
