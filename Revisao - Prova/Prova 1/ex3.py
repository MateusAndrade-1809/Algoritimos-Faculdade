num_binario_entrada = input("Digite um número binário: ")
num_decimal = 0
expoente = len(num_binario_entrada) - 1
for digito in num_binario_entrada:
    num_decimal += int(digito) * (2 ** expoente)
    expoente -= 1
print(f"O número binário {num_binario_entrada} é igual a {num_decimal} em decimal.")