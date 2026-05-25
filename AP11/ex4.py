matriz = []
primeiro = True


for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor da entrada [{i}][{j}]: '))
        linha.append(valor)
        if primeiro:
            maior = valor
            primeiro = False

        elif valor > maior:
            maior = valor
    
    matriz.append(linha)

print(f'Maior valor: {maior}')

    