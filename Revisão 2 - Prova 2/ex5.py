matriz = int(input('Digite o valor da matriz N x N: '))

lista_matriz = []
pares = 0

for i in range(matriz):
    linha = []
    for j in range(matriz):
        valor = int(input(f'Digite o valor para posição [{i}][{j}]: '))
        linha.append(valor)
        
    lista_matriz.append(linha)

for i in lista_matriz:
    for j in i:
        if j % 2 == 0:
            pares += 1

print(f'Existem {pares} numeros pares na matriz')