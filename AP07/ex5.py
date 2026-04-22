mesas = int(input('Qual a quantidade de mesas atendidas: '))

total_mesa = validos = h = r = s = total = 0

for i in range(1, mesas + 1):
    pedidos = int(input('Qual a quantidade dde pedidos feitos nessa mesa: '))
    
    for j in range(1, pedidos + 1):
        codigo = int(input('Digite o codigo do produto: '))
        if codigo <= 0 or codigo >= 4:
            print('Codigo invalido, não sera considerado...')
        elif codigo == 1:
            print('Hamburguer')
            h += 1
        elif codigo == 2:
            print('Refrigerante')
            r += 1
        elif codigo == 3:
            print('Sobremesa')
            s += 1
            
    total_mesa = (s * 9) + (r * 6) + (h * 18)
    total += total_mesa
    print(f'Valor total da mesa: {total_mesa}')
    print(f'Quantidade total de intens validos foi de {r + s + h}')

print(f'Faturamento total: {total}')
print(f'Foram vendidos:')
print(f'{h} Hamburguers')
print(f'{r} Refrigerantes')
print(f'{s} Sobremesas')