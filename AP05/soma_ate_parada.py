num_total = 0
soma = 0
num = int(input('Digite um numero para soma: '))
while num != 0:
    soma = num + soma
    num = int(input('digte outro numero: '))
    num_total += 1
print(f'sua soma é de {soma}')

print(f'O total de numeros digitados foi de {num_total}')