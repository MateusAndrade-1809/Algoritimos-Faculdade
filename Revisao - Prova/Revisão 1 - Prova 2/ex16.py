def analisar_precos(produtos):
    media = sum(produtos.values()) / len(produtos)

    produto_mais_caro = max(produtos, key=produtos.get)
    produto_mais_barato = min(produtos, key=produtos.get)

    acima_da_media = []

    for produto, preco in produtos.items():
        if preco > media:
            acima_da_media.append(produto)

    return produto_mais_caro, produto_mais_barato, acima_da_media


produtos = {}

produto = input('Digite o nome do produto: ')

while produto != 'fim':
    preco = float(input('Digite o preço do produto: R$ '))

    produtos[produto] = preco

    produto = input('Digite o nome do produto: ')

if len(produtos) > 0:
    media = sum(produtos.values()) / len(produtos)

    mais_caro, mais_barato, acima_media = analisar_precos(produtos)

    print(f'\nMédia dos preços: R$ {media:.2f}')
    print(f'Produto mais caro: {mais_caro} - R$ {produtos[mais_caro]:.2f}')
    print(f'Produto mais barato: {mais_barato} - R$ {produtos[mais_barato]:.2f}')
    print(f'Produtos acima da média: {acima_media}')
else:
    print('Nenhum produto foi cadastrado.')