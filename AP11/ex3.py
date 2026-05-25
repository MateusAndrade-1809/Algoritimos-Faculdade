matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite o valor da entrada [{i}][{j}]: '))
        linha.append(valor)
        soma += valor
    matriz.append(linha)
    
print(f'Soma total: {soma}')
