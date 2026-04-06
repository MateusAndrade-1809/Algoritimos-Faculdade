base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente (não negativo): "))

resultado = 1

for i in range(expoente):
    resultado = resultado * base

print("Resultado:", resultado)