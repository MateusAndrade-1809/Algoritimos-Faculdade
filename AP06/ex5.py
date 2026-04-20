palavra = input('Digite uma palavra: ')

caracter = input('Digite o caracter que voce quer verificar: ')

contagem = 0

for repetido in palavra:
    if repetido == caracter:
        contagem += 1

print(f'Esse caracter apareceu {contagem} vezes na sua frase...')
