'''
Calcule o valor final de um produto comprado pela internet.

Leia:

preço do produto
percentual de imposto (valor de 0 a 100)
valor do frete
Calcule e apresente:

Valor de imposto a ser cobrado
Valor total (preço somado ao imposto e frete)
Saída esperada:

Resumo da compra
----------------
Valor do imposto: ...
Valor total: ...
'''

preco_produto = int(input('Qual o preço do produto: '))
prec_imposto = int(input('Qual o percentual do imposto (de 0 a 100): '))
frete = int(input('Qual o valor do frete: '))
imposto = preco_produto * prec_imposto / 100
(print(f'O valor do imposto é de {imposto}'))
valor_total = print(f'O valor total do produto é de {preco_produto + imposto + frete}')
