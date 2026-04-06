num_total = 0
soma = 0

temp = int(input('Digite uma temperatura: '))
maior = temp
menor = temp

while temp != -1:
    temp = int(input('digte outra temperatura: '))
    num_total += 1
    soma = temp + soma
    
    if temp > maior:
        maior = temp
    
    if temp < menor:
        menor = temp

media = soma / num_total

print(f'A temepratura total foi de {num_total}')

print(f'A media de temperatura é de {media}')

print("Maior valor:", maior)
if menor != -1:
    print('Menor valor:', menor)