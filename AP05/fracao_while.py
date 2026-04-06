n = int(input("Digite um número: "))

i = 1
soma = 0

while i <= n:
    soma = soma + (1 / i)
    i = i + 1

print("Valor de S:", soma)