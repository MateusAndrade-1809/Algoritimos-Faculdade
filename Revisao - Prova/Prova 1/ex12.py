n = int(input("Digite um número: "))

linha = 1

while linha <= n:
    coluna = 1
    texto = ""

    while coluna <= linha:
        texto = texto + str(coluna)
        coluna = coluna + 1

    print(texto)
    linha = linha + 1
    
linha = n - 1

while linha >= 1:
    coluna = 1
    texto = ""

    while coluna <= linha:
        texto = texto + str(coluna)
        coluna = coluna + 1

    print(texto)
    linha = linha - 1