## Dado um valor inteiro, calcule quantas moedas de:
## 1, 5, 10, 25 e 50 centavos são necessárias.

centavos = [0.50, 0.25, 0.10, 0.05, 0.01]

valor = float(input('Digite um valor: '))

for centavo in centavos:
    quantidade = 0
    while valor >= centavo:
        valor -= centavo
        quantidade += 1
        
    if quantidade > 0:
        print(f'foi usado {quantidade} moedas de {centavo} centavos')
