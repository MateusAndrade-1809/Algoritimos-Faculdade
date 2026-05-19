def contar_frequencia(texto):
    pontuacoes = '.,;:!?()[]{}"\'-'

    texto = texto.lower()

    for pontuacao in pontuacoes:
        texto = texto.replace(pontuacao, '')

    palavras = texto.split()

    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


def pegar_top_3(frequencia):
    top_3 = []

    for palavra, quantidade in frequencia.items():
        if len(top_3) < 3:
            top_3.append([palavra, quantidade])
        else:
            menor_posicao = 0

            for i in range(1, 3):
                if top_3[i][1] < top_3[menor_posicao][1]:
                    menor_posicao = i

            if quantidade > top_3[menor_posicao][1]:
                top_3[menor_posicao] = [palavra, quantidade]

    return top_3


texto = input('Digite um parágrafo: ')

frequencia = contar_frequencia(texto)

top_3 = pegar_top_3(frequencia)

print('Frequência das palavras:')

for palavra, quantidade in frequencia.items():
    print(f'{palavra}: {quantidade}')

print('Top 3 palavras mais frequentes:')

for palavra, quantidade in top_3:
    print(f'{palavra}: {quantidade} vez(es)')