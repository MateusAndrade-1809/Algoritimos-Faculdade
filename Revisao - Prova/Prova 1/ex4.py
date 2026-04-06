valor = int(input("Digite um valor inteiro positivo: "))
cedulas = [100, 50, 20, 10, 5, 1]

print(f"Para o valor R$ {valor}, são necessárias:")

for cedula in cedulas:
    quantidade = 0
    while valor >= cedula:
        valor -= cedula
        quantidade += 1
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R$ {cedula}")