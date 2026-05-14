def processar_pedidos(estoque_inicial):
    estoque = estoque_inicial
    atendidos = 0
    continuar = True
    
    while estoque > 0 and continuar:
        pedido = int(input('Digite o peso desejado de sementes: '))
        
        if pedido < 0:
            continuar = False
        elif pedido > estoque:
            print('Pedido negado. Estoque insuficiente.')
        else:
            estoque -= pedido
            atendidos += 1
            print('Pedido aceito')
            print(f'Quantidade restante no estoque de {estoque}kg')

    print(f'Agricultores atendidos: {atendidos}')
    print(f'Sobra no silo: {estoque:.2f} kg')
    
estoque_incial = int(input('Digite a quantidade do silo em kg: '))

processar_pedidos(estoque_incial)