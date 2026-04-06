n = int(input("Digite um número: "))

i = 1
denominador = 0
soma = 0

while i <= n:
    denominador = denominador + i
    soma = soma + (i / denominador)
    i = i + 1

print("Valor de S:", soma)