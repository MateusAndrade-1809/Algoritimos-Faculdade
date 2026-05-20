def maior_trecho_crescente(lista):
    if len(lista) == 0:
        return 0

    maior = 1
    contador = 1

    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            contador += 1
        else:
            contador = 1

        if contador > maior:
            maior = contador

    return maior


lista = []

numero = int(input('Digite um número inteiro ou 0 para parar: '))

while numero != 0:
    lista.append(numero)
    numero = int(input('Digite um número inteiro ou 0 para parar: '))

resultado = maior_trecho_crescente(lista)

print(f'Lista digitada: {lista}')
print(f'Maior trecho crescente consecutivo: {resultado}')

