num_total = 0
soma = 0
num = int(input('Digite um numero para soma: '))
while num != 0:
    soma = num + soma
    num = int(input('digte outro numero: '))
    num_total += 1
media = soma / num_total
print(f'O total arrecadado é de {soma}R$')

print(f'O total de vendas foi de {num_total}')

print(f'A media de vendas é de {media}')