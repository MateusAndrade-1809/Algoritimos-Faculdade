n = int(input('Digite um numero: '))

linha = n
coluna = 1

while linha <= n and linha > 0:
    texto = ''
    linha = 1
    
    while linha <= coluna:
        texto += str(linha)
        linha += 1
    print(texto)
    coluna += 1
    
linha = n 

while linha <= n and linha > 0:
    texto = ''
    coluna = 1
    
    while coluna <= linha:
        texto += str(coluna)
        coluna += 1

    print(texto)
    linha -= 1