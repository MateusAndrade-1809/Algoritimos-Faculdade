soma = int(input('Digite uma soma: '))

numerador = 1

total = 0

for numerador in range(1, soma + 1):
    denominador = numerador ** 2
    total += numerador / denominador

print(total)