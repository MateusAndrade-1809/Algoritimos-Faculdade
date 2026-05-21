def analisar(lista):
    menor = lista[0]
    maior = lista[0]
    soma = 0

    for i in lista:
        if i > maior:
            maior = i

        if i < menor:
            menor = i

        soma += i

    media = soma / len(lista)

    return maior, menor, media


lista = []

numero = int(input('Digite um número: '))

while numero != 0:
    lista.append(numero)
    numero = int(input('Digite um número: '))

if len(lista) > 0:
    maior, menor, media = analisar(lista)

    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    print(f'Média: {media:.2f}')
else:
    print('Nenhum número foi digitado.')