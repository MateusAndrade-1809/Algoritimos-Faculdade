def fechamento(cliente, valor_produto, desconto):
    print('FECHAMENTO SISTEMA')
    print(f'Nome: {cliente}')
    print(f'Valor final do produto: R${valor_produto - (valor_produto * desconto / 100)}')
    print(f'Comissao: R${desconto}')
    
cliente = input('Nome do cliente: ')
valor_produto = int(input('Digite o valor do produto: '))
desconto = int(input('Desconto: '))
print()

fechamento(cliente, valor_produto, desconto)
    