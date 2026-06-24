def soma_ate(n):
    if n == 0:
        return 0
    return n + soma_ate(n - 1)

numero = int(input('Digite um numero: '))

resultado = soma_ate(numero)

print(f'Numero: {numero}, Soma: {resultado}')