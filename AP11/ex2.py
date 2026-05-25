matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite os numeros da matriz: '))
        linha.append(valor)
    matriz.append(linha)
    
for i in range(3):
    for j in range(3):
        print(f'matriz [{i}][{j}] = {matriz[i][j]}')