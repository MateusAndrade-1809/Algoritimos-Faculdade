lista = []
lista_reversa = []

for i in range(8):
    palavra = input('Digite palavras: ')
    lista.append(palavra)
    
for i in range(8):
    lista_reversa.append(lista[7 - i])
    print(lista_reversa[i])
