def voto(a):
    if 18 <= a <= 69 :
        return print('OBRIGATÓRIO')
    elif 15 <= a <= 17 :
        return print('OPCIONAL')
    elif a > 69 or a <= 14:
        return print('NEGADO')

idade = int(input('Idade: '))
voto(idade)


