lista = []
lista_reversa = []
palindromo = 0

for i in range(7):
    numeros = int(input('Digite numeros inteiros: '))
    lista.append(numeros)
    
for i in lista:
    lista_reversa.append(lista[7 - i])

for i in range(7):
    if lista[i] == lista_reversa[i]:
        palindromo += 1

if palindromo == 7:
    print('A lista é palíndromo.')
else:
    print('A lista não é palíndromo.')
    
