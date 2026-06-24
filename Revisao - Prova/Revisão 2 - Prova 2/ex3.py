matriz = int(input('Digite o valor da matriz N x N: '))

lista_matriz = []
soma = 0

for i in range(matriz):
    linha = []
    for j in range(matriz):
        valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(valor)
        soma += valor
    lista_matriz.append(linha)

maior = lista_matriz[0][0]

for i in lista_matriz:
    for j in i:
        if j > maior:
            maior = j

menor = lista_matriz[0][0]

for i in lista_matriz:
    for j in i:
        if j < menor:
            menor = j
            

print(f'Soma: {soma}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')