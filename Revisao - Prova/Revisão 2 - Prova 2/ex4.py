matriz = int(input('Digite o valor da matriz N x N: '))

lista_matriz = []

for i in range(matriz):
    linha = []
    for j in range(matriz):
        valor = int(input(f'Digite o valor [{i}][{j}]: '))
        linha.append(valor)
    lista_matriz.append(linha)
    
soma_diagonal = 0

for i in range(matriz):
    soma_diagonal += lista_matriz[i][i]
    
print(f'Soma diagonal princial: {soma_diagonal}')