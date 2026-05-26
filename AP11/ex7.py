matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)
    
pares = []
impares = []

for i in range(4):
    qtd_pares = 0
    
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            qtd_pares += 1
            
    pares.append(qtd_pares)
    
for j in range(4):
    qtd_impares = 0
    
    for i in range(4):
        if matriz[i][j] % 2 == 0:
            qtd_impares += 1
            
    impares.append(qtd_impares)
    
print(f'Pares: {pares}')
print(f'Impares: {impares}')