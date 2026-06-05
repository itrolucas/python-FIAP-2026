lanche = ["Hamburguer", "Pizza"]

while True:
    menu = input('Quer adicionar algo ao seu combo? [S/N] ').strip().upper()[0]

    if menu == 'S':
        produto = input('Digite o produto que tu quiser: ').strip()

        if 'BATATA' in produto.upper():
            tamanho = input('Batata pequena ou grande? [P/G] ').strip().upper()[0]

            while tamanho not in 'PG':
                tamanho = input('Inválido. Tente novamente [P/G]: ').strip().upper()[0]

            if tamanho == 'P':
                lanche.append('Batata pequena')
            else:
                lanche.append('Batata grande')
        else:
            lanche.append(produto)

    elif menu == 'N':
        print('OK vlw')
        break

    else:
        print('Opção inválida.')

print(f'O seu pedido final ficou assim: {lanche}')
