matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

qtd_picos = 0

for i in range(1, 4):
    for j in range(1, 4):
        valor = matriz[i][j]

        cima = matriz[i - 1][j]
        baixo = matriz[i + 1][j]
        esquerda = matriz[i][j - 1]
        direita = matriz[i][j + 1]

        if valor > cima and valor > baixo and valor > esquerda and valor > direita:
            print(f'Pico encontrado em [{i}][{j}] com valor {valor}')
            qtd_picos += 1

print(f'Quantidade de picos: {qtd_picos}')