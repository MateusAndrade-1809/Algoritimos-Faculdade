def calcular_maior_pontuacao(jogo):
    n = len(jogo)
    m = len(jogo[0])

    melhor = []

    for i in range(n):
        linha = []

        for j in range(m):
            if i == 0 and j == 0:
                linha.append(jogo[i][j])

            elif i == 0:
                linha.append(linha[j - 1] + jogo[i][j])

            elif j == 0:
                linha.append(melhor[i - 1][j] + jogo[i][j])

            else:
                vindo_de_cima = melhor[i - 1][j]
                vindo_da_esquerda = linha[j - 1]

                if vindo_de_cima > vindo_da_esquerda:
                    linha.append(vindo_de_cima + jogo[i][j])
                else:
                    linha.append(vindo_da_esquerda + jogo[i][j])

        melhor.append(linha)

    return melhor[n - 1][m - 1]


n = int(input('Digite a quantidade de linhas: '))
m = int(input('Digite a quantidade de colunas: '))

jogo = []

for i in range(n):
    linha = []

    for j in range(m):
        valor = int(input(f'Digite a pontuação da posição [{i}][{j}]: '))
        linha.append(valor)

    jogo.append(linha)


resultado = calcular_maior_pontuacao(jogo)

print(f'Maior pontuação possível: {resultado}')