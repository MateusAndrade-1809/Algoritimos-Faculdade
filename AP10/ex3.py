lista = []
lista_par = []
lista_impar = []
par = 0
impar = 0

for i in range(11):
    numero = int(input('Digite numeros inteiros: '))
    lista.append(numero)
    
for i in lista:
    if i % 2 == 0:
        par += 1
        lista_par.append(i)
    else:
        impar += 1
        lista_impar.append(i)

print(f'Quantidade de pares: {par}')
print(f'Quantidade de impares: {impar}')
print(f'Pares: {lista_par}')
print(f'Impares: {lista_impar}')

