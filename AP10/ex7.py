lista = []
nova_lista = []
novo_produto = 0
for i in range(8):
    produto = int(input('Digite o preço do produto: '))
    lista.append(produto)
    
for i in lista:
    if i < 100:
        novo_produto = i + (i * 10 / 100)
        nova_lista.append(novo_produto)
    else:
        novo_produto = i + (i * 5 / 100)
        nova_lista.append(novo_produto)


print(f'Preços originais: {lista}')
print(f'Preços reajustados: {nova_lista}')