contador = 1
pares = 0
impares = 0

while contador <= 10:
    numero = int(input(f'Digite o número {contador}: '))
    
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    contador = contador + 1

print(f'Quantidade de pares: {pares}')
print(f'Quantidade de impar: {impares}')