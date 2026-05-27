a = []
b = []

print('Digite os valores da matriz a:')

for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f'a[{i}][{j}]: '))
        linha.append(valor)
    a.append(linha)

print('Digite os valores da matriz b:')

for i in range(3):
    linha = []
    for j in range(2):
        valor = int(input(f'b[{i}][{j}]: '))
        linha.append(valor)
    b.append(linha)

c = []

for i in range(2):
    linha = []
    for j in range(2):
        soma = 0

        for k in range(3):
            soma += a[i][k] * b[k][j]

        linha.append(soma)

    c.append(linha)

print('Matriz resultante:')

for linha in c:
    print(linha)