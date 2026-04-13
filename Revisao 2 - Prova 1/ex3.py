decimal = int(input('digite um numero para converter para binario: '))

binario = ''

if decimal == 0:
    binario = '0'
else:
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
        
print(f'O numero em binario é {binario}')