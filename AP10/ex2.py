lista = []
soma = 0

for i in range(6):
    numero = int(input('Digite numeros reais: '))
    lista.append(numero)

for i in lista:
    soma += i

media = soma / len(lista)

print(f'Soma: {soma}')
print(f'Media: {media}')