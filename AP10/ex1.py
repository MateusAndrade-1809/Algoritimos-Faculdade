lista = []
contador = 0

while contador < 5:
    numero = int(input('Digite numeros interios: '))
    contador += 1
    lista.append(numero)

print(f'Lista completa: {lista}')

for i in lista:
    print(i)