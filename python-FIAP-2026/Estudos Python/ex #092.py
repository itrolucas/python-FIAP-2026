from datetime import datetime

dicionário = {}


dicionário["Nome"] = str(input('Nome do trabalhador: '))
dicionário["Ano de nascimento"] = int(input('Ano de nascimento: '))
dicionário["CPTS"] = int(input('Carteira de trabalho: (0 se não tiver) '))
dicionário["idade"] = datetime.now().year - dicionário["Ano de nascimento"]
if dicionário["CPTS"] == 0:
    for k,v in dicionário.items():
        print(f'  -{k} tem valor {v}')
else:
    dicionário["Ano de contratação"] = int(input('Ano de contratação: '))
    dicionário["Salário"] = float(input('Salário: '))
    for k,v in dicionário.items():
        print(f'-  {k} tem valor {v}')
    razão = 30
    print(f'a idade do trabalhador é {dicionário["idade"]} e ele vai se aposentar com'
          f'{dicionário["idade"]+31}anos')

