## Peça um valor inteiro positivo ao usuário e determine quantas cédulas de R$100,
## R$50, R$20, R$10, R$5 e R$1 são necessárias para formar esse valor, utilizando
## estruturas de repetição.

valor = int(input('Digite um valor inteiro positivo: '))

cedulas = [100, 50, 20, 10, 5, 1]

for cedula in cedulas:
    quantidade = 0
    while valor >= cedula:
        valor -= cedula
        quantidade += 1
        
    if quantidade > 0:
        print(f'foi utilizado {quantidade} cedula(s) de {cedula} reais')