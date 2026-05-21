def positivos(lista):
    nova_lista = []
    for i in lista:
        if i >= 0:
            nova_lista.append(i)
    
    return nova_lista

lista = []
for i in range(8):
    num = int(input('Digite numeros: '))
    lista.append(num)

postivo = positivos(lista)

print(f'Lista somente com os numeros positivos: {postivo}')