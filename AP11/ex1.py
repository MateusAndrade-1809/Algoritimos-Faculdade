lista = []

for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor de [{i}][{j}]: '))
        linha.append(valor)
    
    lista.append(linha)

for i in lista:
    print(i)