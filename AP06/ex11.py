texto = input('Digite seu texto: ').lower()

quantidade_palavras = 0
dentro_palavra = False

for i in range(len(texto)):
    if texto[i] != ' ' and dentro_palavra == False:
        quantidade_palavras += 1
        dentro_palavra = True
    elif texto[i] == ' ':
        dentro_palavra = False

print(f'Quantidade de palavras: {quantidade_palavras}')