matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

diagonal_principal = 0
diagonal_secundaria = 0
acima = 0
abaixo = 0

for i in range(5):
    for j in range(5):
        if i == j:
            diagonal_principal += matriz[i][j]

        if i + j == 4:
            diagonal_secundaria += matriz[i][j]

        if j > i:
            acima += matriz[i][j]

        if i > j:
            abaixo += matriz[i][j]

print(f'Soma da diagonal principal: {diagonal_principal}')
print(f'Soma da diagonal secundaria: {diagonal_secundaria}')
print(f'Soma acima da diagonal principal: {acima}')
print(f'Soma abaixo da diagonal principal: {abaixo}')

if acima > abaixo:
    print('Maior regiao: acima da diagonal principal')
else:
    print('Maior regiao: abaixo da diagonal principal')