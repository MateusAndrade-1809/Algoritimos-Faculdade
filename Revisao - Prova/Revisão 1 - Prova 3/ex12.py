def multiplicar(a, b):
    if b == 0:
        return 0

    if b > 0:
        return a + multiplicar(a, b - 1)

    return -multiplicar(a, -b)


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

resultado = multiplicar(a, b)

print(f'Resultado: {resultado}')