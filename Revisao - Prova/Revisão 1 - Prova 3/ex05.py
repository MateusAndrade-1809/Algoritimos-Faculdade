def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

resultado = potencia(base, expoente)

print(resultado)