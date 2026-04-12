##Peça um número inteiro positivo ao usuário e determine se ele é primo utilizando while

n = int(input('Digite um número inteiro positivo: '))

divisor = 1
quantidade_divisores = 0

while divisor <= n:
    if n % divisor == 0:
        quantidade_divisores += 1
    divisor += 1

if quantidade_divisores == 2:
    print('É primo')
else:
    print('Não é primo')