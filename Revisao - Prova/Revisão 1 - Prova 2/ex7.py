n = int(input('Digite o tamanho da matriz: '))

matriz = []

for i in range(n):
    linha = []
    
    for j in range(n):
        numero = int(input(f'Digite o valor de [{i}][{j}]: '))
        linha.append(numero)
        
    matriz.append(linha[:])
    
    
nova_matriz = []

for linha in matriz:
    nova_matriz.append(linha[:])
    
for i in range(1, n - 1):
    for j in range(1, n - 1):
        
        media = (
            matriz[i][j] + 
            matriz [i - 1][j] +
            matriz [i + 1][j] +
            matriz [i][j - 1] +
            matriz [i][j + 1]
        ) // 5
        
        nova_matriz[i][j] = media
        
print(f'Nova matriz: ')

for linha in nova_matriz:
    print(linha)
