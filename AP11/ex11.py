matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

menor = matriz[0][0]
maior = matriz[0][0]

for i in range(4):
    for j in range(4):
        if matriz[i][j] < menor:
            menor = matriz[i][j]

        if matriz[i][j] > maior:
            maior = matriz[i][j]

normalizada = []

for i in range(4):
    linha = []
    for j in range(4):
        if maior == menor:
            valor_normalizado = 0
        else:
            valor_normalizado = (matriz[i][j] - menor) / (maior - menor)

        linha.append(valor_normalizado)

    normalizada.append(linha)

print('Matriz normalizada:')

for i in range(4):
    for j in range(4):
        print(f'{normalizada[i][j]:.2f}', end=' ')
    print()