lista = []
lista_reversa = []
palindromo = 0

for i in range(7):
    numero = int(input('Digite números inteiros: '))
    lista.append(numero)

for i in range(7):
    lista_reversa.append(lista[6 - i])

for i in range(7):
    if lista[i] == lista_reversa[i]:
        palindromo += 1

print(lista)
print(lista_reversa)

if palindromo == 7:
    print('A lista é palíndromo.')
else:
    print('A lista não é palíndromo.')
    
