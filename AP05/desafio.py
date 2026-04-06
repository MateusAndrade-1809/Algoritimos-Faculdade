total_vendido = 0
quantidade_vendas = 0
escolha_usuario = -1
p1 = 0
p2 = 0
p3 = 0

while escolha_usuario != 0:
    print('-------------SISTEMA DE CAIXA---------------')
    print('1 - Registrar venda')
    print('2 - Mostrar total vendido')
    print('3 - Mostrar quantidade de vendas')
    print('4 - Mostrar valor médio das vendas')
    print('5 - Mostrar quantidade vendida por tipo de produto')
    print('0 - Encerrar sistema')

    escolha_usuario = int(input('Escolha uma opção de 1 a 5 (0 para encerrar o sistema): '))

    if escolha_usuario not in [1, 2, 3, 4, 5, 0]:
        print('Opção inválida. Por favor escolha uma opção válida.')

    if escolha_usuario == 1:
        print('1 - Lanche')
        print('2 - Bebida')
        print('3 - Sobremesa')
        op_1 = int(input('Escolha uma das opções: '))

        if op_1 not in [1, 2, 3]:
            print('Opção inválida. Escolha uma opção válida.')
        else:
            valor = float(input('Digite o valor da venda: '))

            if valor <= 0:
                print('Valor inválido, digite um valor maior que 0')
            else:
                total_vendido += valor
                quantidade_vendas += 1

                if op_1 == 1:
                    p1 += 1
                if op_1 == 2:
                    p2 += 1
                if op_1 == 3:
                    p3 += 1

    if escolha_usuario == 2:
        print(f'O valor total vendido foi de R${total_vendido:.2f}')

    if escolha_usuario == 3:
        print(f'A quantidade total de vendas foi de {quantidade_vendas} produtos')

    if escolha_usuario == 4:
        if quantidade_vendas > 0:
            print(f'O valor médio das vendas é de R${total_vendido / quantidade_vendas:.2f}')
        else:
            print('Nenhuma venda registrada')

    if escolha_usuario == 5:
        print(f'A quantidade total de lanches vendidos é de {p1} lanches')
        print(f'A quantidade total de bebidas vendidas é de {p2} bebidas')
        print(f'A quantidade total de sobremesas vendidas é de {p3} sobremesas')

print('-------------SISTEMA ENCERRADO--------------')
print(f'Total vendido: R${total_vendido:.2f}')
print(f'Quantidade total de vendas: {quantidade_vendas}')

if quantidade_vendas > 0:
    print(f'Valor médio das vendas: R${total_vendido / quantidade_vendas:.2f}')
else:
    print('Valor médio das vendas: R$0.00')

print(f'Quantidade de vendas de lanche: {p1}')
print(f'Quantidade de vendas de bebida: {p2}')
print(f'Quantidade de vendas de sobremesa: {p3}')