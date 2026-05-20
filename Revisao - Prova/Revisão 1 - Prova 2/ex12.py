def ler_matriz(m, n):
    matriz = []

    for i in range(m):
        linha = []

        for j in range(n):
            valor = int(input(f'Digite o valor da posição [{i}, {j}]: '))
            linha.append(valor)

        matriz.append(linha)

    return matriz


m = int(input('Digite o valor para M: '))
n = int(input('Digite o valor para N: '))

matriz = ler_matriz(m, n)

for linha in matriz:
    print(linha)