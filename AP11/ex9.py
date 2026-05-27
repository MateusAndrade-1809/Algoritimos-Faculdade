temperaturas = []
acima_30 = 0

for i in range(4):
    linha = []
    for j in range(7):
        temp = int(input(f'Digite a temperatura da cidade {i}, dia {j}: '))
        linha.append(temp)

        if temp > 30:
            acima_30 += 1

    temperaturas.append(linha)

maior_geral = temperaturas[0][0]
pos_linha = 0
pos_coluna = 0

for i in range(4):
    soma = 0
    maior_cidade = temperaturas[i][0]
    dia_quente = 0

    for j in range(7):
        soma += temperaturas[i][j]

        if temperaturas[i][j] > maior_cidade:
            maior_cidade = temperaturas[i][j]
            dia_quente = j

        if temperaturas[i][j] > maior_geral:
            maior_geral = temperaturas[i][j]
            pos_linha = i
            pos_coluna = j

    media = soma / 7
    print(f'Cidade {i} - Media: {media:.2f} - Dia mais quente: {dia_quente}')

print(f'Maior temperatura geral: {maior_geral}')
print(f'Posicao da maior temperatura: [{pos_linha}][{pos_coluna}]')
print(f'Registros acima de 30 graus: {acima_30}')