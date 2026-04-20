maior = 0

for contador in range(1,6):
    num = int(input('Digite um numero: '))
    
    if num > maior:
        maior = num

print(f'O maior numero digitado foi o {maior}')