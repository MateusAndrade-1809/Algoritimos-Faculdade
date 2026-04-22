n = int(input('Digite um numero: '))
soma = 0
maior = 0
multiplo = 0

for i in range(1, n + 1):
    coluna = ''
    for j in range(1, i + 1): 
        coluna += str(j) + ''
        soma += j
        if j > maior:
            maior = j
        if j % 3 == 0:
            multiplo += 1
    print(coluna)
    print(f'soma = {soma}')
    soma = 0
    print(f'maior = {maior}')
    print(f'multiplos de 3 = {multiplo}')
    multiplo = 0
    
    
        