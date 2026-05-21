
produto = input('Digite um produto (fim para parar): ')
dic = {}

while produto != 'fim':
    preco = int(input('Dgite o preço desse produto: '))
    dic[produto] = preco
    
    produto = input('Digite um produto (fim para parar): ')
    
primeiro = True
    
for chave, valor in dic.items():
    if primeiro:
        menor = valor
        maior = valor
        mais_caro = chave
        mais_barato = chave
        primeiro = False
    
    else:
        if valor > maior:
            maior = valor
            mais_caro = chave
        
        if valor < menor:
            menor = valor
            mais_barato = chave

print(f'Produto mais caro: {mais_caro}')
print(f'Produto mais barato: {mais_barato}')

