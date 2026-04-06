n = int(input("Digite um número: "))

i = 1
soma = 0
sinal = 1

while i <= n:
    soma = soma + sinal * (1 / i)
    sinal = -sinal
    i = i + 1

print("Valor de S:", soma)