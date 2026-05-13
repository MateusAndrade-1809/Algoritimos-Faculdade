numero = int(input('Digite um numero inteiro positivco: '))

media = 0
quantidade = 0
maior_valor = 0
menor_valor = 99999999999999999
while numero != 0:
    if numero > 0:
        quantidade += 1
        if numero > maior_valor:
            maior_valor = numero
            
        if numero < menor_valor:
            menor_valor = numero
        
        numero2 = numero
        media = numero2 / quantidade
    
    else:
        print('O numero devera ser inteiro e positivo')
    
    numero = int(input('Digite um numero inteiro positivco: '))
        
print(f'A quantidade de numeros foi de {quantidade} numeros')
print(f'A media dos numeros digitados foi de {media}')
print(f'O maior valor foi de {maior_valor}')
print(f'O menor valor foi de {menor_valor}')