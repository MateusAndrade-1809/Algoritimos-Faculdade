n = int(input('Digite o valor de n: '))

soma = 0

for i in range(1, n + 1):
    numerador = 1
    
    j = 2
    while j <= i + 1:
        numerador = numerador * j
        j = j + 1
    
    denominador = i * i
    
    termo = numerador / denominador
    
    print(f'termo {i} = {termo}')
    
    soma = soma + termo

print(f'A soma total é de {soma}')