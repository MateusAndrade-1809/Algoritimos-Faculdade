## Peça um número inteiro positivo e calcule o fatorial usando while

numero = int(input('Fale um numero inteiro positivo para fazer o fatorial dele: '))

i = 1

while numero > 1:
    i *= numero
    numero -= 1

print(i)
