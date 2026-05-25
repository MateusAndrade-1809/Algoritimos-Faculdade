matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite um valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    
    matriz.append(linha)

soma = 0

for i in range(3):
    soma = 0
    for j in range(4):
        soma += matriz[i][j]
    print(f'Soma linha {i}: {soma}')