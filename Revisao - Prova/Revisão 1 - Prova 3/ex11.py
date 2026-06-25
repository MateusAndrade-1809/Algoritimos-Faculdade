def contar_ocorrencias(valores, procurado, indice):
    if indice >= len(valores):
        return 0

    if valores[indice] == procurado:
        return 1 + contar_ocorrencias(valores, procurado, indice + 1)
    else:
        return contar_ocorrencias(valores, procurado, indice + 1)


def primeira_posicao(valores, procurado, indice):
    if indice >= len(valores):
        return -1

    if valores[indice] == procurado:
        return indice
    else:
        return primeira_posicao(valores, procurado, indice + 1)
