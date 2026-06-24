def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

numero = int(input('Digite um numero: '))

resultado = contar_digitos(numero)

print(f'Quantidade de digitos: {resultado}')
