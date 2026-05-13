'''Considere a série:
***imagem***
Escreva um programa que leia um valor inteiro n e calcule os n primeiros termos
dessa série e sua soma final.
Observação: o numerador de cada termo é formado por um produtório sequencial
começando em 2, e o denominador é o quadrado da posição do termo'''
total = 0
valor = int(input('Digite um valor inteiro: '))

i = 1

while i <= valor:
    numerador = 1
    j = 2

    while j <= i + 1:
        numerador *= j
        j += 1

    denominador = i ** 2
    formula = numerador / denominador
    total += formula

    i += 1

print(total)
