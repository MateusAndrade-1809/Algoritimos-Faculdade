numero = int(input('Digite um número (0 para parar): '))

if numero == 0:
    maior = 0
else:
    anterior = numero
    contador = 1
    maior = 1

    numero = int(input('Digite um número (0 para parar): '))

    while numero != 0:
        if numero > anterior:
            contador = contador + 1
        else:
            contador = 1
        
        if contador > maior:
            maior = contador
        
        anterior = numero
        
        numero = int(input('Digite um número (0 para parar): '))

print(f'Maior sequência crescente: {maior}')