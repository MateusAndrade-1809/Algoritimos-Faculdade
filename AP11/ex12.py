matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite um valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    
    matriz.append(linha)
    
matriz_girada = []

for j in range(4):
    linha_girada = []
    for i in range(3, -1, -1):
        linha_girada.append(matriz[i][j])
    
    matriz_girada.append(linha_girada)

for linha in matriz:
    print(linha)
print()
print('Matriz girada: ')
for linha in matriz_girada:
    print(linha)